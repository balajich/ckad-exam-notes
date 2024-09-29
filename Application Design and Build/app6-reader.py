"""
This script reads the log file and prints the contents.
"""
import time


def read_log(log_file):
    with open(log_file, "r") as file:
        for line in file:
            print(line.strip())


if __name__ == "__main__":
    log_file = "/logs/datetime.log"
    while True:
        read_log(log_file)
        time.sleep(10) # Sleep for 10 seconds

