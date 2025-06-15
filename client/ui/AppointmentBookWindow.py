# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appointmentBook.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AppointmentBook(object):
    def setupUi(self, AppointmentBook):
        if not AppointmentBook.objectName():
            AppointmentBook.setObjectName(u"AppointmentBook")
        AppointmentBook.resize(800, 600)
        self.mainLayout = QHBoxLayout(AppointmentBook)
        self.mainLayout.setObjectName(u"mainLayout")
        self.leftPanel = QVBoxLayout()
        self.leftPanel.setObjectName(u"leftPanel")
        self.calendarWidget = QCalendarWidget(AppointmentBook)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.leftPanel.addWidget(self.calendarWidget)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.addButton = QPushButton(AppointmentBook)
        self.addButton.setObjectName(u"addButton")

        self.buttonLayout.addWidget(self.addButton)

        self.editButton = QPushButton(AppointmentBook)
        self.editButton.setObjectName(u"editButton")

        self.buttonLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(AppointmentBook)
        self.deleteButton.setObjectName(u"deleteButton")

        self.buttonLayout.addWidget(self.deleteButton)


        self.leftPanel.addLayout(self.buttonLayout)


        self.mainLayout.addLayout(self.leftPanel)

        self.rightPanel = QVBoxLayout()
        self.rightPanel.setObjectName(u"rightPanel")
        self.appointmentTable = QTableWidget(AppointmentBook)
        if (self.appointmentTable.columnCount() < 2):
            self.appointmentTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.appointmentTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.appointmentTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.appointmentTable.setObjectName(u"appointmentTable")

        self.rightPanel.addWidget(self.appointmentTable)

        self.formGroupBox = QGroupBox(AppointmentBook)
        self.formGroupBox.setObjectName(u"formGroupBox")
        self.formLayout = QVBoxLayout(self.formGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.titleLabel = QLabel(self.formGroupBox)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.addWidget(self.titleLabel)

        self.titleInput = QLineEdit(self.formGroupBox)
        self.titleInput.setObjectName(u"titleInput")

        self.formLayout.addWidget(self.titleInput)

        self.timeLabel = QLabel(self.formGroupBox)
        self.timeLabel.setObjectName(u"timeLabel")

        self.formLayout.addWidget(self.timeLabel)

        self.timeInput = QLineEdit(self.formGroupBox)
        self.timeInput.setObjectName(u"timeInput")

        self.formLayout.addWidget(self.timeInput)

        self.notesLabel = QLabel(self.formGroupBox)
        self.notesLabel.setObjectName(u"notesLabel")

        self.formLayout.addWidget(self.notesLabel)

        self.notesInput = QTextEdit(self.formGroupBox)
        self.notesInput.setObjectName(u"notesInput")

        self.formLayout.addWidget(self.notesInput)

        self.saveButton = QPushButton(self.formGroupBox)
        self.saveButton.setObjectName(u"saveButton")

        self.formLayout.addWidget(self.saveButton)


        self.rightPanel.addWidget(self.formGroupBox)


        self.mainLayout.addLayout(self.rightPanel)


        self.retranslateUi(AppointmentBook)

        QMetaObject.connectSlotsByName(AppointmentBook)
    # setupUi

    def retranslateUi(self, AppointmentBook):
        AppointmentBook.setWindowTitle(QCoreApplication.translate("AppointmentBook", u"Appointment Book", None))
        self.addButton.setText(QCoreApplication.translate("AppointmentBook", u"Add", None))
        self.editButton.setText(QCoreApplication.translate("AppointmentBook", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("AppointmentBook", u"Delete", None))
        ___qtablewidgetitem = self.appointmentTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AppointmentBook", u"Time", None));
        ___qtablewidgetitem1 = self.appointmentTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AppointmentBook", u"Title", None));
        self.formGroupBox.setTitle(QCoreApplication.translate("AppointmentBook", u"Appointment Details", None))
        self.titleLabel.setText(QCoreApplication.translate("AppointmentBook", u"Title:", None))
        self.timeLabel.setText(QCoreApplication.translate("AppointmentBook", u"Time:", None))
        self.notesLabel.setText(QCoreApplication.translate("AppointmentBook", u"Notes:", None))
        self.saveButton.setText(QCoreApplication.translate("AppointmentBook", u"Save", None))
    # retranslateUi

