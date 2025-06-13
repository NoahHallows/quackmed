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

class LoginService:
    def GetSalt(self, request, context):
        cur.execute("SELECT salt FROM users WHERE username = %s", (request.username,))
        row = cur.fetchone()
        if row is None:
            # Handle user not found
            return quackmed_pb2.password_salt(salt=b"")  # or raise an error

        salt = row[0]
        print(salt)
        return quackmed_pb2.password_salt(salt=salt)

    def Login(self, request, context):
        print("ADGGD")
        cur.execute("SELECT password_hash FROM users where username = %s", (request.username,))
        password_hash = cur.fetchone()
        password_hash = b'1010101010'
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

