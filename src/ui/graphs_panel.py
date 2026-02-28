from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from infra.inbound_messages import BotTelemetryMsg
from ui.plots.loop_interval_plot import LoopIntervalPlot
from ui.plots.mpu_plot_widget import MpuPlotWidget


class GraphsPanel(QWidget):

    SAMPLE_RATE = 100
    BUFFER_SECONDS = 10

    def __init__(self):
        super().__init__()

        self._create_widgets()
        self._create_layout()
        self._connect_signals()
        self._create_timers()


    def _create_widgets(self):
        self.loop_interval_plot = LoopIntervalPlot(self.SAMPLE_RATE, self.BUFFER_SECONDS)
        self.pitch_plot = MpuPlotWidget(self.SAMPLE_RATE, self.BUFFER_SECONDS)

    def _create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.loop_interval_plot, )
        layout.addWidget(self.pitch_plot)
        layout.addStretch()
        self.setLayout(layout)

    def _connect_signals(self):
        pass

    def _create_timers(self):
        self.plot_timer = QTimer()
        self.plot_timer.timeout.connect(self._update_plots)
        self.plot_timer.start(25)

    def _update_plots(self):
        self.loop_interval_plot.update_plot()
        self.pitch_plot.update_plot()

    def handle_bot_telemetry(self, msg: BotTelemetryMsg):
        self.loop_interval_plot.add_sample(msg.dt)
        self.pitch_plot.add_sample(msg.pitch, msg.gx, msg.ay * 90, msg.az * 90)
