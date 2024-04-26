import serial
from abc import ABC, abstractmethod

class RadioCommunicator(ABC):
    @abstractmethod
    def read_data(self):
        pass

class ICOM7300Communicator(RadioCommunicator):
    BAUD_RATE = 9600
    TIMEOUT = 3
    CIV_ADDRESS = 0x94
    SMETER_CMD = bytes([0xFE, 0xFE, CIV_ADDRESS, 0xE0, 0x15, 0x02, 0xFD])
    FREQ_CMD = bytes([0xFE, 0xFE, CIV_ADDRESS, 0xE0, 0x03, 0xFD])

    def __init__(self, serial_port):
        self.serial_port = serial.Serial(serial_port, self.BAUD_RATE, timeout=self.TIMEOUT)

    def read_data(self):
        return {
            'frequency': self._read_frequency(),
            's_meter': self._read_s_meter()
        }

    def _read_frequency(self):
        self.serial_port.write(self.FREQ_CMD)
        response = self.serial_port.read(14)
        if len(response) == 14 and response[:2] == b'\xfe\xfe':
            freq_data = response[6:11]
            frequency = int.from_bytes(freq_data, byteorder='big')
            return frequency
        return None

    def _read_s_meter(self):
        self.serial_port.write(self.SMETER_CMD)
        response = self.serial_port.read(11)
        if len(response) == 11 and response[:2] == b'\xfe\xfe':
            return response[9]
        return None
