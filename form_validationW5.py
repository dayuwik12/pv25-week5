import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

class FormValidation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Validation F1D022050 Ida Ayu Dewi Purnama Anjani")
        self.init_ui()

    def init_ui(self):
        # Input & Label Definitions
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()

        self.phone_label = QLabel("Phone Number:")
        self.phone_input = QLineEdit()
        self.phone_input.setInputMask("+62 999 9999 9999")

        self.address_label = QLabel("Address:")
        self.address_input = QTextEdit()
        self.address_input.setFixedHeight(60)

        self.gender_label = QLabel("Gender:")
        self.gender_input = QComboBox()
        self.gender_input.addItems(["", "Male", "Female"])

        self.education_label = QLabel("Education:")
        self.education_input = QComboBox()
        self.education_input.addItems(["", "Elementary School", "Junior High School", "Senior High School", "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral Degree"])

        self.save_button = QPushButton("Save")
        self.clear_button = QPushButton("Clear")

        self.save_button.clicked.connect(self.validate_form)
        self.clear_button.clicked.connect(self.clear_fields)

        # Shortcut to close
        close_shortcut = QShortcut(QKeySequence("Q"), self)
        close_shortcut.activated.connect(self.close)

        # Atur lebar input fields
        self.set_input_widths(300)

        # Atur tombol
        self.save_button.setFixedWidth(100)
        self.clear_button.setFixedWidth(100)

        # Main Layout
        layout = QVBoxLayout()
        layout.addLayout(self.create_form_row(self.name_label, self.name_input))
        layout.addLayout(self.create_form_row(self.email_label, self.email_input))
        layout.addLayout(self.create_form_row(self.age_label, self.age_input))
        layout.addLayout(self.create_form_row(self.phone_label, self.phone_input))
        layout.addLayout(self.create_form_row(self.address_label, self.address_input))
        layout.addLayout(self.create_form_row(self.gender_label, self.gender_input))
        layout.addLayout(self.create_form_row(self.education_label, self.education_input))
        
        # Tambahan layout styling
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(12)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)


    def set_input_widths(self, width):
        widgets = [
            self.name_input, self.email_input, self.age_input, self.phone_input,
            self.address_input, self.gender_input, self.education_input
        ]
        for widget in widgets:
            widget.setFixedWidth(width)

        self.address_input.setFixedSize(width, 150)

    def create_form_row(self, label, widget):
        layout = QHBoxLayout()
        label.setFixedWidth(120)
        layout.addWidget(label)
        layout.addWidget(widget)
        return layout

    def validate_form(self):
        name = self.name_input.text()
        email = self.email_input.text()
        age = self.age_input.text()
        phone = self.phone_input.text()
        address = self.address_input.toPlainText()
        gender = self.gender_input.currentText()
        education = self.education_input.currentText()

        # Validation
        if not all([name, email, age, phone.strip().replace("+62", "").replace(" ", "").isdigit(), address.strip(), gender, education]):
            self.show_message("All fields are required.")
            return
        if not name.strip():
            self.show_message("Name is required.")
            return
        if any(char.isdigit() for char in name):
            self.show_message("Name should not contain numbers.")
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_message("Invalid email format.")
            return
        if not age.isdigit():
            self.show_message("Age must be numeric.")
            return
        if int(age) < 17:
            self.show_message("Age must be at least 17 years old.")
            return
        if '_' in phone:
            if len(phone.replace("+62", "").replace(" ", "")) != 11:
                self.show_message("Phone number must be 13 digits.")
            return
        if not address.strip():
            self.show_message("Address is required.")
            return
        if gender == "":
            self.show_message("Please select a gender.")
            return
        if education == "":
            self.show_message("Please select an education level.")
            return

        self.show_message("Data saved successfully!", QMessageBox.Information)
        self.clear_fields()

    def show_message(self, message, icon=QMessageBox.Warning):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setText(message)
        msg_box.exec_()

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()
        self.gender_input.setCurrentIndex(0)
        self.education_input.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormValidation()
    window.resize(650, 500)
    window.show()
    sys.exit(app.exec_())
