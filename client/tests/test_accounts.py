import unittest
import random
import string
from client_backend import accounts

def login_test_func(username, password):
    res = accounts.login(self, username, password)
    token = res[1]
    if isinstance(token, bytes) and res[0] == True:
        return True
    else:
        return False

def create_account_test_func(username, password):
    res = accounts.create_account(self, username, password)
    token = res[1]
    if isinstance(token, bytes) and res[0] == True:
        if login_test_func(self, username, password):
            return delete_account_test_func(username)
    else:
        return False

def delete_account_test_func(username):
    return accounts.delete_user(self, username)[0]
     

class TestCreateAccount(unittest.TestCase):
    def test_create_account1(self):
        length = random.randint(1, 50)
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        self.assertTrue(create_account_test_func(username, password))

class TestLogin(unittest.TestCase):
    def test_correct(self):
        username = 'noah'
        password = 'amicia'
        self.assertTrue(login_test_func(username, password))

    def test_non_existent_user_and_passwd(self):
        username = 'The Doctor'
        password = 'gdongdog'
        self.assertFalse(login_test_func(username, password))

    def test_incorrect_passwd(self):
        username = 'noah'
        password = 'wornggggg'
        self.assertFalse(login_test_func(username, password))


