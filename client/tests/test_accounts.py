import unittest
import random
import string
from backend.auth import accounts



class TestCreateAccount(unittest.TestCase):
    def setUp(self):
        self.account_manager = accounts()
        self.account_manager.login('noah', 'amicia')
    
    def test_create_account_doctor(self):
        length = random.randint(1, 50)
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
         
        # Doctor type
        user_type = 1
        # Test account creation
        result = self.account_manager.create_account(username, password, user_type)
        self.assertTrue(result)
        
        # Test login with created account
        login_success, msg = self.account_manager.login(username, password)
        self.assertTrue(login_success)
        
        # Clean up - delete the test account
        delete_result = self.account_manager.delete_user(username)
        self.assertTrue(delete_result)

    def test_create_account_nurse(self):
        length = random.randint(1, 50)
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
         
        # Nurse type
        user_type = 2
        # Test account creation
        result = self.account_manager.create_account(username, password, user_type)
        self.assertTrue(result)
        
        # Test login with created account
        login_success, msg = self.account_manager.login(username, password)
        self.assertTrue(login_success)
        
        # Clean up - delete the test account
        delete_result = self.account_manager.delete_user(username)
        self.assertTrue(delete_result)

    def test_create_account_admin(self):
        length = random.randint(1, 50)
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
         
        # Admin type
        user_type = 3
        # Test account creation
        result = self.account_manager.create_account(username, password, user_type)
        self.assertTrue(result)
        
        # Test login with created account
        login_success, msg = self.account_manager.login(username, password)
        self.assertTrue(login_success)
        
        # Clean up - delete the test account
        delete_result = self.account_manager.delete_user(username)
        self.assertTrue(delete_result)

    def test_create_account_receptionist(self):
        length = random.randint(1, 50)
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
         
        # Receptionist type
        user_type = 4
        # Test account creation
        result = self.account_manager.create_account(username, password, user_type)
        self.assertTrue(result)
        
        # Test login with created account
        login_success  = self.account_manager.login(username, password)
        self.assertTrue(login_success)
        
        # Clean up - delete the test account
        delete_result = self.account_manager.delete_user(username)
        self.assertTrue(delete_result)

class TestLogin(unittest.TestCase):
    # Don't worry about the success variable because its just for the ui
    def setUp(self):
        self.account_manager = accounts()
    
    def test_correct_login(self):
        username = 'noah'
        password = 'amicia'
        success, msg = self.account_manager.login(username, password)
        self.assertTrue(success)

    def test_non_existent_user(self):
        username = 'The_Doctor_' + ''.join(random.choices(string.ascii_letters, k=10))  # Make it unique
        password = 'gdongdog'
        success, msg = self.account_manager.login(username, password)
        self.assertFalse(success)

    def test_incorrect_password(self):
        username = 'noah'
        password = 'wrongpassword'
        success, mgs = self.account_manager.login(username, password)
        self.assertFalse(success)

    def test_empty_username_and_password(self):
        username = ''
        password = ''
        success, msg = self.account_manager.login(username, password)
        self.assertFalse(success)

    def test_wrong_types(self):
        username = {}
        password = {}
        success, msg = self.account_manager.login(username, password)
        self.assertFalse(success)

class TestDeleteAccount(unittest.TestCase):
    def setUp(self):
        self.account_manager = accounts()
        self.account_manager.login('noah', 'amicia')
    
    def test_delete_existing_account(self):
        # First create a test account
        username = 'test_delete_' + ''.join(random.choices(string.ascii_letters, k=10))
        password = 'testpassword'
        user_type = random.randint(1, 4)
        create_result = self.account_manager.create_account(username, password, user_type)
        self.assertTrue(create_result)
        
        # Then delete it
        delete_result = self.account_manager.delete_user(username)
        self.assertTrue(delete_result)
        
        # Verify it's deleted by trying to login
        login_success, msg = self.account_manager.login(username, password)
        self.assertFalse(login_success)

class TestListUsers(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.account_manager = accounts()
        self.account_manager.login('noah', 'amicia')
        for i in range(1, 5):
            for n in range(1, 6):
                username = 'test_user_list_' + str(i) + str(n)
                password = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
                self.account_manager.create_account(username, password, i)
    
    @classmethod
    def tearDownClass(self):
        for i in range(1, 5):
            for n in range(1, 6):
                username = 'test_user_list_' + str(i) + str(n)
                self.account_manager.delete_user(username)

    def test_list_all_users(self):
        user_dict = {}
        response = self.account_manager.list_users(0)
        for user in response.users:
            user_dict[user.username] = user.user_type
        for i in range(1, 5):
            for n in range(1, 6):
                username = 'test_user_list_' + str(i) + str(n)
                self.assertIsNotNone(user_dict.get(username))
                self.assertEqual(user_dict[username], i)

    def test_list_doctors(self):
        user_dict = {}
        response = self.account_manager.list_users(1)
        for user in response.users:
            user_dict[user.username] = user.user_type

        for n in range(1, 6):
            username = "test_user_list_" + str(1) + str(n)
            self.assertIsNotNone(user_dict.get(username))
            self.assertEqual(user_dict[username], 1)

    def test_list_nurses(self):
        user_dict = {}
        response = self.account_manager.list_users(2)
        for user in response.users:
            user_dict[user.username] = user.user_type

        for n in range(1, 6):
            username = "test_user_list_" + str(2) + str(n)
            self.assertIsNotNone(user_dict.get(username))
            self.assertEqual(user_dict[username], 2)

    def test_list_admin(self):
        user_dict = {}
        response = self.account_manager.list_users(3)
        for user in response.users:
            user_dict[user.username] = user.user_type

        for n in range(1, 6):
            username = "test_user_list_" + str(3) + str(n)
            self.assertIsNotNone(user_dict.get(username))
            self.assertEqual(user_dict[username], 3)

    def test_list_receptionist(self):
        user_dict = {}
        response = self.account_manager.list_users(4)
        for user in response.users:
            user_dict[user.username] = user.user_type

        for n in range(1, 6):
            username = "test_user_list_" + str(4) + str(n)
            self.assertIsNotNone(user_dict.get(username))
            self.assertEqual(user_dict[username], 4)

    class TestGetUserDetails(unittest.TestCase):
        def setUp(self):
            self.account_manager = accounts()
            self.account_manager.login("noah", "amicia")
        
        def test_get_user_1(self):
            username = "test_get_user_details_" + ''.join(random.choices(string.ascii_letters, k=5))
            res = self.account_manager.create_account(username, "afsafsa", 2)
            self.assertTrue(res)
            res = self.account_manager.get_user_details(username)
            self.assertEqual(res, 2)

            # Then delete it
            delete_result = self.account_manager.delete_user(username)
            self.assertTrue(delete_result)


if __name__ == '__main__':
    unittest.main()

