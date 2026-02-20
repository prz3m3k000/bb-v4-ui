from dataclasses import dataclass

from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QLabel, QGroupBox, QFormLayout, QPushButton, QDoubleSpinBox, QCheckBox


class PidControllerForm(QGroupBox):
    submitted = pyqtSignal(object)
    reset = pyqtSignal()

    def __init__(self, prefix: str):
        super().__init__(f'{prefix} PID settings')
        self._create_widgets()
        self._create_layout()
        self._connect_signals()

    def _create_widgets(self):
        self.p_edit = self._double_spin_box()
        self.i_edit = self._double_spin_box()
        self.d_edit = self._double_spin_box()
        self.output_edit = self._double_spin_box()
        self.apply_on_change = QCheckBox("Apply on change")
        self.apply_button = QPushButton("Apply")
        self.reset_button = QPushButton("Reset")

    def _create_layout(self):
        layout = QFormLayout()
        layout.addRow(QLabel("P"), self.p_edit)
        layout.addRow(QLabel("I"), self.i_edit)
        layout.addRow(QLabel("D"), self.d_edit)
        layout.addRow(QLabel("Output"), self.output_edit)
        layout.addWidget(self.apply_on_change)
        layout.addWidget(self.apply_button)
        layout.addWidget(self.reset_button)
        self.setLayout(layout)

    def _connect_signals(self):
        self.p_edit.valueChanged.connect(self._on_value_changed)
        self.i_edit.valueChanged.connect(self._on_value_changed)
        self.d_edit.valueChanged.connect(self._on_value_changed)
        self.output_edit.valueChanged.connect(self._on_value_changed)
        self.apply_button.clicked.connect(self._on_apply_click)
        self.reset_button.clicked.connect(self._on_reset_click)

    def _on_apply_click(self):
        self._submit_form()

    def _on_reset_click(self):
       self.reset.emit()

    def _on_value_changed(self):
        if self.apply_on_change.isChecked():
            self._submit_form()

    def _submit_form(self):
        self.submitted.emit(PidFormData(p=self._get_p(), i=self._get_i(), d=self._get_d(), output=self._get_output()))

    def _get_p(self):
        return self.p_edit.value()

    def _get_i(self):
        return self.i_edit.value()

    def _get_d(self):
        return self.d_edit.value()

    def _get_output(self):
        return self.output_edit.value()

    def configure_p_edit(self, max_value: float, precision: int, step: float):
        self.p_edit.setMaximum(max_value)
        self.p_edit.setDecimals(precision)
        self.p_edit.setSingleStep(step)

    def configure_i_edit(self, max_value: float, precision: int, step: float):
        self.i_edit.setMaximum(max_value)
        self.i_edit.setDecimals(precision)
        self.i_edit.setSingleStep(step)

    def configure_d_edit(self, max_value: float, precision: int, step: float):
        self.d_edit.setMaximum(max_value)
        self.d_edit.setDecimals(precision)
        self.d_edit.setSingleStep(step)

    def configure_output_edit(self, value: float, max_value: float, precision: int, step: float):
        self.output_edit.setMaximum(max_value)
        self.output_edit.setDecimals(precision)
        self.output_edit.setSingleStep(step)
        self.output_edit.setValue(value)

    @staticmethod
    def _double_spin_box():
        widget = QDoubleSpinBox()
        widget.setAlignment(Qt.AlignmentFlag.AlignRight)
        return widget

@dataclass(frozen=True)
class PidFormData:
    p: float
    i: float
    d: float
    output: float
