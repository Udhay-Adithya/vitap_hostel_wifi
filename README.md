# My Tkinter Application

## Overview

This application is a custom-built GUI using Tkinter in Python. It includes features like a "Logout" button and other functionalities designed to fit specific needs.

## Installation

1. **Prerequisites:**
   - Just a Windows Machine
   - No additional software is required on your machine to run the executable. The `.exe` file includes all necessary components.


2. **Installation Steps:**
   - **Windows:**
     - Download the executable from the release page.
     - Open a command prompt and navigate to the directory containing the executable.
     - Run the application by typing the executable's name (`Hostel Wi-fi.exe`).

## Running the Application

1. **Windows:**
   - Open a command prompt.
   - Navigate to the directory containing the executable.
   - Run the application by typing the executable's name (`Hostel Wi-fi.exe`).

2. **Mac/Linux:**
   - Not Supported Yet

## Features

- **Auto connect to Wi-Fi:** Detects and automatically connects to Hostel Wi-Fi.
- **Login Button:** Logs in the user in a single click.
- **Logout Button:** Logs out the user in a single click.

## Instructions for Setting the Application as a Startup App (Windows)(Optional)

1. **Create a Shortcut:**
   - Navigate to the directory containing your `.exe` file.
   - Right-click on the `.exe` file and select `Create shortcut`.

2. **Move Shortcut to Startup Folder:**
   - Press `Win + R` to open the Run dialog.
   - Type `shell:startup` and press Enter. This opens the Startup folder.
   - Move or copy the shortcut you created into this folder.

   Alternatively, you can create a script to automatically add your application to the startup folder:

   ```python
   import os
   import shutil
   import winreg as reg

   def add_to_startup():
       shortcut_path = r'C:\Path\To\YourApp.exe'
       startup_folder = os.getenv('APPDATA') + r'\Microsoft\Windows\Start Menu\Programs\Startup'
       shutil.copy(shortcut_path, startup_folder)
       print("Application added to startup.")

   if __name__ == "__main__":
       add_to_startup()
