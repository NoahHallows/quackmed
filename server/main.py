from concurrent import futures

import grpc
import psycopg2
import bcrypt
import secrets

import quackmed_pb2
import quackmed_pb2_grpc

USERNAME = "noah"
PASSWORD = "amicia"
HOST = "127.0.0.1"

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

# Server interceptor for token validation
class AuthInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        if handler_call_details.method == "/AuthService/Login":
            return continuation(handler_call_details)

        metadata = dict(handler_call_details.invocation_metadata)
        token = metadata.get("authorization")

        if token not in TOKENS.values():
            context = grpc.ServicerContext()
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid token")

        return continuation(handler_call_details)

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


def serve():
    print("Starting server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=(AuthInterceptor(),))
    quackmed_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
    


if __name__ == "__main__":
    serve()

