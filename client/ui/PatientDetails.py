# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PatientDetails.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QTextEdit, QWidget)

class Ui_PatientDetails(object):
    def setupUi(self, PatientDetails):
        if not PatientDetails.objectName():
            PatientDetails.setObjectName(u"PatientDetails")
        PatientDetails.resize(400, 300)
        self.formLayout = QFormLayout(PatientDetails)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(PatientDetails)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.FirstNameEdit = QLineEdit(PatientDetails)
        self.FirstNameEdit.setObjectName(u"FirstNameEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.FirstNameEdit)

        self.label_2 = QLabel(PatientDetails)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.LastNameEdit = QLineEdit(PatientDetails)
        self.LastNameEdit.setObjectName(u"LastNameEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.LastNameEdit)

        self.label_3 = QLabel(PatientDetails)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.DoBEdit = QDateEdit(PatientDetails)
        self.DoBEdit.setObjectName(u"DoBEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.DoBEdit)

        self.label_4 = QLabel(PatientDetails)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.NotesEdit = QTextEdit(PatientDetails)
        self.NotesEdit.setObjectName(u"NotesEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.NotesEdit)

        self.DialogButtons = QDialogButtonBox(PatientDetails)
        self.DialogButtons.setObjectName(u"DialogButtons")
        self.DialogButtons.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.DialogButtons)


        self.retranslateUi(PatientDetails)

        QMetaObject.connectSlotsByName(PatientDetails)
    # setupUi

    def retranslateUi(self, PatientDetails):
        PatientDetails.setWindowTitle(QCoreApplication.translate("PatientDetails", u"Patient details", None))
        self.label.setText(QCoreApplication.translate("PatientDetails", u"First name", None))
        self.label_2.setText(QCoreApplication.translate("PatientDetails", u"Last name", None))
        self.label_3.setText(QCoreApplication.translate("PatientDetails", u"Date of birth", None))
        self.label_4.setText(QCoreApplication.translate("PatientDetails", u"Notes", None))
    # retranslateUi

