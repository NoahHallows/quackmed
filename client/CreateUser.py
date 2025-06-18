from ui.CreateUserCompiled import Ui_CreateUser
from PySide6 import QtCore
from PySide6.QtWidgets import QMessageBox, QWidget, QDialogButtonBox

class Window(QWidget, Ui_CreateUser):
    def __init__(self, auth_backend):
        super().__init__()
        self.setupUi(self)
        self.auth_backend = auth_backend
        self.create_user = True
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
                if self.create_user:
                    msgBox.setText("User created")
                else:
                    msgBox.setText("User modified")
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.exec()
                self.close()

        else:
            msgBox = QMessageBox()
            msgBox.setText("Password doesn't match")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.exec()

    def EditUser(self, username):
        self.create_user = False
        self.UserEdit.setText(username)
        self.PasswordEdit.clear()
        self.PasswordEdit.setPlaceholderText("Please enter new password")
        self.PasswordConfirmEdit.clear()
        self.PasswordConfirmEdit.setPlaceholderText("Please confirm new password")
        self.TitleLable.setText("Edit user")
        user_type = self.auth_backend.get_user_details(username)
        user_type = user_type - 1
        print(user_type)
        self.UserTypeSelector.setCurrentIndex(user_type)
    
    @QtCore.Slot()
    def CloseWindow(self):
        self.close()

