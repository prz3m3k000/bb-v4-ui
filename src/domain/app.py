from domain.commands import Commands
from infra.data_sender import UdpDataSender
from infra.udp_commands import UdpCommands


class App:

    BOT_REMOTE_PORT = 8080

    def __init__(self):
        self._data_sender = UdpDataSender()
        self._commands = UdpCommands(self._data_sender)

    def commands(self) -> Commands:
        return self._commands

    def set_bot_address(self, ip: str):
        self._data_sender.set_address(ip, self.BOT_REMOTE_PORT)
