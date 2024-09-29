"""
This script writes the current date and time to a log file.
"""
import time
from datetime import datetime


def write_to_log(log_file):
    with open(log_file, "a") as file:
        file.write(f"{datetime.now()}\n")


if __name__ == "__main__":
    log_file = "/logs/datetime.log"
    while True:
        write_to_log(log_file)
        time.sleep(10) # Sleep for 10 seconds
