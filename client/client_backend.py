import grpc
import quackmed_pb2
import quackmed_pb2_grpc
import bcrypt

def login(username, password):
    print(f"{username}, {password}")
    channel = grpc.insecure_channel("localhost:50051")
    stub = quackmed_pb2_grpc.LoginServiceStub(channel)
    print("DAGDGADG")
    response = stub.GetSalt(quackmed_pb2.salt_request(username=username))
    password_hash = bcrypt.hashpw(password.encode(), response.salt)
    print(type(password_hash))
    print(type(username))
    response = stub.Login(quackmed_pb2.login_request(username=username, password=password_hash))
    return response

def create_account(username, password):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode(), salt)
    channel = grpc.insecure_channel("localhost:50051")
    stub = quackmed_pb2_grpc.LoginServiceStub(channel)
    response = stub.CreateAccount(quackmed_pb2.register_request(username=username, password=password_hash, salt=salt))
    return response

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    option = input("Create account or login (1, 2)")
    if option == "1":
        create_account(username, password)
    if option == "2":
        login(username, password)
    print("Done")
