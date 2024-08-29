import time
import urllib3
import requests
from bs4 import BeautifulSoup
from vitap_hostel_wifi.constants import URL

# Suppressing the SSL Certificate verification warning
urllib3.disable_warnings()


def login(username, password, producttype=0):
    """
    Logs in the user using the provided credentials.

    Args:
        username (str): Official VIT-AP Reg.No of the student.
        password (str): Student Wi-Fi password.
        producttype (int): Type of device (Web=0, IOS=1, Android=2).

    Returns:
        str: Message indicating login status.
    """
    try:
        data = {
            "mode": 191,
            "username": username,
            "password": password,
            "a": int(round(time.time() * 1000)),
            "producttype": producttype,
        }

        # Send a POST request with data using the session object
        with requests.Session() as session:
            response = session.post(URL, data=data, verify=False)

        soup = BeautifulSoup(response.text, features="xml")

        # Check the response and print appropriate message
        message = soup.find("message").text
        # Check the message, and replace '{username}' with the actual username
        if "You are signed in as" in message:
            return f"You are signed in as {username}"
        else:
            return message
    except requests.RequestException as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
