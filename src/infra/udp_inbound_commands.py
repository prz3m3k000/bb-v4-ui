from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtNetwork import QUdpSocket, QHostAddress

from infra.inbound_messages import BotTelemetryMsg


class UdpInboundCommands(QObject):

    CMD_BOT_TELEMETRY = 1

    on_bot_telemetry_ready = pyqtSignal(BotTelemetryMsg)

    def __init__(self, port: int = 8888):
        super().__init__()
        self._create_widgets(port)
        self._connect_signals()

    def _create_widgets(self, port: int):
        self.socket = QUdpSocket(self)
        self.socket.bind(QHostAddress.SpecialAddress.Any, port)

    def _connect_signals(self):
        self.socket.readyRead.connect(self._on_datagram_ready)

    def _on_datagram_ready(self):
        while self.socket.hasPendingDatagrams():
            data, host, port = self.socket.readDatagram(self.socket.pendingDatagramSize())

            command_id = data[0]
            if command_id == self.CMD_BOT_TELEMETRY:
                self._handle_bot_telemetry(data)

    def _handle_bot_telemetry(self, data: bytes):
        self.on_bot_telemetry_ready.emit(BotTelemetryMsg.from_bytes(data))
