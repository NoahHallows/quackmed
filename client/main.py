import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

# Import compilled layout
from MainWindow import Ui_MainWindow
from LoginWindow import Ui_Login

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


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Quackmed")
        self.CreateUserButton.clicked.connect(self.createUser)
        self.DeleteUserButton.clicked.connect(self.deleteUser)

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
