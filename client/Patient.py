from ui.PatientDetails import Ui_PatientDetails
from ui.PatientListCompiled import Ui_PatientList
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QDialogButtonBox
from datetime import datetime

class DetailsWindow(QWidget, Ui_PatientDetails):
    def __init__(self, patient_backend):
        super().__init__()
        self.setupUi(self)
        self.backend = patient_backend
        self.DialogButtons.button(QDialogButtonBox.Apply).clicked.connect(self.create_patient)
        self.DialogButtons.rejected.connect(self.CloseWindow)

    @QtCore.Slot()
    def create_patient(self):
        first_name = self.FirstNameEdit.text()
        last_name = self.LastNameEdit.text()
        dob_datetime = self.DoBEdit.date().toPython() 
        notes = self.NotesEdit.toMarkdown()
        dob = dob_datetime.strftime("%d-%m-%Y")

        print(f"First_name: {first_name} of type {type(first_name)}, last_name: {last_name}, date of birth: {dob} of type {type(dob)}, notes: {notes}")
        res = self.backend.create_patient(first_name, last_name, notes, dob)
        print(res)

    def show_patient_details(patient_id):
        pass

    @QtCore.Slot()
    def CloseWindow(self):
        self.close()

class ListWindow(QWidget, Ui_PatientList):
    def __init__(self, patient_backend):
        super().__init__()
        self.setupUi(self)
        self.backend = patient_backend
        self.CloseButton.clicked.connect(self.CloseWindow)
        self.NewPatientButton.clicked.connect(self.create_patient)
        self.EditPatientButton.clicked.connect(self.show_patient_details)
        self.PatientTable.cellDoubleClicked.connect(self.show_patient_details)
        self.populate_table(self)

    @QtCore.Slot()
    def show_patient_details(self):
        pass

    @QtCore.Slot()
    def create_patient(self):
        pass

    @QtCore.Slot()
    def populate_table(self):
        first_name = '*'
        last_name = "*"
        response = self.backend.get_patient_list(first_name, last_name)
        for patient in response:
            print(patient)
            print(patient.first_name)

    @QtCore.Slot()
    def CloseWindow(self):
        self.close()
