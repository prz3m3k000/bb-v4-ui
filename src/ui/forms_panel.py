from PyQt6.QtWidgets import QWidget, QVBoxLayout

from domain.app import App
from ui.forms.communication_form import CommunicationForm, CommunicationFormData
from ui.forms.motorbase_form import MotorbaseForm
from ui.forms.pid_controller_form import PidControllerForm, PidFormData
from ui.forms.setpoints_form import SetpointsForm, SetpointsData


class FormsPanel(QWidget):

    def __init__(self, app: App):
        super().__init__()

        self.app = app
        self._create_widgets()
        self._create_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.speed_pid_form = PidControllerForm("Speed")
        self.speed_pid_form.configure_p_edit(1, 5, 0.0001)
        self.speed_pid_form.configure_i_edit(1, 5, 0.0001)
        self.speed_pid_form.configure_d_edit(1, 5, 0.00001)
        self.speed_pid_form.configure_output_edit(15, 15, 5, 0.1)


        self.pitch_pid_form = PidControllerForm("Pitch")
        self.pitch_pid_form.configure_p_edit(1000, 4, 1)
        self.pitch_pid_form.configure_i_edit(100, 4, 0.1)
        self.pitch_pid_form.configure_d_edit(10, 4, 0.01)
        self.pitch_pid_form.configure_output_edit(3000, 3000, 4, 1)

        self.setpoints_form = SetpointsForm()

        self.motorbase_form = MotorbaseForm()
        self.communication_form = CommunicationForm()

    def _create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.speed_pid_form)
        layout.addWidget(self.pitch_pid_form)
        layout.addWidget(self.setpoints_form)
        layout.addWidget(self.motorbase_form)
        layout.addWidget(self.communication_form)
        layout.addStretch()
        self.setLayout(layout)

    def _connect_signals(self):
        self.speed_pid_form.submitted.connect(self._on_speed_pid_data_submitted)
        self.speed_pid_form.reset.connect(self._on_speed_pid_reset_submitted)
        self.pitch_pid_form.submitted.connect(self._on_pitch_pid_data_submitted)
        self.pitch_pid_form.reset.connect(self._on_pitch_pid_reset_submitted)
        self.setpoints_form.submitted.connect(self._on_setpoints_data_submitted)
        self.motorbase_form.motorbase_enabled.connect(self._on_motorbase_enabled)
        self.communication_form.submitted.connect(self._on_communication_data_submitted)

    def _on_speed_pid_data_submitted(self, data: PidFormData):
        print(f'Speed PID data = {data}')
        self.app.commands().set_speed_pid_coefficients(data.p, data.i, data.d, data.output)

    def _on_speed_pid_reset_submitted(self):
        print(f'Speed PID reset')
        self.app.commands().speed_pid_reset()

    def _on_pitch_pid_data_submitted(self, data: PidFormData):
        print(f'Pitch PID data = {data}')
        self.app.commands().set_pitch_pid_coefficients(data.p, data.i, data.d, data.output)

    def _on_pitch_pid_reset_submitted(self):
        print(f'Pitch PID reset')
        self.app.commands().pitch_pid_reset()

    def _on_setpoints_data_submitted(self, data: SetpointsData):
        print(f'Setpoints data = {data}')
        self.app.commands().set_setpoints(data.speed, data.pitch)

    def _on_motorbase_enabled(self, enabled: bool):
        print(f'Motor base status: {enabled}')
        if enabled:
            self.app.commands().enable_motorbase()
        else:
            self.app.commands().disable_motorbase()

    def _on_communication_data_submitted(self, data: CommunicationFormData):
        print(f'Communication data = {data}')
        self.app.set_bot_address(data.bot_ip)
        self.app.commands().set_dashboard_address(data.dashboard_port)
