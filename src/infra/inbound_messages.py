import struct
from abc import ABC
from dataclasses import dataclass
from typing import ClassVar

class BaseInboundMessage(ABC):
    STRUCT_FORMAT: ClassVar[str]

    @classmethod
    def from_bytes(cls, data: bytes):
        if not hasattr(cls, 'STRUCT_FORMAT'):
            raise NotImplementedError(f'{cls.__name__} must define STRUCT_FORMAT')

        expected_size = struct.calcsize(cls.STRUCT_FORMAT)
        actual_size = len(data)

        if actual_size != expected_size:
            raise ValueError(f'{cls.__name__}: expected {expected_size} bytes, got {actual_size}')

        return cls(*struct.unpack(cls.STRUCT_FORMAT, data))


@dataclass(frozen=True)
class BotTelemetryMsg(BaseInboundMessage):
    STRUCT_FORMAT = '<BI10f'
    # ---
    msg_id: int
    timestamp: int
    dt: float
    ax: float
    ay: float
    az: float
    gx: float
    gy: float
    gz: float
    pitch: float
    roll: float
    yaw: float