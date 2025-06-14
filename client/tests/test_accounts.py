import unittest
import random
import string
from client_backend import accounts

class TestCreateAccount(unittest.TestCase):
    def setUp(self):
        self.account_manager = accounts()
    
    def test_create_account1(self):
        length = random.randint(1, 50)
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        
        # Test account creation
        result = self.account_manager.create_account(username, password)
        self.assertTrue(result)
        
        # Test login with created account
        login_success, token = self.account_manager.login(username, password)
        self.assertTrue(login_success)
        self.assertIsInstance(token, bytes)
        
        # Clean up - delete the test account
        delete_result = self.account_manager.delete_user(username)
        self.assertTrue(delete_result)

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.account_manager = accounts()
    
    def test_correct_login(self):
        username = 'noah'
        password = 'amicia'
        success, token = self.account_manager.login(username, password)
        self.assertTrue(success)
        self.assertIsInstance(token, bytes)

    def test_non_existent_user(self):
        username = 'The_Doctor_' + ''.join(random.choices(string.ascii_letters, k=10))  # Make it unique
        password = 'gdongdog'
        success, token = self.account_manager.login(username, password)
        self.assertFalse(success)
        self.assertEqual(token, b'')

    def test_incorrect_password(self):
        username = 'noah'
        password = 'wrongpassword'
        success, token = self.account_manager.login(username, password)
        self.assertFalse(success)
        self.assertEqual(token, b'')

class TestDeleteAccount(unittest.TestCase):
    def setUp(self):
        self.account_manager = accounts()
    
    def test_delete_existing_account(self):
        # First create a test account
        username = 'test_delete_' + ''.join(random.choices(string.ascii_letters, k=10))
        password = 'testpassword'
        
        create_result = self.account_manager.create_account(username, password)
        self.assertTrue(create_result)
        
        # Then delete it
        delete_result = self.account_manager.delete_user(username)
        self.assertTrue(delete_result)
        
        # Verify it's deleted by trying to login
        login_success, token = self.account_manager.login(username, password)
        self.assertFalse(login_success)

if __name__ == '__main__':
    unittest.main()

