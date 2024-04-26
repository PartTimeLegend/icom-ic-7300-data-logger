import csv
import time

class DataLogger:
    CSV_FILE = 's_meter_values.csv'

    def __init__(self, communicator):
        self.communicator = communicator

    def log_data(self):
        with open(self.CSV_FILE, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Timestamp', 'Frequency', 'S-Meter Value'])
            while True:
                data = self.communicator.read_data()
                if data['frequency'] is not None and data['s_meter'] is not None:
                    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                    csv_writer.writerow([timestamp, data['frequency'], data['s_meter']])
                    print(f"Logged frequency {data['frequency']} Hz and S-meter value {data['s_meter']} at {timestamp}")
                else:
                    print("Failed to log data at", timestamp)
                time.sleep(60)
