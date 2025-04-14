import sys
import psycopg2
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QLabel,
    QVBoxLayout, QMessageBox
)
from Sample import SampleWindow


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setGeometry(400, 200, 300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("New Username")

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("New Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton("Register", self)
        self.register_button.clicked.connect(self.register_user)

        layout.addWidget(QLabel("New Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("New Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Please enter both username and password.")
            return

        try:
            conn = psycopg2.connect(
                database="sample_db",
                user="postgres",
                password="admin",
                host="localhost"
            )
            cur = conn.cursor()

            # Check if username already exists
            cur.execute("SELECT * FROM pyqt_schema.users WHERE username=%s", (username,))
            if cur.fetchone():
                QMessageBox.warning(self, "Error", "Username already exists.")
                conn.close()
                return

            cur.execute("INSERT INTO pyqt_schema.users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success", "Registration successful! You can now login.")
            self.close()

        except psycopg2.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(400, 200, 300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.check_login)

        self.register_button = QPushButton("Register", self)
        self.register_button.clicked.connect(self.open_register_window)

        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        try:
            conn = psycopg2.connect(
                database="sample_db",
                user="postgres",
                password="admin",
                host="localhost"
            )
            cur = conn.cursor()
            cur.execute("SELECT * FROM pyqt_schema.users WHERE username=%s AND password=%s", (username, password))
            result = cur.fetchone()
            conn.close()

            if result:
                QMessageBox.information(self, "Login Success", f"Welcome {username}!")
                self.open_main_app()
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

        except psycopg2.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error connecting to database:\n{e}")

    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()

    def open_main_app(self):
        self.sample_window = SampleWindow()
        self.sample_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())
