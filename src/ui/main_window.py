from PyQt6.QtWidgets import QWidget, QHBoxLayout

from domain.app import App
from ui.forms_panel import FormsPanel
from ui.graphs_panel import GraphsPanel


class MainWindow(QWidget):

    def __init__(self, app: App):
        super().__init__()
        self.setMinimumSize(1200, 800)
        self._create_widgets(app)
        self._create_layout()

    def _create_widgets(self, app: App):
        self.forms_panel = FormsPanel(app)
        self.forms_panel.setFixedWidth(300)

        self.graphs_panel = GraphsPanel()

    def _create_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.forms_panel)
        layout.addWidget(self.graphs_panel)
        self.setLayout(layout)
