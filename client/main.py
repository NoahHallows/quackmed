import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QTableWidgetItem
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

# Import compilled layout
from ui.MainWindow import Ui_MainWindow
from ui.LoginWindow import Ui_Login
from ui.AppointmentBookWindow import Ui_AppointmentBook
from ui.UserListWindow import Ui_Users

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
        success, token = backend.login(username, password)
        if success == True:
            self.w = MainWindow()
            self.w.show()
            self.hide()
        else:
             LoginErrorMessageBox = QMessageBox(self)
             LoginErrorMessageBox.setWindowTitle("Incorrect username or password")
             LoginErrorMessageBox.setText("Please try again")


class UserListWindow(QWidget, Ui_Users):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CloseButton.clicked.connect(self.close_window)
        self.UserTypeSelector.currentIndexChanged.connect(self.populateTable)
   
    @QtCore.Slot()
    def close_window(self):
        self.close()
    
    @QtCore.Slot()
    def populateTable(self):
        user_type = self.UserTypeSelector.currentIndex()
        row = 0
        role = "Undefined"
        response = backend.list_users(user_type)
        self.UserTable.clearContents()
        self.UserTable.setRowCount(len(response.users))
        for user in response.users:
            if user.user_type == 1:
                role = "Doctor"
            elif user.user_type == 2:
                role = "Nurse"
            elif user.user_type == 3:
                role = "Admin"
            elif user.user_type == 4:
                role = "Receptionist"
            self.UserTable.setItem(row, 0, QTableWidgetItem(role))
            self.UserTable.setItem(row, 1, QTableWidgetItem(user.username))
            row = row + 1


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
        self.ListUsersButton.clicked.connect(self.list_users)


    @QtCore.Slot()
    def list_users(self):
        self.ListUsersWindow = UserListWindow()
        self.ListUsersWindow.show()
        self.ListUsersWindow.populateTable()

    @QtCore.Slot()
    def showAppointmentBook(self):
        self.AppointmentWindowObject = AppointmentWindow()
        self.AppointmentWindowObject.show()

    @QtCore.Slot()
    def deleteUser(self):
        username = self.UserEdit.text()
        backend.delete_user(username)
        print("Deleted user")

    @QtCore.Slot()
    def createUser(self):
        username = self.UserEdit.text()
        password = self.PasswordEdit.text()
        #user_type = self.UserTypeInput.value()
        #backend.create_account(username, password, user_type)
        print("Created user")

if __name__ == "__main__":
    backend = client_backend.accounts()
    app = QtWidgets.QApplication(sys.argv)
    
    window = LoginWindow()
    window.show()
    app.exec()
