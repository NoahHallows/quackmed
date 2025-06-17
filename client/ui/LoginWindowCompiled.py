# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(400, 300)
        self.formLayout = QFormLayout(Login)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.UsernameEdit = QLineEdit(Login)
        self.UsernameEdit.setObjectName(u"UsernameEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.UsernameEdit)

        self.label = QLabel(Login)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(5, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(6, QFormLayout.ItemRole.LabelRole, self.verticalSpacer)

        self.LoginButton = QPushButton(Login)
        self.LoginButton.setObjectName(u"LoginButton")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.LoginButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(4, QFormLayout.ItemRole.LabelRole, self.verticalSpacer_3)

        self.PasswordEdit = QLineEdit(Login)
        self.PasswordEdit.setObjectName(u"PasswordEdit")
        self.PasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.PasswordEdit)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Username", None))
        self.label.setText(QCoreApplication.translate("Login", u"Password", None))
        self.LoginButton.setText(QCoreApplication.translate("Login", u"Login", None))
    # retranslateUi

