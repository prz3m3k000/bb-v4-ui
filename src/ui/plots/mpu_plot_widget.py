import pyqtgraph as pg
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from ui.plots.circular_buffer import CircularBuffer


class MpuPlotWidget(QWidget):
    def __init__(self, sample_rate: int = 100, buffer_seconds: int = 5, ):
        super().__init__()

        buffer_size = sample_rate * buffer_seconds
        self.buffer_pitch = CircularBuffer(buffer_size)
        self.buffer_gx = CircularBuffer(buffer_size)
        self.buffer_ay = CircularBuffer(buffer_size)
        self.buffer_az = CircularBuffer(buffer_size)

        self._create_widgets()
        self._create_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.plot = pg.PlotWidget()
        self.plot.addLegend()
        self.plot.setYRange(-120, 120)

        self.curve_pitch = self.plot.plot(pen='r', name='pitch')
        self.curve_gx = self.plot.plot(pen='g', name='gx')
        self.curve_ay = self.plot.plot(pen='b', name='ay')
        self.curve_az = self.plot.plot(pen='y', name='az')

    def _create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.plot)
        self.setLayout(layout)

    def _connect_signals(self):
        pass

    def add_sample(self, pitch: float, gx: float, ay: float, az: float):
        self.buffer_pitch.add_value(pitch)
        self.buffer_gx.add_value(gx)
        self.buffer_ay.add_value(ay)
        self.buffer_az.add_value(az)

    def update_plot(self):
        self.curve_pitch.setData(self.buffer_pitch.get_data())
        self.curve_gx.setData(self.buffer_gx.get_data())
        self.curve_ay.setData(self.buffer_ay.get_data())
        self.curve_az.setData(self.buffer_az.get_data())
