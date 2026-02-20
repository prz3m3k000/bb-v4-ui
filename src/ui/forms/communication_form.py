import socket
from dataclasses import dataclass

from PyQt6.QtCore import QRegularExpression, pyqtSignal
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QFormLayout, QLineEdit, QLabel, QGroupBox, QPushButton


class CommunicationForm(QGroupBox):
    DEFAULT_BOT_HOSTNAME = "balancing-bot.local"

    submitted = pyqtSignal(object)

    def __init__(self):
        super().__init__("Communication settings")
        self._create_widgets()
        self._create_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.bot_hostname = QLineEdit()
        self.bot_hostname.setText(self.DEFAULT_BOT_HOSTNAME)
        self.find_bots_ip_button = QPushButton("Find bot's IP")
        self.bot_ip = QIpEdit()
        self.apply_button = QPushButton("Apply")
        pass

    def _create_layout(self):
        layout = QFormLayout()
        layout.addRow(QLabel("Bot's hostname"), self.bot_hostname)
        layout.addRow(self.find_bots_ip_button)
        layout.addRow(QLabel("Bot's IP address"), self.bot_ip)
        layout.addRow(self.apply_button)
        self.setLayout(layout)

    def _connect_signals(self):
        self.find_bots_ip_button.clicked.connect(self._find_bots_ip)
        self.apply_button.clicked.connect(self._submit_form)

    def _find_bots_ip(self):
        hostname = self.bot_hostname.text()
        try:
            ip = socket.gethostbyname(hostname)
            self.bot_ip.setText(ip)
        except socket.gaierror:
            self.bot_ip.setText(None)

    def _submit_form(self):
        data = CommunicationFormData(dashboard_ip='', dashboard_port=8888, bot_ip=self.bot_ip.text(), bot_port=0)
        self.submitted.emit(data)


class QIpEdit(QLineEdit):

    def __init__(self):
        super().__init__()
        self.setPlaceholderText("xxx.xxx.xxx.xxx")
        self.setValidator(self._ip_validator())

    @staticmethod
    def _ip_validator():
        ipv4_regex = QRegularExpression(
            r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
            r"(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"
        )
        return QRegularExpressionValidator(ipv4_regex)


@dataclass(frozen=True)
class CommunicationFormData:
    dashboard_ip: str
    dashboard_port: int
    bot_ip: str
    bot_port: int
