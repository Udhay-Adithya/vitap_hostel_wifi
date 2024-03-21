# vitap_hostel_wifi
VIT-AP Network Authentication Toolkit

vitap_hostel_wifi is a Python package containing `login` and `logout` functions for handling authentication with VIT-AP's Hostel Wi-Fi network.

## Installation

1. Clone the repository:

    git clone https://github.com/Udhay-Adithya/vitap_hostel_wifi.git

2. Navigate to the `vitap_hostel_wifi` directory:

    cd vitap_hostel_wifi

3. Install the package using pip:

    pip install .

## Usage

Once installed, you can use the `login` and `logout` functions in your Python scripts.

```python```
import my_package

username = "your_username"
password = "your_password"

# Login
login_result = my_package.login(username, password)
print(login_result)

# Logout
logout_result = my_package.logout(username, password)
print(logout_result)

Directory Structure:
hostel_wifi/
│
├── __init__.py
├── login.py
├── logout.py


__init__.py: Initializes the package and imports the login and logout functions.
login.py: Contains the login function for authentication.
logout.py: Contains the logout function for logging out.
README.md: Instructions and information about the package.

Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. 

