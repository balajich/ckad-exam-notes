"""
Health check script to check if a website is up and running.
"""
import time

import requests


def health_check():
    while True:
        try:
            print("Checking website Health...")
            response = requests.get("https://github.com/balajich")
            if response.status_code == 200:
                print("Website is up and running!")
            else:
                print(f"Website returned status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error checking website: {e}")
        time.sleep(15)


if __name__ == "__main__":
    while True:
        health_check()
