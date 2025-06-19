import unittest
import random
import string
from datetime import date, timedelta

from backend.auth import accounts
from backend.patient import PatientManager

def random_date():
        # initializing dates ranges 
    test_date1, test_date2 = date(2015, 6, 3), date(2015, 7, 1)
    # initializing K
    K = 7
    # getting days between dates
    dates_bet = test_date2 - test_date1
    total_days = dates_bet.days

    res = []
    for idx in range(K):
        random.seed(a=None)
        
        # getting random days
        randay = random.randrange(total_days)
        
        # getting random dates 
        res.append(test_date1 + timedelta(days=randay))

    return str(res)


class TestCreatePatient(unittest.TestCase):
    def setUp(self):
        self.account_manager = accounts()
        self.account_manager.login("noah", "amicia")
        self.patient_manager = PatientManager()

    def test_create_patient(self):
        firstname = "test_patient_firstname_" + ''.join(random.choices(string.ascii_letters, k=10))
        lastname = "test_patient_lastname_" + ''.join(random.choices(string.ascii_letters, k=10))
        notes = ''.join(random.choices(string.ascii_letters, k=20))
        dob = "01-01-2000"
        res, patient_id = self.patient_manager.create_patient(firstname, lastname, notes, dob)
        self.assertTrue(res)
        self.assertTrue(self.patient_manager.delete_patient(patient_id))

class TestPatientList(unittest.TestCase):
    def setUp(self):
        self.account_manager = accounts()
        self.account_manager.login("noah", "amicia")
        self.patient_manager = PatientManager()
        self.patient_ids = []
        for i in range(1, 25):
            firstname = "test_patient_firstname_" + str(i)
            lastname = "test_patient_lastname_" + str(i)
            notes = ''.join(random.choices(string.ascii_letters, k=50))
            dob = "01-01-2000"
            res, patient_id = self.patient_manager.create_patient(firstname, lastname, notes, dob)
            self.patient_ids.append(int(patient_id))

    def tearDown(self):
        for patient_id in self.patient_ids:
            res = self.patient_manager.delete_patient(patient_id)

    def test_list_all_patients(self):
        patients_res = self.patient_manager.get_patient_list("*", "*")
        i = 1
        for patient in patients_res.patients:
            self.assertEqual(patient.first_name, "test_patient_firstname_" + str(i))
            self.assertEqual(patient.lastname, "test_patient_lastname_" + str(i))
            i += 1

    def test_list_one_patient(self):
        i = random.randint(1,25)
        firstname = "test_patient_firstname_" + ''.join(str(i))
        lastname = "test_patient_lastname_" + ''.join(str(i))
        patient_res = self.patient_manager.get_patient_list(firstname, lastname)
        patient = patient_res.patients[0]
        self.assertEqual(patient.first_name, firstname)
        self.assertEqual(patient.last_name, lastname)
        self.assertTrue(isinstance(patient.patient_id, int))
        self.assertTrue(isinstance(patient.notes, str))

class TestPatientDetails(unittest.TestCase):
    def setUp(self):
        self.account_manager = accounts()
        self.account_manager.login("noah", "amicia")
        self.patient_manager = PatientManager()

    def test_patient_details(self):
        # Create patient
        firstname = "test_patient_firstname_" + ''.join(random.choices(string.ascii_letters, k=10))
        lastname = "test_patient_lastname_" + ''.join(random.choices(string.ascii_letters, k=10))
        notes = ''.join(random.choices(string.ascii_letters, k=1500))
        dob = "27-11-2006"
        res, patient_id = self.patient_manager.create_patient(firstname, lastname, notes, dob)
        self.assertTrue(res)
        # Access records
        patient = self.patient_manager.get_patient_details(patient_id)
        self.assertEqual(patient.first_name, firstname)
        self.assertEqual(patient.last_name, lastname)
        self.assertEqual(patient.notes, notes)
        self.assertEqual(patient.dob, dob)
        
        # Cleanup
        self.assertTrue(self.patient_manager.delete_patient(patient_id))
        
        
