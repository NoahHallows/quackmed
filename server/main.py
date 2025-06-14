from concurrent import futures

import grpc
import psycopg2
import bcrypt
import secrets
import _credentials
import contextlib

import quackmed_pb2
import quackmed_pb2_grpc

USERNAME = "noah"
PASSWORD = "amicia"
HOST = "127.0.0.1"


_LISTEN_ADDRESS_TEMPLATE = "localhost:%d"
_AUTH_HEADER_KEY = "authorization"
_AUTH_HEADER_VALUE = "Bearer example_oauth2_token"


# Authenticated TOKENS
TOKENS = {}

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

def db_binary_to_binary(db_binary):
    binary = b''
    for collumn in db_binary:
        for byte in collumn:
            binary = binary + byte
    return binary


class AuthInterceptor(grpc.ServerInterceptor):
    def __init__(self):
        def abort(ignored_request, context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid signature")

        self._abort_handler = grpc.unary_unary_rpc_method_handler(abort)

    def intercept_service(self, continuation, handler_call_details):
        # Example HandlerCallDetails object:
        #     _HandlerCallDetails(
        #       method=u'/helloworld.Greeter/SayHello',
        #       invocation_metadata=...)
        expected_metadata = (_AUTH_HEADER_KEY, _AUTH_HEADER_VALUE)
        if expected_metadata in handler_call_details.invocation_metadata:
            return continuation(handler_call_details)
        else:
            return self._abort_handler


class AuthService(quackmed_pb2_grpc.AuthService):
    def CheckUserExists(self, request, context):
        cur.execute("SELECT 1 FROM users WHERE username = %s;", (request.username,))
        exists = cur.fetchone() is not None
        return quackmed_pb2.user_exists_response(exists=exists)


    def GetSalt(self, request, context):
        salt = b''
        cur.execute("SELECT salt FROM users WHERE username = %s;", (request.username,))
        rows = cur.fetchone()
        if rows != None:
            salt = db_binary_to_binary(rows)

        print(salt)
        return quackmed_pb2.password_salt(salt=salt)

    def Login(self, request, context):
        print(f"Username: {request.username}, password: {request.password}")
        try:
            cur.execute("SELECT password_hash FROM users where username = %s", (request.username,))
            password_hash_raw = cur.fetchall()
            password_hash = db_binary_to_binary(password_hash_raw)
        except:
            print("Password not found")
            password_hash = b''
        print(f"Username: {request.username}, password_hash: {password_hash}, sent password hash: {request.password}")
        if (password_hash == request.password):
            result = True
            token = secrets.token_bytes(4)
            TOKENS[request.username] = token
            print(token)

        else:
            result = False
            token = b''
        return quackmed_pb2.login_result(success=result, token=token)

    def CreateAccount(self, request, context):
        print("Creating user")
        cur.execute("SELECT 1 FROM users WHERE username = %s;", (request.username,))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)", (request.username, request.password, request.salt))
            conn.commit()
            token = secrets.token_bytes(4)
            TOKENS[request.username] = token
            print("Done")
            return quackmed_pb2.register_result(success=True, token=token)
        else:
            return quackmed_pb2.register_result(success=False, token=token)

    def DeletetUser(self, request, context):
        print("Deleting user")
        cur.execute("SELECT 1 FROM users WHERE username = %s;", (request.username,))
        if cur.fetchone() is None:
            cur.execute("DELETE FROM users WHERE username = %s", (request.username,))
            conn.commit()
            print("Done")
            return quackmed_pb2.delete_result(success=True)
        else:
            print("User doesn't exist")
            return quackmed_pb2.delete_result(success=False)

    def Logout(self, request, context):
        print("Logging out")
        if request.username in TOKENS:
            TOKENS.pop(request.username)
            return quackmed_pb2.logout_result(success=True)
        else:
            return quackmed_pb2.logout_result(success=False)
    


class AppointmentService(quackmed_pb2_grpc.appointmentService):
    def GetAppointmentBook(self, request, context):
        pass

    def UpdateAppointmentBook(self, request, context):
        pass


@contextlib.contextmanager
def run_server(port):
    # Bind interceptor to server
    server = grpc.server(
        futures.ThreadPoolExecutor(),
        interceptors=(AuthInterceptor(),),
    )
    quackmed_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)

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

