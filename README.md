# IC-7300 Data Logger

This Python script interfaces with an Icom IC-7300 transceiver via USB-serial connection to log S-meter values and frequency readings to a CSV file at regular intervals.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/parttimelegend/icom-ic-7300-data-logger.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ic-7300-data-logger
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure the Icom IC-7300 transceiver is connected to your computer via USB.

2. Run the main script `main.py`:

    ```bash
    python main.py
    ```

3. The script will automatically detect the IC-7300, log the S-meter values and frequency readings to a CSV file named `s_meter_values.csv` in the project directory, and print the logged data to the console.

4. Press `Ctrl+C` to stop the script.

## Configuration

- The script uses the default CI-V address (0x94) for the IC-7300. Modify the `CIV_ADDRESS` variable in `radio_communicator.py` if your transceiver is configured with a different address.

- By default, the script logs data every 60 seconds. You can adjust the logging interval by changing the sleep duration in the `log_data` method of `data_logger.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
