from concurrent import futures

import grpc
import psycopg2
import bcrypt
import secrets
import _credentials
import contextlib
import jwt
from datetime import datetime, timedelta

import auth_pb2
import auth_pb2_grpc

USERNAME = "noah"
PASSWORD = "amicia"
HOST = "127.0.0.1"

with open("credentials/private_key.pem", "rb") as f:
    PRIVATE_KEY = f.read()

with open("credentials/public_key.pem", "rb") as f:
    PUBLIC_KEY = f.read()


# For JWT
AuthServerName = "Localhost"
AudienceName = "Local"

# Blacklisted tokens
REVOKED_TOKENS = set()

# Connect to db
try:
    conn = psycopg2.connect(
        dbname="quackmed",
        user=USERNAME,
        password=PASSWORD,
        host=HOST
    )

    cur = conn.cursor()

except:
    print("Connection error")
    exit()

# Convert the list of bytes to a single variable
def db_binary_to_binary(db_binary):
    binary = b''
    for collumn in db_binary:
        for byte in collumn:
            binary = binary + byte
    return binary

# Create token for auth
def create_jwt(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "iss": AuthServerName,
        "aud": AudienceName,
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")

# Verify token for auth
def verify_jwt(token: str) -> dict:
    return jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"], audience=AudienceName, issuer=AuthServerName)

# Interceptor to check auth (JWT) token
class AuthInterceptor(grpc.ServerInterceptor):
    PUBLIC_METHODS = {
        "/AuthService/Login",
        "/AuthService/CheckUserExists",
        "/AuthService/GetSalt",
    }

    def __init__(self):
        def abort(ignored_request, context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid token")

        self._abort_handler = grpc.unary_unary_rpc_method_handler(abort)

    def intercept_service(self, continuation, handler_call_details):
        # Example HandlerCallDetails object:
        #     _HandlerCallDetails(
        #       method=u'/helloworld.Greeter/SayHello',
        #       invocation_metadata=...)

        # Continue if a public method was called
        if handler_call_details.method in self.PUBLIC_METHODS:
            return continuation(handler_call_details)
        metadata = dict(handler_call_details.invocation_metadata)
        auth_header = metadata.get("authorization")
        
        
        if not auth_header or not auth_header.startswith("Bearer "):
            def deny(_, context):
                context.abort(grpc.StatusCode.UNAUTHENTICATED, "Missing or invalid authorization header")
            return grpc.unary_unary_rpc_method_handler(deny)

        token = auth_header[len("Bearer "):]

        if token in REVOKED_TOKENS:
            return grpc.unary_unary_rpc_method_handler(
                lambda _, ctx: ctx.abort(grpc.StatusCode.UNAUTHENTICATED, "Token revoked")
            )
        try:
            payload = verify_jwt(token)
            # optionally add user info to context
        except jwt.PyJWTError as e:
            def deny(_, context):
                context.abort(grpc.StatusCode.UNAUTHENTICATED, f"Token verification failed:")
            return grpc.unary_unary_rpc_method_handler(deny)

        return continuation(handler_call_details)

# Service for login, creating accounts ect
class AuthService(auth_pb2_grpc.AuthService):
    # Check if the user exists
    def CheckUserExists(self, request, context):
        cur.execute("SELECT 1 FROM users WHERE username = %s;", (request.username,))
        exists = cur.fetchone() is not None
        return auth_pb2.user_exists_response(exists=exists)

    # Get the salt for the user from the db and send to client so client can hash password
    def GetSalt(self, request, context):
        # Declare variable in case user doesn't exists.
        salt = b''
        cur.execute("SELECT salt FROM users WHERE username = %s;", (request.username,))
        rows = cur.fetchone()
        if rows != None:
            salt = db_binary_to_binary(rows)

        return auth_pb2.password_salt(salt=salt)
    # Login function
    def Login(self, request, context):
        print("Logging in")
        try:
            # Attempt to get password hash from db
            cur.execute("SELECT password_hash FROM users where username = %s", (request.username,))
            password_hash_raw = cur.fetchall()
            password_hash = db_binary_to_binary(password_hash_raw)
        except:
            # If hash can't be found
            print("Password not found")
            password_hash = b''
        # Compare password hashes
        if (password_hash == request.password):
            result = True
            token = create_jwt(request.username)
            return auth_pb2.login_result(success=result, token=token)
        context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid credentials")

    def CreateAccount(self, request, context):
        print("Creating user")
        # Check user doesn't exist
        cur.execute("SELECT 1 FROM users WHERE username = %s;", (request.username,))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)", (request.username, request.password, request.salt))
            conn.commit()
            print("Done")
            return auth_pb2.register_result(success=True)
        else:
            return auth_pb2.register_result(success=False)

    def DeletetUser(self, request, context):
        print("Deleting user")
        # Check user exists
        cur.execute("SELECT 1 FROM users WHERE username = %s;", (request.username,))
        if cur.fetchone() is None:
            cur.execute("DELETE FROM users WHERE username = %s", (request.username,))
            conn.commit()
            print("Done")
            return auth_pb2.delete_result(success=True)
        else:
            print("User doesn't exist")
            return auth_pb2.delete_result(success=False)

    def Logout(self, request, context):
        print("Logging out")
        try:
            payload = verify_jwt(request.token)
            REVOKED_TOKENS.add(request.token)
            return auth_pb2.LogoutResponse(status="Logged out")
        except jwt.PyJWTError:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid token")
    




@contextlib.contextmanager
def run_server(port):
    # Bind interceptor to server
    server = grpc.server(
        futures.ThreadPoolExecutor(),
        interceptors=(AuthInterceptor(),),
    )
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)

    # Loading credentials
    server_credentials = grpc.ssl_server_credentials(
        (
            (
                _credentials.SERVER_CERTIFICATE_KEY,
                _credentials.SERVER_CERTIFICATE,
            ),
        )
    )

    # Pass down credentials
    port = server.add_secure_port(
        _LISTEN_ADDRESS_TEMPLATE % port, server_credentials
    )

    server.start()
    try:
        yield server, port
    finally:
        server.stop(0)


def serve():
    print("Starting server...")
    with run_server(50051) as (server, port):
        server.wait_for_termination()



if __name__ == "__main__":
    serve()

