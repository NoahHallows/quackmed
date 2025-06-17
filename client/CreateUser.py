from ui.CreateUserCompiled import Ui_CreateUser
from PySide6 import QtCore
from PySide6.QtWidgets import QMessageBox, QWidget, QDialogButtonBox

class Window(QWidget, Ui_CreateUser):
    def __init__(self, auth_backend):
        super().__init__()
        self.setupUi(self)
        self.auth_backend = auth_backend
        self.DialogButton.button(QDialogButtonBox.Apply).clicked.connect(self.CreateUser)
        self.DialogButton.rejected.connect(self.CloseWindow)

    @QtCore.Slot()
    def CreateUser(self):
        print("Creating user")
        username = self.UserEdit.text()
        password = self.PasswordEdit.text()
        user_type = self.UserTypeSelector.currentIndex() + 1
        password_confirm = self.PasswordConfirmEdit.text()
        if password == password_confirm:
            result = self.auth_backend.create_account(username, password, user_type)
            print(result)
            if result == False:
                msgBox = QMessageBox()
                msgBox.setText("An error has occured")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.exec()
            else:
                msgBox = QMessageBox()
                msgBox.setText("User created")
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.exec()
                self.close()


        else:
            msgBox = QMessageBox()
            msgBox.setText("Password doesn't match")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.exec()
    
    @QtCore.Slot()
    def CloseWindow(self):
        self.close()

