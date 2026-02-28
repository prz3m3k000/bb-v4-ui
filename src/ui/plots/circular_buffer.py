import numpy as np


class CircularBuffer:
    def __init__(self, size: int):
        self.size = size
        self.index = 0
        self.buffer = np.zeros(size)

    def add_value(self, v: float):
        self.buffer[self.index] = v
        self.index = (self.index + 1) % self.size

    def get_data(self):
        return np.roll(self.buffer, -self.index)
