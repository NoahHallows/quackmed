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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.CreateUserButton = QPushButton(self.centralwidget)
        self.CreateUserButton.setObjectName(u"CreateUserButton")

        self.gridLayout.addWidget(self.CreateUserButton, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.LogoutButton = QPushButton(self.centralwidget)
        self.LogoutButton.setObjectName(u"LogoutButton")

        self.gridLayout.addWidget(self.LogoutButton, 1, 4, 1, 1)

        self.DeleteUserButton = QPushButton(self.centralwidget)
        self.DeleteUserButton.setObjectName(u"DeleteUserButton")

        self.gridLayout.addWidget(self.DeleteUserButton, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 5, 1, 1)

        self.ListUsersButton = QPushButton(self.centralwidget)
        self.ListUsersButton.setObjectName(u"ListUsersButton")

        self.gridLayout.addWidget(self.ListUsersButton, 1, 1, 1, 1)

        self.AppointmentButton = QPushButton(self.centralwidget)
        self.AppointmentButton.setObjectName(u"AppointmentButton")

        self.gridLayout.addWidget(self.AppointmentButton, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.ListPatientsButton = QPushButton(self.centralwidget)
        self.ListPatientsButton.setObjectName(u"ListPatientsButton")

        self.gridLayout.addWidget(self.ListPatientsButton, 2, 4, 1, 1)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Quackmed", None))
        self.CreateUserButton.setText(QCoreApplication.translate("MainWindow", u"Create user", None))
        self.LogoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.DeleteUserButton.setText(QCoreApplication.translate("MainWindow", u"Delete user", None))
        self.ListUsersButton.setText(QCoreApplication.translate("MainWindow", u"List Users", None))
        self.AppointmentButton.setText(QCoreApplication.translate("MainWindow", u"Appointment Book", None))
        self.ListPatientsButton.setText(QCoreApplication.translate("MainWindow", u"List Patients", None))
    # retranslateUi

