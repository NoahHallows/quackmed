import unittest
import random
import string
from client_backend import login, create_account

def login_test_func(username, password):
    res = login(username, password)
    token = res.token
    if type(token) == 'bytes' and success == True:
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
    def test_login1(self):
        username = 'noah'
        password = 'amicia'
        self.assertTrue(login_test_func(username, password))

#    def test_login2(self):
#        username = 'The Doctor'
#        password = 'gdongdog'
#        self.assertTrue(login_test_func(username, password))


