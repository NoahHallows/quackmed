# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userList.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Users(object):
    def setupUi(self, Users):
        if not Users.objectName():
            Users.setObjectName(u"Users")
        Users.resize(578, 490)
        self.verticalLayout = QVBoxLayout(Users)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Users)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.UserTable = QTableWidget(Users)
        if (self.UserTable.columnCount() < 2):
            self.UserTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.UserTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.UserTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.UserTable.rowCount() < 9):
            self.UserTable.setRowCount(9)
        self.UserTable.setObjectName(u"UserTable")

        self.verticalLayout.addWidget(self.UserTable)

        self.label_2 = QLabel(Users)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.UserTypeSelector = QComboBox(Users)
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.addItem("")
        self.UserTypeSelector.setObjectName(u"UserTypeSelector")

        self.verticalLayout.addWidget(self.UserTypeSelector)

        self.CloseButton = QPushButton(Users)
        self.CloseButton.setObjectName(u"CloseButton")

        self.verticalLayout.addWidget(self.CloseButton)


        self.retranslateUi(Users)

        QMetaObject.connectSlotsByName(Users)
    # setupUi

    def retranslateUi(self, Users):
        Users.setWindowTitle(QCoreApplication.translate("Users", u"User list", None))
        self.label.setText(QCoreApplication.translate("Users", u"Users", None))
        ___qtablewidgetitem = self.UserTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Users", u"Role", None));
        ___qtablewidgetitem1 = self.UserTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Users", u"Name", None));
        self.label_2.setText(QCoreApplication.translate("Users", u"User role", None))
        self.UserTypeSelector.setItemText(0, QCoreApplication.translate("Users", u"All", None))
        self.UserTypeSelector.setItemText(1, QCoreApplication.translate("Users", u"Doctor", None))
        self.UserTypeSelector.setItemText(2, QCoreApplication.translate("Users", u"Nurse", None))
        self.UserTypeSelector.setItemText(3, QCoreApplication.translate("Users", u"Admin", None))
        self.UserTypeSelector.setItemText(4, QCoreApplication.translate("Users", u"Receptionist", None))

        self.CloseButton.setText(QCoreApplication.translate("Users", u"Close", None))
    # retranslateUi

