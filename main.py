import time
from radio_communicator import ICOM7300Communicator
from data_logger import DataLogger
import serial.tools.list_ports
from icom_radio_detector import IcomRadioDetector

def main():
    ports = IcomRadioDetector.detect_radios()
    if not ports:
        print("No radio detected")
    for port in ports:
        communicator = ICOM7300Communicator(port)
        logger = DataLogger(communicator)
        logger.log_data()

if __name__ == '__main__':
    main()
