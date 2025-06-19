# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patientList.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PatientList(object):
    def setupUi(self, PatientList):
        if not PatientList.objectName():
            PatientList.setObjectName(u"PatientList")
        PatientList.resize(400, 360)
        self.verticalLayout = QVBoxLayout(PatientList)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(PatientList)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(PatientList)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.PatientTable = QTableWidget(PatientList)
        if (self.PatientTable.columnCount() < 3):
            self.PatientTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.PatientTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.PatientTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.PatientTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.PatientTable.setObjectName(u"PatientTable")

        self.verticalLayout.addWidget(self.PatientTable)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.NewPatientButton = QPushButton(PatientList)
        self.NewPatientButton.setObjectName(u"NewPatientButton")

        self.horizontalLayout_2.addWidget(self.NewPatientButton)

        self.EditPatientButton = QPushButton(PatientList)
        self.EditPatientButton.setObjectName(u"EditPatientButton")

        self.horizontalLayout_2.addWidget(self.EditPatientButton)

        self.CloseButton = QPushButton(PatientList)
        self.CloseButton.setObjectName(u"CloseButton")

        self.horizontalLayout_2.addWidget(self.CloseButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(PatientList)

        QMetaObject.connectSlotsByName(PatientList)
    # setupUi

    def retranslateUi(self, PatientList):
        PatientList.setWindowTitle(QCoreApplication.translate("PatientList", u"Patient list", None))
        self.label.setText(QCoreApplication.translate("PatientList", u"Search", None))
        ___qtablewidgetitem = self.PatientTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PatientList", u"First name", None));
        ___qtablewidgetitem1 = self.PatientTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PatientList", u"Last name", None));
        ___qtablewidgetitem2 = self.PatientTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PatientList", u"Date of birth", None));
        self.NewPatientButton.setText(QCoreApplication.translate("PatientList", u"New patient", None))
        self.EditPatientButton.setText(QCoreApplication.translate("PatientList", u"Edit patient", None))
        self.CloseButton.setText(QCoreApplication.translate("PatientList", u"Close", None))
    # retranslateUi

