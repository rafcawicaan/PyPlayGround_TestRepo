import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

# This is your main window class
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")  # Sets the window title
        self.setGeometry(100, 100, 300, 150)  # (x, y, width, height)

        # Create labels and input boxes
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # Hides password input

        # Create login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)  # Run function when clicked

        # Put everything in a vertical layout (top to bottom)
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        # Set the layout on the main window
        self.setLayout(layout)

    def check_login(self):
        # Grab what the user typed
        username = self.username_input.text()
        password = self.password_input.text()

        # You can change this to check a database or file
        if username == "admin" and password == "password123":
            QMessageBox.information(self, "Success", "You are logged in!")
            # You can now open your main app window or do something else
        else:
            QMessageBox.warning(self, "Error", "Wrong username or password.")

# Start the app
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Starts the app
    window = LoginWindow()  # Makes a login window
    window.show()  # Shows the login window
    sys.exit(app.exec_())  # Runs the app loop
