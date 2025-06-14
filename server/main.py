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

class LoginService:
    def GetSalt(self, request, context):
        cur.execute("SELECT salt FROM users WHERE username = %s;", (request.username,))
        rows = cur.fetchall()
        #if rows is None:
            # Handle user not found
        #    return quackmed_pb2.password_salt(salt=b"")  # or raise an error

        salt = db_binary_to_binary(rows[0])
        print(salt)
        return quackmed_pb2.password_salt(salt=salt)

    def Login(self, request, context):
        print("ADGGD")
        print(f"request: {request.username}, password: {request.password}")
        cur.execute("SELECT password_hash FROM users where username = %s", (request.username,))
        password_hash_raw = cur.fetchone()
        password_hash = db_binary_to_binary(password_hash_raw[0])
        print(f"Username: {request.username}, password_hash: {password_hash}, sent password hash: {request.password}")
        print(type(password_hash))
        print(type(request.password))
        result = bcrypt.checkpw(password_hash, request.password)
        print(result)
        token = secrets.token_bytes(4)
        return quackmed_pb2.login_result(success=True, token=token)

    def CreateAccount(self, request, context):
        print("Creating user")
        cur.execute("INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)", (request.username, request.password, request.salt))
        conn.commit()
        token = secrets.token_bytes(4)
        print("Done")
        return quackmed_pb2.register_result(success=True, token=token)



class AppointmentService(quackmed_pb2_grpc.appointmentService):
    def GetAppointmentBook(self, request, context):
        pass

    def UpdateAppointmentBook(self, request, context):
        pass


def serve():
    print("Starting server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quackmed_pb2_grpc.add_LoginServiceServicer_to_server(LoginService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
    


if __name__ == "__main__":
    serve()

