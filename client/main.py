import sys
from PySide6.QtWidgets import QApplication
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

# Import compilled layout
from MainWindow import Ui_MainWindow

# Import backend
import client_backend

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hello World")
        self.LoginButton.clicked.connect(self.Login)
        self.backend = client_backend.accounts()
    
    @QtCore.Slot()
    def Login(self):
        username = self.UsernameEdit.text()
        password = self.PasswordEdit.text()
        print(f"Username: {username}, password: {password}")
        success, token = self.backend.login(username, password)
        print(token)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
