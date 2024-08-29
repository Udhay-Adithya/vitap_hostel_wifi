import time
import urllib3
import requests
from bs4 import BeautifulSoup
from src.constants import URL

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
        if len(username) < 6:
            return "Username too short"
        if len(password) < 6:
            return "Password too short"
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
            print(response.text)

        soup = BeautifulSoup(response.text, features="xml")

        # Check the response and print appropriate message
        message = soup.find("message").text
        # Check the message, and replace '{username}' with the actual username
        print(message)
        
        if "You are signed in as" in message:
            return f"You are signed in as {username}"
        else:
            return message
    except requests.RequestException as e:
        error_str = str(e)
        if "HTTPSConnectionPool" in error_str:
            return "Login Failed\nMake sure you are connected\nto hostel Wi-Fi"
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
