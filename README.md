# VIT-AP Network Authentication Toolkit

vitap_hostel_wifi is a Python package containing `login` and `logout` functions for handling authentication with VIT-AP's Hostel Wi-Fi network.

# Installation Steps:

**1.Clone the Repository:**

First, you need to clone the repository containing the my_package package. You can do this using Git by running the following command in your terminal or command prompt:
`git clone https://github.com/Udhay-Adithya/vitap_hostel_wifi.git`

**2.Navigate to the Package Directory:**

Once you've cloned the repository, navigate to the my_package directory using the cd command:
`cd vitap_hostel_wifi`

**3.Install the Package:**

Inside the my_package directory, you can install the package using pip. This will make the package available for use in your Python environment. Run the following command:
`pip install .`
The dot (.) at the end indicates that you want to install the package from the current directory.

**4.Verify Installation:**

After the installation is complete, you can verify that the package is installed correctly by importing it in a Python script or interpreter:
`import vitap_hostel_wifi`
If you don't encounter any errors, the package is successfully installed and ready to use.




## Usage
Once installed, you can use the `login` and `logout` functions in your Python scripts.

```
import vitap_hostel_wifi

username = "your_username"
password = "your_password"

# Login
login_result = my_package.login(username, password)
print(login_result)

# Logout
logout_result = my_package.logout(username, password)
print(logout_result)
```
# Directory
__init__.py: Initializes the package and imports the login and logout functions.

login.py: Contains the login function for authentication.

logout.py: Contains the logout function for logging out.

README.md: Instructions and information about the package.




# Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License. 

