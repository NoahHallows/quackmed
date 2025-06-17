import grpc
from backend.grpc import auth_pb2
from backend.grpc import auth_pb2_grpc
from backend.connectionManager import GRPCConnectionManager
import bcrypt

# Auth token
TOKEN = ''
HOST = "localhost:50051"

class accounts:
    def __init__(self):
            self.conn = GRPCConnectionManager()
            self.stub = self.conn.get_stub(auth_pb2_grpc.AuthServiceStub)

    def login(self, username, password):
        response = self.stub.CheckUserExists(auth_pb2.user_exists_request(username=username))
        if response.exists:
            response = self.stub.GetSalt(auth_pb2.salt_request(username=username))
            password_hash = bcrypt.hashpw(password.encode(), response.salt)
            response = self.stub.Login(auth_pb2.login_request(username=username, password=password_hash))
            if response.success:
                self.conn.set_token(response.token)
                self.stub = self.conn.get_stub(auth_pb2_grpc.AuthServiceStub)
            return response.success
        else:
            return False

    def create_account(self, username, password, user_type):
        response = self.stub.CheckUserExists(auth_pb2.user_exists_request(username=username))
        if not response.exists:
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode(), salt)
            response = self.stub.CreateAccount(auth_pb2.register_request(username=username, password=password_hash, salt=salt, user_type=user_type))
            return response.success
        else:
            return False

    def delete_user(self, username):
        response = self.stub.DeleteUser(auth_pb2.delete_request(username=username))
        return response.success

    def logout(self):
        response = self.stub.Logout(auth_pb2.logout_request(token=TOKEN))
        self.conn.set_token("unauthorised")
        self.stub = self.conn.get_stub(auth_pb2_grpc.AuthServiceStub)
    def list_users(self, user_type):
        response = self.stub.ListUsers(auth_pb2.list_users_request(user_type=user_type))
        return response
