from abc import ABC, abstractmethod



class Commands(ABC):

    CMD_SPEED_PID_COEFFICIENTS = 1
    CMD_PITCH_PID_COEFFICIENTS = 2
    CMD_ENABLE_MOTORBASE = 3
    CMD_DISABLE_MOTORBASE = 4
    CMD_DASHBOARD_ADDRESS = 5
    CMD_SPEED_PID_RESET = 6
    CMD_PITCH_PID_RESET = 7
    CMD_SETPOINTS = 8

    @abstractmethod
    def set_speed_pid_coefficients(self, p: float, i: float, d: float, output: float):
        pass

    @abstractmethod
    def set_pitch_pid_coefficients(self, p: float, i: float, d: float, output: float):
        pass

    @abstractmethod
    def enable_motorbase(self):
        pass

    @abstractmethod
    def disable_motorbase(self):
        pass

    @abstractmethod
    def set_dashboard_address(self, port: int):
        pass

    @abstractmethod
    def speed_pid_reset(self):
        pass

    @abstractmethod
    def pitch_pid_reset(self):
        pass

    @abstractmethod
    def set_setpoints(self, speed: float, pitch: float):
        pass