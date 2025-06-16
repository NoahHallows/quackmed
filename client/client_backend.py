import grpc
import auth_pb2
import auth_pb2_grpc
import bcrypt
import _credentials

# Auth token
TOKEN = ''
HOST = "localhost:50051"

class accounts:
    def __init__(self):
           self.intialise_conn('unauthorised')

    def intialise_conn(self, token):
        # Call credential object will be invoked for every single RPC
        call_credentials = grpc.access_token_call_credentials(
            token
        )
        # Channel credential will be valid for the entire channel
        channel_credential = grpc.ssl_channel_credentials(
            _credentials.ROOT_CERTIFICATE
        )
        # Combining channel credentials and call credentials together
        composite_credentials = grpc.composite_channel_credentials(
            channel_credential,
            call_credentials,
        )
        self.channel = grpc.secure_channel(HOST, composite_credentials)
        self.stub = auth_pb2_grpc.AuthServiceStub(self.channel)


    def login(self, username, password):
        response = self.stub.CheckUserExists(auth_pb2.user_exists_request(username=username))
        if response.exists:
            response = self.stub.GetSalt(auth_pb2.salt_request(username=username))
            password_hash = bcrypt.hashpw(password.encode(), response.salt)
            response = self.stub.Login(auth_pb2.login_request(username=username, password=password_hash))
            self.intialise_conn(response.token)
            return response.success, response.token
        else:
            return False, b''

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
        self.intialise_conn('unauthorised')

    def list_users(self, user_type):
        response = self.stub.ListUsers(auth_pb2.list_users_request(user_type=user_type))
        for users in response.users:
            print(users.username)
        return response
        


if __name__ == "__main__":
    account_manager = accounts()
    username = input("Enter username: ")
    password = input("Enter password: ")
    option = input("Create account or login (1, 2): ")
    if option == "1":
        result = account_manager.create_account(username, password)
        print(f"Account creation result: {result}")
    elif option == "2":
        success, token = account_manager.login(username, password)
        print(f"Login result: {success}, Token: {token}")
    print("Done")

