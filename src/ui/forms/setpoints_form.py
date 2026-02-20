from dataclasses import dataclass

from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QGroupBox, QDoubleSpinBox, QLabel, QFormLayout, QCheckBox, QPushButton


class SetpointsForm(QGroupBox):
    submitted = pyqtSignal(object)

    def __init__(self):
        super().__init__(f'Setpoints')
        self._create_widgets()
        self._create_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.speed_setpoint_edit = self._double_spin_box()
        self.speed_setpoint_edit.setMinimum(-100)
        self.speed_setpoint_edit.setMaximum(100)
        self.speed_setpoint_edit.setDecimals(2)
        self.speed_setpoint_edit.setSingleStep(0.1)
        self.speed_setpoint_edit.setValue(0)


        self.pitch_setpoint_edit = self._double_spin_box()
        self.pitch_setpoint_edit.setMinimum(-5)
        self.pitch_setpoint_edit.setMaximum(5)
        self.pitch_setpoint_edit.setDecimals(2)
        self.pitch_setpoint_edit.setSingleStep(0.1)
        self.pitch_setpoint_edit.setValue(0)


        self.apply_on_change = QCheckBox("Apply on change")
        self.apply_on_change.setCheckState(Qt.CheckState.Checked)

        self.apply_button = QPushButton("Apply")
        pass

    def _create_layout(self):
        layout = QFormLayout()
        layout.addRow(QLabel("Speed"), self.speed_setpoint_edit)
        layout.addRow(QLabel("Pitch"), self.pitch_setpoint_edit)
        layout.addWidget(self.apply_on_change)
        layout.addWidget(self.apply_button)
        self.setLayout(layout)

    def _connect_signals(self):
        self.speed_setpoint_edit.valueChanged.connect(self._on_value_changed)
        self.pitch_setpoint_edit.valueChanged.connect(self._on_value_changed)
        self.apply_button.clicked.connect(self._on_apply_click)

    def _on_apply_click(self):
        self._submit_form()

    def _on_value_changed(self):
        if self.apply_on_change.isChecked():
            self._submit_form()

    def _submit_form(self):
        self.submitted.emit(SetpointsData(speed=self.speed_setpoint_edit.value(), pitch=self.pitch_setpoint_edit.value()))

    @staticmethod
    def _double_spin_box():
        widget = QDoubleSpinBox()
        widget.setAlignment(Qt.AlignmentFlag.AlignRight)
        return widget

@dataclass(frozen=True)
class SetpointsData:
    speed: float
    pitch: float
