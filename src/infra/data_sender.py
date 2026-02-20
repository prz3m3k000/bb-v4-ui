import socket
from abc import ABC, abstractmethod


class DataSender(ABC):

    @abstractmethod
    def send(self, data: bytes):
        pass


class UdpDataSender(DataSender):

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip = None
        self.port = None
        pass

    def set_address(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        print(f'UdpDataSender: destination address set to {self.ip}:{self.port}')

    def send(self, data: bytes):
        if self.ip is None or self.port is None:
            print(f'UdpDataSender: ip or port not set (ip="{self.ip}", port="{self.port}")')
            return

        b = self.sock.sendto(data, (self.ip, self.port))
        print(f'UdpDataSender: sent {b} bytes to {self.ip}:{self.port}')
