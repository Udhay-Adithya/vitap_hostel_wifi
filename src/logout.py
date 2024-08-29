import time
import urllib3
import requests
from src.constants import URL
from bs4 import BeautifulSoup

# Suppressing the SSL Certificate verification warning
urllib3.disable_warnings()


def logout(username, password, producttype=0):
    """
    Logs out the user using the provided credentials.

    Args:
        username (str): Official VIT-AP Reg.No of the student.
        password (str): User Wi-Fi password.
        producttype (int): Type of device (Web=0, IOS=1, Android=2).

    Returns:
        str: Message indicating logout status.
    """
    try:
        data = {
            "mode": 193,
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
        message = soup.find("message").text # Resposne message will contain this full string'You&amp;#39;ve signed out'
        if message.__contains__(
            "signed out"
        ):  
            return "Successfully Signed Out"
        else:
            return "Signout failed. Please Sign-in first to Sign out."

    except requests.RequestException as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
