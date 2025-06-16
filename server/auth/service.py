import grpc
import psycopg2
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
from .jwt_auth import create_jwt, verify_jwt
# loading variables from .env file
load_dotenv() 

import auth_pb2
import auth_pb2_grpc

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]

# Connect to db
try:
    conn = psycopg2.connect(
        dbname="quackmed",
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host="127.0.0.1"
    )

    cur = conn.cursor()

except:
    print("Connection error")
    exit()

# Convert the list of bytes to a single variable
def db_binary_to_binary(db_binary):
    binary = b''
    for collumn in db_binary:
        for byte in collumn:
            binary = binary + byte
    return binary


# Service for login, creating accounts ect
class AuthService(auth_pb2_grpc.AuthService):
    # Check if the user exists
    def CheckUserExists(self, request, context):
        cur.execute("SELECT 1 FROM users WHERE username = %s;", (request.username,))
        exists = cur.fetchone() is not None
        return auth_pb2.user_exists_response(exists=exists)

    # Get the salt for the user from the db and send to client so client can hash password
    def GetSalt(self, request, context):
        # Declare variable in case user doesn't exists.
        salt = b''
        cur.execute("SELECT salt FROM users WHERE username = %s;", (request.username,))
        rows = cur.fetchone()
        if rows != None:
            salt = db_binary_to_binary(rows)

        return auth_pb2.password_salt(salt=salt)
    # Login function
    def Login(self, request, context):
        print("Logging in")
        try:
            # Attempt to get password hash from db
            cur.execute("SELECT password_hash FROM users where username = %s", (request.username,))
            password_hash_raw = cur.fetchall()
            password_hash = db_binary_to_binary(password_hash_raw)
        except:
            # If hash can't be found
            print("Password not found")
            password_hash = b''
        # Compare password hashes
        if (password_hash == request.password):
            cur.execute("SELECT type FROM users WHERE username = %s", (request.username,))
            user_type = cur.fetchone()[0]
            result = True
            token = create_jwt(request.username, user_type)
            return auth_pb2.login_result(success=result, token=token)
        return auth_pb2.login_result(success=False, token='')

    def CreateAccount(self, request, context):
        print("Creating user")
        # Check user doesn't exist
        cur.execute("SELECT 1 FROM users WHERE username = %s;", (request.username,))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO users (username, password_hash, salt, type) VALUES (%s, %s, %s, %s)", (request.username, request.password, request.salt, request.user_type))
            conn.commit()
            print("Done")
            return auth_pb2.register_result(success=True)
        else:
            return auth_pb2.register_result(success=False)

    def DeleteUser(self, request, context):
        print("Deleting user")
        # Check user exists
        cur.execute("SELECT 1 FROM users WHERE username = %s;", (request.username,))
        if cur.fetchone() != None:
            cur.execute("DELETE FROM users WHERE username = %s", (request.username,))
            conn.commit()
            print("Done")
            return auth_pb2.delete_result(success=True)
        else:
            print("User doesn't exist")
            return auth_pb2.delete_result(success=False)

    def Logout(self, request, context):
        print("Logging out")
        try:
            payload = verify_jwt(request.token)
            REVOKED_TOKENS.add(request.token)
            return auth_pb2.LogoutResponse(status="Logged out")
        except jwt.PyJWTError:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid token")

    def ListUsers(self, request, context):
        print("Listing users")
        if request.user_type != 0:
            cur.execute("SELECT username, type FROM users WHERE type = %s", (str(request.user_type)))
        else:
            cur.execute("SELECT username, type FROM users")
        rows = cur.fetchall()
        users = []
        for row in rows:
            users.append(auth_pb2.user_details(username=row[0], user_type=row[1]))
            print(row)

        return auth_pb2.list_user_response(users=users)
        


