import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QTableWidgetItem
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

# Import compilled layout
from ui.MainWindow import Ui_MainWindow
from ui.LoginWindow import Ui_Login
from ui.AppointmentBookWindow import Ui_AppointmentBook

# Import backend
import client_backend

class LoginWindow(QWidget, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.LoginButton.clicked.connect(self.Login)
    
    @QtCore.Slot()
    def Login(self):
        username = self.UsernameEdit.text()
        password = self.PasswordEdit.text()
        print(f"Username: {username}, password: {password}")
        success, token = backend.login(username, password)
        print(token)
        self.w = MainWindow()
        self.w.show()


class AppointmentWindow(QWidget, Ui_AppointmentBook):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.setWindowTitle("Appointment Book")

        # Store appointments in-memory: {QDate: [ {title, time, notes}, ... ]}
        self.appointments = {}

        # Signal connections
        self.calendarWidget.selectionChanged.connect(self.update_table)
        self.addButton.clicked.connect(self.add_appointment)
        self.editButton.clicked.connect(self.edit_appointment)
        self.deleteButton.clicked.connect(self.delete_appointment)
        self.saveButton.clicked.connect(self.save_appointment)
        self.appointmentTable.cellClicked.connect(self.load_selected_to_form)

        # Initial load
        self.update_table()

        # For edit tracking
        self.editing_index = None

    def get_selected_date(self):
        return self.calendarWidget.selectedDate()

    def update_table(self):
        date = self.get_selected_date()
        items = self.appointments.get(date, [])

        self.appointmentTable.setRowCount(len(items))
        for row, appt in enumerate(items):
            self.appointmentTable.setItem(row, 0, QTableWidgetItem(appt["time"]))
            self.appointmentTable.setItem(row, 1, QTableWidgetItem(appt["title"]))

        self.clear_form()
        self.editing_index = None

    def add_appointment(self):
        self.clear_form()
        self.editing_index = None

    def save_appointment(self):
        date = self.get_selected_date()
        title = self.titleInput.text()
        time = self.timeInput.text()
        notes = self.notesInput.toPlainText()

        if not title or not time:
            QMessageBox.warning(self, "Missing Info", "Title and Time are required.")
            return

        new_appt = {"title": title, "time": time, "notes": notes}

        if date not in self.appointments:
            self.appointments[date] = []

        if self.editing_index is not None:
            # Edit existing
            self.appointments[date][self.editing_index] = new_appt
        else:
            # Add new
            self.appointments[date].append(new_appt)

        self.update_table()

    def delete_appointment(self):
        date = self.get_selected_date()
        row = self.appointmentTable.currentRow()

        if row == -1:
            QMessageBox.warning(self, "No Selection", "Select an appointment to delete.")
            return

        del self.appointments[date][row]
        self.update_table()

    def edit_appointment(self):
        row = self.appointmentTable.currentRow()
        if row == -1:
            QMessageBox.warning(self, "No Selection", "Select an appointment to edit.")
            return

        self.load_selected_to_form(row)

    def load_selected_to_form(self, row):
        date = self.get_selected_date()
        if date not in self.appointments or row >= len(self.appointments[date]):
            return

        appt = self.appointments[date][row]
        self.titleInput.setText(appt["title"])
        self.timeInput.time()
        self.notesInput.setPlainText(appt["notes"])
        self.editing_index = row

    def clear_form(self):
        self.titleInput.clear()
        self.timeInput.clear()
        self.notesInput.clear()



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quackmed")
        self.CreateUserButton.clicked.connect(self.createUser)
        self.DeleteUserButton.clicked.connect(self.deleteUser)
        self.AppointmentButton.clicked.connect(self.showAppointmentBook)

    @QtCore.Slot()
    def showAppointmentBook(self):
        self.w = AppointmentWindow()
        self.w.show()

    @QtCore.Slot()
    def deleteUser(self):
        username = self.UserEdit.text()
        backend.delete_user(username)
        print("Deleted user")

    @QtCore.Slot()
    def createUser(self):
        username = self.UserEdit.text()
        password = self.PasswordEdit.text()
        backend.create_account(username, password)
        print("Created user")

if __name__ == "__main__":
    backend = client_backend.accounts()
    app = QtWidgets.QApplication(sys.argv)
    
    window = LoginWindow()
    window.show()
    app.exec()
