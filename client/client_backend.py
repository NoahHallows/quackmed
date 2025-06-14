import grpc
import quackmed_pb2
import quackmed_pb2_grpc
import bcrypt

# Auth token
TOKEN = b''
HOST = "127.0.0.1:50051"

class accounts:
    def __init__(self):
        self.channel = grpc.insecure_channel(HOST)
        self.stub = quackmed_pb2_grpc.AuthServiceStub(self.channel)

    def login(self, username, password):
        print(f"{username}, {password}")
        response = self.stub.CheckUserExists(quackmed_pb2.user_exists_request(username=username))
        if response.exists:
            response = self.stub.GetSalt(quackmed_pb2.salt_request(username=username))
            password_hash = bcrypt.hashpw(password.encode(), response.salt)
            response = self.stub.Login(quackmed_pb2.login_request(username=username, password=password_hash))
            global TOKEN  # Fixed: need global keyword to modify module-level TOKEN
            TOKEN = response.token
            return response.success, response.token
        else:
            return False, b''

    def create_account(self, username, password):
        metadata = [("authorization", TOKEN)]
        response = self.stub.CheckUserExists(quackmed_pb2.user_exists_request(username=username), metadata=metadata)
        if not response.exists:
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode(), salt)
            response = self.stub.CreateAccount(quackmed_pb2.register_request(username=username, password=password_hash, salt=salt), metadata=metadata)
            return response.success
        else:
            return False

    def delete_user(self, username):
        metadata = [("authorization", TOKEN)]
        response = self.stub.DeleteUser(quackmed_pb2.delete_request(username=username), metadata=metadata)
        return response.success


if __name__ == "__main__":
    account_manager = accounts()  # Fixed: create instance
    username = input("Enter username: ")
    password = input("Enter password: ")
    option = input("Create account or login (1, 2): ")
    print(username)
    if option == "1":
        result = account_manager.create_account(username, password)  # Fixed: use instance
        print(f"Account creation result: {result}")
    elif option == "2":  # Fixed: use elif
        success, token = account_manager.login(username, password)  # Fixed: use instance
        print(f"Login result: {success}, Token: {token}")
    print("Done")

