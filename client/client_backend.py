import grpc
import quackmed_pb2
import quackmed_pb2_grpc
import bcrypt
import _credentials

# Auth token
TOKEN = b''
HOST = "localhost:50051"
_SERVER_ADDR_TEMPLATE = "localhost:%d"

class accounts:
    def __init__(self):
        # Call credential object will be invoked for every single RPC
        call_credentials = grpc.access_token_call_credentials(
            "example_oauth2_token"
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
        self.stub = quackmed_pb2_grpc.AuthServiceStub(self.channel)


    def login(self, username, password):
        print(f"{username}, {password}")
        response = self.stub.CheckUserExists(quackmed_pb2.user_exists_request(username=username))
        if True:
            response = self.stub.GetSalt(quackmed_pb2.salt_request(username=username))
            password_hash = bcrypt.hashpw(password.encode(), response.salt)
            response = self.stub.Login(quackmed_pb2.login_request(username=username, password=password_hash))
            global TOKEN
            TOKEN = response.token
            return response.success, response.token
        else:
            return False, b''

    def create_account(self, username, password):
        response = self.stub.CheckUserExists(quackmed_pb2.user_exists_request(username=username))
        if not response.exists:
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode(), salt)
            response = self.stub.CreateAccount(quackmed_pb2.register_request(username=username, password=password_hash, salt=salt))
            return response.success
        else:
            return False

    def delete_user(self, username):
        response = self.stub.DeleteUser(quackmed_pb2.delete_request(username=username))
        return response.success


if __name__ == "__main__":
    account_manager = accounts()
    username = input("Enter username: ")
    password = input("Enter password: ")
    option = input("Create account or login (1, 2): ")
    print(username)
    if option == "1":
        result = account_manager.create_account(username, password)
        print(f"Account creation result: {result}")
    elif option == "2":
        success, token = account_manager.login(username, password)
        print(f"Login result: {success}, Token: {token}")
    print("Done")

