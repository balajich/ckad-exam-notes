"""
Health check script to check if a website is up and running.
"""

import requests


def health_check():
    try:
        print("Checking website Health...")
        response = requests.get("https://github.com/balajich")
        if response.status_code == 200:
            print("Website is up and running!")
        else:
            print(f"Website returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking website: {e}")


if __name__ == "__main__":
    health_check()
