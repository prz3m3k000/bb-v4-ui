from PyQt6.QtWidgets import QWidget, QHBoxLayout

from domain.app import App
from infra.inbound_messages import BotTelemetryMsg
from infra.udp_inbound_commands import UdpInboundCommands
from ui.forms_panel import FormsPanel
from ui.graphs_panel import GraphsPanel


class MainWindow(QWidget):

    def __init__(self, app: App):
        super().__init__()
        self.setMinimumSize(1200, 800)
        self._create_widgets(app)
        self._create_layout()
        self._connect_signals()

    def _create_widgets(self, app: App):
        self.forms_panel = FormsPanel(app)
        self.forms_panel.setFixedWidth(300)
        self.graphs_panel = GraphsPanel()
        self.udp_inbound_commands = UdpInboundCommands(8888)

    def _create_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.forms_panel)
        layout.addWidget(self.graphs_panel)
        self.setLayout(layout)

    def _connect_signals(self):
        self.udp_inbound_commands.on_bot_telemetry_ready.connect(self.graphs_panel.handle_bot_telemetry)
