import serial.tools.list_ports

class IcomRadioDetector():
    def detect_radios():
        radios = []
        ports = serial.tools.list_ports.comports()
        for port, desc, _hwid in sorted(ports):
            if "icom" in desc.lower():
                radios.append(port)
        return radios
