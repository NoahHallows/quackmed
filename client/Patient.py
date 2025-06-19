from ui.PatientDetails import Ui_PatientDetails
from ui.PatientListCompiled import Ui_PatientList
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QDialogButtonBox, QTableWidgetItem, QMessageBox
from datetime import datetime

class DetailsWindow(QWidget, Ui_PatientDetails):
    update_table = QtCore.Signal()
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
        self.update_table.emit()
        

    def show_patient_details(self, patient_id):
        res = self.backend.get_patient_details(patient_id) 
        self.FirstNameEdit.setText(res.first_name)
        self.LastNameEdit.setText(res.last_name)
        self.NotesEdit.setText(res.notes)

    @QtCore.Slot()
    def CloseWindow(self):
        self.close()

class ListWindow(QWidget, Ui_PatientList):
    def __init__(self, patient_backend):
        super().__init__()
        self.setupUi(self)
        self.backend = patient_backend
        self.patient_ids = []
        self.CloseButton.clicked.connect(self.CloseWindow)
        self.NewPatientButton.clicked.connect(self.create_patient)
        self.EditPatientButton.clicked.connect(self.show_patient_details)
        self.PatientTable.cellDoubleClicked.connect(self.show_patient_details)
        # Connect the signal to refresh the table when patient is updated
        self.populate_table()

    @QtCore.Slot()
    def show_patient_details(self):
        try:
            current_row = self.PatientTable.currentRow()
            
        except Exception as e:
            QMessageBox.warning(self, "Unable to edit user", f"Please select a user from the table\n{e}")
            return
        self.CreateUserWindow = CreateUser.Window(auth_backend)
        self.CreateUserWindow.EditUser(self.patient_ids[current_row])
        self.CreateUserWindow.show() 

    @QtCore.Slot()
    def create_patient(self):
        self.details_window = DetailsWindow(self.backend)
        self.details_window.update_table.connect(self.populate_table)
        self.details_window.show()

    def populate_table(self):
        print("Populating table")
        first_name = '*'
        last_name = '*'
        row = 0
        response = self.backend.get_patient_list(first_name, last_name)
        self.PatientTable.clearContents()
        self.PatientTable.setRowCount(len(response.patients))
        for patient in response.patients:
            self.patient_ids.append(patient.patient_id)
            self.PatientTable.setItem(row, 0, QTableWidgetItem(patient.first_name))
            self.PatientTable.setItem(row, 1, QTableWidgetItem(patient.last_name))
            self.PatientTable.setItem(row, 2, QTableWidgetItem(patient.dob))
            row = row + 1

    @QtCore.Slot()
    def CloseWindow(self):
        self.close()
