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
    QLineEdit, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_PatientList(object):
    def setupUi(self, PatientList):
        if not PatientList.objectName():
            PatientList.setObjectName(u"PatientList")
        PatientList.resize(400, 300)
        self.tableWidget = QTableWidget(PatientList)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(9, 57, 371, 231))
        self.widget = QWidget(PatientList)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 9, 175, 24))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.retranslateUi(PatientList)

        QMetaObject.connectSlotsByName(PatientList)
    # setupUi

    def retranslateUi(self, PatientList):
        PatientList.setWindowTitle(QCoreApplication.translate("PatientList", u"Form", None))
        self.label.setText(QCoreApplication.translate("PatientList", u"Search", None))
    # retranslateUi

