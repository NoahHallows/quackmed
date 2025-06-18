# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createUser.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_CreateUser(object):
    def setupUi(self, CreateUser):
        if not CreateUser.objectName():
            CreateUser.setObjectName(u"CreateUser")
        CreateUser.resize(400, 300)
        self.formLayout = QFormLayout(CreateUser)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(CreateUser)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.UserEdit = QLineEdit(CreateUser)
        self.UserEdit.setObjectName(u"UserEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.UserEdit)

        self.label_2 = QLabel(CreateUser)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.PasswordEdit = QLineEdit(CreateUser)
        self.PasswordEdit.setObjectName(u"PasswordEdit")
        self.PasswordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.PasswordEdit)

        self.label_3 = QLabel(CreateUser)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.UserTypeSelector = QComboBox(CreateUser)
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.setObjectName(u"UserTypeSelector")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.UserTypeSelector)

        self.DialogButton = QDialogButtonBox(CreateUser)
        self.DialogButton.setObjectName(u"DialogButton")
        self.DialogButton.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel)
        self.DialogButton.setCenterButtons(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.DialogButton)

        self.TitleLable = QLabel(CreateUser)
        self.TitleLable.setObjectName(u"TitleLable")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.TitleLable)

        self.PasswordConfirmEdit = QLineEdit(CreateUser)
        self.PasswordConfirmEdit.setObjectName(u"PasswordConfirmEdit")
        self.PasswordConfirmEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.PasswordConfirmEdit)

        self.label_5 = QLabel(CreateUser)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_5)


        self.retranslateUi(CreateUser)

        QMetaObject.connectSlotsByName(CreateUser)
    # setupUi

    def retranslateUi(self, CreateUser):
        CreateUser.setWindowTitle(QCoreApplication.translate("CreateUser", u"Create User", None))
        self.label.setText(QCoreApplication.translate("CreateUser", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("CreateUser", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("CreateUser", u"User type", None))
        self.UserTypeSelector.setItemText(0, QCoreApplication.translate("CreateUser", u"Doctor", None))
        self.UserTypeSelector.setItemText(1, QCoreApplication.translate("CreateUser", u"Nurse", None))
        self.UserTypeSelector.setItemText(2, QCoreApplication.translate("CreateUser", u"Admin", None))
        self.UserTypeSelector.setItemText(3, QCoreApplication.translate("CreateUser", u"Recepionist", None))

        self.TitleLable.setText(QCoreApplication.translate("CreateUser", u"Create user", None))
        self.label_5.setText(QCoreApplication.translate("CreateUser", u"Confirm\n"
"password", None))
    # retranslateUi

