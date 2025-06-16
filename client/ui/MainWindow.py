# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.UserTypeSelector = QComboBox(self.centralwidget)
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.setObjectName(u"UserTypeSelector")

        self.gridLayout.addWidget(self.UserTypeSelector, 3, 3, 1, 1)

        self.ListUsersButton = QPushButton(self.centralwidget)
        self.ListUsersButton.setObjectName(u"ListUsersButton")

        self.gridLayout.addWidget(self.ListUsersButton, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.LogoutButton = QPushButton(self.centralwidget)
        self.LogoutButton.setObjectName(u"LogoutButton")

        self.gridLayout.addWidget(self.LogoutButton, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 5, 1, 1)

        self.PasswordEdit = QLineEdit(self.centralwidget)
        self.PasswordEdit.setObjectName(u"PasswordEdit")
        self.PasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.PasswordEdit, 2, 3, 1, 1)

        self.UserEdit = QLineEdit(self.centralwidget)
        self.UserEdit.setObjectName(u"UserEdit")

        self.gridLayout.addWidget(self.UserEdit, 1, 3, 1, 1)

        self.AppointmentButton = QPushButton(self.centralwidget)
        self.AppointmentButton.setObjectName(u"AppointmentButton")

        self.gridLayout.addWidget(self.AppointmentButton, 0, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.CreateUserButton = QPushButton(self.centralwidget)
        self.CreateUserButton.setObjectName(u"CreateUserButton")

        self.gridLayout.addWidget(self.CreateUserButton, 4, 1, 1, 1)

        self.DeleteUserButton = QPushButton(self.centralwidget)
        self.DeleteUserButton.setObjectName(u"DeleteUserButton")

        self.gridLayout.addWidget(self.DeleteUserButton, 4, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.UserTypeSelector.setItemText(0, QCoreApplication.translate("MainWindow", u"Doctor", None))
        self.UserTypeSelector.setItemText(1, QCoreApplication.translate("MainWindow", u"Nurse", None))
        self.UserTypeSelector.setItemText(2, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.UserTypeSelector.setItemText(3, QCoreApplication.translate("MainWindow", u"Receptionist", None))

        self.ListUsersButton.setText(QCoreApplication.translate("MainWindow", u"List Users", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.LogoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.AppointmentButton.setText(QCoreApplication.translate("MainWindow", u"Appointment Book", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"User type", None))
        self.CreateUserButton.setText(QCoreApplication.translate("MainWindow", u"Create user", None))
        self.DeleteUserButton.setText(QCoreApplication.translate("MainWindow", u"Delete user", None))
    # retranslateUi

