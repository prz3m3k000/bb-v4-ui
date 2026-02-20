import struct

from domain.commands import Commands
from infra.data_sender import DataSender


class UdpCommands(Commands):

    def __init__(self, sender: DataSender):
        self.sender = sender

    def set_speed_pid_coefficients(self, p: float, i: float, d: float, output:float):
        data = struct.pack('<B4f', self.CMD_SPEED_PID_COEFFICIENTS, p, i, d, output)
        self.sender.send(data)

    def set_pitch_pid_coefficients(self, p: float, i: float, d: float, output: float):
        data = struct.pack('<B4f', self.CMD_PITCH_PID_COEFFICIENTS, p, i, d, output)
        self.sender.send(data)

    def enable_motorbase(self):
        data = struct.pack('<B', self.CMD_ENABLE_MOTORBASE)
        self.sender.send(data)

    def disable_motorbase(self):
        data = struct.pack('<B', self.CMD_DISABLE_MOTORBASE)
        self.sender.send(data)

    def set_dashboard_address(self, port: int):
        data = struct.pack("<BH", self.CMD_DASHBOARD_ADDRESS, port)
        self.sender.send(data)

    def speed_pid_reset(self):
        data = struct.pack('<B', self.CMD_SPEED_PID_RESET)
        self.sender.send(data)

    def pitch_pid_reset(self):
        data = struct.pack('<B', self.CMD_PITCH_PID_RESET)
        self.sender.send(data)

    def set_setpoints(self, speed: float, pitch: float):
        data = struct.pack('<B2f', self.CMD_SETPOINTS, speed, pitch)
        self.sender.send(data)





