# VIT-AP Network Authentication Toolkit

vitap_hostel_wifi is a Python package containing `login` and `logout` functions for handling authentication with VIT-AP's Hostel Wi-Fi network.

## Installation Steps:

### **1.Clone the Repository:**

First, you need to clone the repository containing the my_package package. You can do this using Git by running the following command in your terminal or command prompt:
```bash
git clone https://github.com/Udhay-Adithya/vitap_hostel_wifi.git
```

### **2.Navigate to the Package Directory:**

Once you've cloned the repository, navigate to the my_package directory using the cd command:
```bash
cd vitap_hostel_wifi
```
### **3.Install Dependencies:**
Installing these dependencies ensures that your local environment has all the necessary components to execute the project successfully.
```bash
pip install -r requirements.txt
```
### **4.Install the Package:**

Inside the my_package directory, you can install the package using pip. This will make the package available for use in your Python environment. Run the following command:
```bash
pip install .
```
The dot (.) at the end indicates that you want to install the package from the current directory.

### **5.Verify Installation:**

After the installation is complete, you can verify that the package is installed correctly by importing it in a Python script or interpreter:
```python
import vitap_hostel_wifi
```
If you don't encounter any errors, the package is successfully installed and ready to use.




## Usage
Once installed, you can use the `login` and `logout` functions in your Python scripts.


```python
import vitap_hostel_wifi

username = "your_username"
password = "your_password"

# Login
login_result = vitap_hostel_wifi.login(username, password)
print(login_result)

# Logout
logout_result = vitap_hostel_wifi.logout(username, password)
print(logout_result)
```


## Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. 

