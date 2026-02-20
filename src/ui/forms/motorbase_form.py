from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QFormLayout, QPushButton, QGroupBox


class MotorbaseForm(QGroupBox):

    motorbase_enabled = pyqtSignal(bool)

    def __init__(self):
        super().__init__("Motor base")

        self.disable_motorbase_button =  QPushButton("Disable motor base")
        self.disable_motorbase_button.clicked.connect(lambda: self.motorbase_enabled.emit(False))

        self.enable_motorbase_button =  QPushButton("Enable motor base")
        self.enable_motorbase_button.clicked.connect(lambda: self.motorbase_enabled.emit(True))

        layout = QFormLayout()
        self.setLayout(layout)
        layout.addWidget(self.disable_motorbase_button)
        layout.addWidget(self.enable_motorbase_button)