import psycopg2
from PyQt5.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem, QPushButton,
    QVBoxLayout, QWidget, QLineEdit, QLabel, QMessageBox
)


class SampleWindow(QMainWindow):  # Changed from ContactApp
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Contact Manager")
        self.setGeometry(390, 200, 600, 400)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Name")
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone")

        self.add_button = QPushButton("Add Contact", self)
        self.add_button.clicked.connect(self.add_contact)

        self.update_button = QPushButton("Update Contact", self)
        self.update_button.clicked.connect(self.update_contact)

        self.delete_button = QPushButton("Delete Contact", self)
        self.delete_button.clicked.connect(self.delete_contact)

        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Phone"])
        self.table.cellClicked.connect(self.load_selected_contact)

        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Phone:"))
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_contacts()

    def get_db_connection(self):
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="sample_db",
                user="postgres",
                password="admin"
            )
            return connection
        except psycopg2.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error connecting to database: {err}")

    def load_contacts(self):
        connection = self.get_db_connection()
        if not connection:
            return
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pyqt_schema.contacts")
        records = cursor.fetchall()
        connection.close()

        self.table.setRowCount(0)
        for contact in records:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            for column, data in enumerate(contact):
                self.table.setItem(row_position, column, QTableWidgetItem(str(data)))

    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()

        if not name or not phone:
            QMessageBox.warning(self, "Validation Error", "Both name and phone fields are required.")
            return

        connection = self.get_db_connection()
        if not connection:
            return
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO pyqt_schema.contacts (name, phone) VALUES (%s, %s)", (name, phone))
            connection.commit()
        except psycopg2.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error adding contact: {err}")
        finally:
            connection.close()

        self.load_contacts()
        self.name_input.clear()
        self.phone_input.clear()

    def update_contact(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Selection Error", "Please select a contact to update.")
            return

        contact_id = int(self.table.item(selected_row, 0).text())
        name = self.name_input.text()
        phone = self.phone_input.text()

        if not name or not phone:
            QMessageBox.warning(self, "Validation Error", "Both name and phone fields are required.")
            return

        connection = self.get_db_connection()
        if not connection:
            return
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE pyqt_schema.contacts SET name=%s, phone=%s WHERE con_id=%s",
                           (name, phone, contact_id))
            connection.commit()
        except psycopg2.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error updating contact: {err}")
        finally:
            connection.close()

        self.load_contacts()
        self.name_input.clear()
        self.phone_input.clear()

    def delete_contact(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Selection Error", "Please select a contact to delete.")
            return

        contact_id = int(self.table.item(selected_row, 0).text())

        connection = self.get_db_connection()
        if not connection:
            return
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM pyqt_schema.contacts WHERE con_id=%s", (contact_id,))
            connection.commit()
        except psycopg2.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error deleting contact: {err}")
        finally:
            connection.close()

        self.load_contacts()

    def load_selected_contact(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            self.name_input.setText(self.table.item(selected_row, 1).text())
            self.phone_input.setText(self.table.item(selected_row, 2).text())
