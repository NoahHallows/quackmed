import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem
)
from PySide6.QtCore import QDate
from ui.AppointmentBookWindow import Ui_AppointmentBook


class AppointmentBookBackend(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AppointmentBook()
        self.ui.setupUi(self)

        # Store appointments in-memory: {QDate: [ {title, time, notes}, ... ]}
        self.appointments = {}

        # Signal connections
        self.ui.calendarWidget.selectionChanged.connect(self.update_table)
        self.ui.addButton.clicked.connect(self.add_appointment)
        self.ui.editButton.clicked.connect(self.edit_appointment)
        self.ui.deleteButton.clicked.connect(self.delete_appointment)
        self.ui.saveButton.clicked.connect(self.save_appointment)
        self.ui.appointmentTable.cellClicked.connect(self.load_selected_to_form)

        # Initial load
        self.update_table()

        # For edit tracking
        self.editing_index = None

    def get_selected_date(self):
        return self.ui.calendarWidget.selectedDate()

    def update_table(self):
        date = self.get_selected_date()
        items = self.appointments.get(date, [])

        self.ui.appointmentTable.setRowCount(len(items))
        for row, appt in enumerate(items):
            self.ui.appointmentTable.setItem(row, 0, QTableWidgetItem(appt["time"]))
            self.ui.appointmentTable.setItem(row, 1, QTableWidgetItem(appt["title"]))

        self.clear_form()
        self.editing_index = None

    def add_appointment(self):
        self.clear_form()
        self.editing_index = None

    def save_appointment(self):
        date = self.get_selected_date()
        title = self.ui.titleInput.text()
        time = self.ui.timeInput.text()
        notes = self.ui.notesInput.toPlainText()

        if not title or not time:
            QMessageBox.warning(self, "Missing Info", "Title and Time are required.")
            return

        new_appt = {"title": title, "time": time, "notes": notes}

        if date not in self.appointments:
            self.appointments[date] = []

        if self.editing_index is not None:
            # Edit existing
            self.appointments[date][self.editing_index] = new_appt
        else:
            # Add new
            self.appointments[date].append(new_appt)

        self.update_table()

    def delete_appointment(self):
        date = self.get_selected_date()
        row = self.ui.appointmentTable.currentRow()

        if row == -1:
            QMessageBox.warning(self, "No Selection", "Select an appointment to delete.")
            return

        del self.appointments[date][row]
        self.update_table()

    def edit_appointment(self):
        row = self.ui.appointmentTable.currentRow()
        if row == -1:
            QMessageBox.warning(self, "No Selection", "Select an appointment to edit.")
            return

        self.load_selected_to_form(row)

    def load_selected_to_form(self, row):
        date = self.get_selected_date()
        if date not in self.appointments or row >= len(self.appointments[date]):
            return

        appt = self.appointments[date][row]
        self.ui.titleInput.setText(appt["title"])
        self.ui.timeInput.setText(appt["time"])
        self.ui.notesInput.setPlainText(appt["notes"])
        self.editing_index = row

    def clear_form(self):
        self.ui.titleInput.clear()
        self.ui.timeInput.clear()
        self.ui.notesInput.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppointmentBookBackend()
    window.show()
    sys.exit(app.exec())

