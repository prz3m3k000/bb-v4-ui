import pyqtgraph as pg
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from ui.plots.circular_buffer import CircularBuffer


class LoopIntervalPlot(QWidget):
    def __init__(self, sample_rate: int = 100, buffer_seconds: int = 5):
        super().__init__()

        self.interval_data = CircularBuffer(sample_rate * buffer_seconds)
        self._create_widgets()
        self._create_layout()

    def _create_widgets(self):
        self.plot = pg.PlotWidget()
        self.plot.addLegend()
        self.plot.setYRange(-0.01, 0.01)
        self.interval_curve = self.plot.plot(pen='r', name='loop interval')

    def _create_layout(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.plot.setFixedHeight(100)
        layout.addWidget(self.plot)

    def _connect_signals(self):
        pass

    def add_sample(self, interval: float):
        self.interval_data.add_value(interval)

    def update_plot(self):
        self.interval_curve.setData(self.interval_data.get_data())
