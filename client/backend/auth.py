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
            # Connection is shaired between all modules
            self.conn = GRPCConnectionManager()
            self.stub = self.conn.get_stub(auth_pb2_grpc.AuthServiceStub)

    def login(self, username, password):
        # Input checks
        if username == '' or password == '':
            return False, "Username or password Empty"
        try:
            username = str(username)
            password = str(password)
        except:
            return False, "Username and password must be strings"

        # Ask server is user exists
        response = self.stub.CheckUserExists(auth_pb2.user_exists_request(username=username))
        if response.exists:
            # Get the salt from the server and hash
            response = self.stub.GetSalt(auth_pb2.salt_request(username=username))
            password_hash = bcrypt.hashpw(password.encode(), response.salt)
            response = self.stub.Login(auth_pb2.login_request(username=username, password=password_hash))
            if response.success:
                # Get this connection to use the authentication token and return true
                self.conn.set_token(response.token)
                self.stub = self.conn.get_stub(auth_pb2_grpc.AuthServiceStub)
                return response.success, ""
            else:
                # Hashed password failed checks on server
                return response.success, "Incorrect username or password"
        else:
            return False, "User doesn't exist"

    def create_account(self, username, password, user_type):
        # Input checks
        if username == '' or password == '':
            return False
        
        try:
            username = str(username)
            password = str(password)

        # Check user exists, if user does then fail
        response = self.stub.CheckUserExists(auth_pb2.user_exists_request(username=username))
        if not response.exists:
            # Hash password and generate salt, username, hashed password and salt are then sent to the server to be stored in the db
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode(), salt)
            response = self.stub.CreateAccount(auth_pb2.register_request(username=username, password=password_hash, salt=salt, user_type=user_type))
            return response.success
        else:
            return False

    def delete_user(self, username):
        # Input checks
        if username == '':
            return False
        try:
            username = str(username)
        except:
            return False
        #Check user exists
        user_exists_response = self.stub.CheckUserExists(auth_pb2.user_exists_request(username=username))
        if user_exists_response.exists:
            # This line tells the server to delete the user
            response = self.stub.DeleteUser(auth_pb2.delete_request(username=username))
            return response.success
        else:
            return False

    def logout(self):
        response = self.stub.Logout(auth_pb2.logout_request(token=TOKEN))
        self.conn.set_token("unauthorised")
        self.stub = self.conn.get_stub(auth_pb2_grpc.AuthServiceStub)
    def list_users(self, user_type):
        # TODO: use strings instead of ints for user type
        response = self.stub.ListUsers(auth_pb2.list_users_request(user_type=user_type))
        return response
