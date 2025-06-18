from ui.PatientDetails import Ui_PatientDetails
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


    def CloseWindow(self):
        self.close()
