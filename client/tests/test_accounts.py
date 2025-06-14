import unittest
import random
import string
from client_backend import login, create_account

def login_test_func(username, password):
    res = login(username, password)
    token = res.token
    print(type(token))
    print(res.success)
    if isinstance(token, bytes) and res.success == True:
        return True
    else:
        return False

def create_account_test_func(username, password):
    res = create_account(username, password)
    token = res.token
    if type(token) == 'bytes' and success == True:
        return login_test_func(username, password)
    else:
        return False

#class TestCreateAccount(unittest.TestCase):
#    def test_create_account1(self):
#        length = random.randint(1, 50)
#        username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
#        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
#        self.assertTrue(create_account_test_func(username, password))

class TestLogin(unittest.TestCase):
    def test_correct(self):
        username = 'noah'
        password = 'amicia'
        self.assertTrue(login_test_func(username, password))

    def test_non_existent_user_and_passwd(self):
        username = 'The Doctor'
        password = 'gdongdog'
        self.assertTrue(login_test_func(username, password))

    def test_incorrect_passwd(self):
        username = 'noah'
        password = 'wornggggg'
        self.assertFalse(login_test_func(username, password))


