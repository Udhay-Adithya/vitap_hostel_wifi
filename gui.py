import threading
import tkinter as tk
from tkinter import simpledialog
from tkinter import font
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw, ImageTk
from src.login import login
from src.logout import logout
from src.auto_connect import connect_to_available_networks
from src.credentials import save_credentials, load_credentials
from src.constants import (
    bgColor,
    primaryTextColor,
    secondaryTextColor,
    containerColor,
    activeColor,
)

# Initialize the icon variable globally
icon = None

# To solve blurry fonts on Windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

def on_tray_login(icon, item):
    try:
        username, password = load_credentials()
        if not username or not password:
            username = simpledialog.askstring("Input", "Enter Username :", parent=root)
            password = simpledialog.askstring("Input", "Enter Password :", parent=root)

        if username and password:
            save_credentials(username, password)
            result = login(username, password)
            icon.notify(result)
    except Exception:
        pass

def on_tray_logout(icon, item):
    try:
        username, password = load_credentials()
        if not username or not password:
            username = simpledialog.askstring("Input", "Enter Username :", parent=root)
            password = simpledialog.askstring("Input", "Enter Password :", parent=root)

        if username and password:
            result = logout(username, password)
            icon.notify(result)
    except Exception:
        pass

def on_tray_quit(icon, item):
    try:
        icon.stop()
        root.quit()
    except Exception:
        pass

def setup_tray():
    global icon
    try:
        try:
            tray_icon = Image.open("C:/vitap_hostel_wifi/favicon.ico")  # Use full path
        except FileNotFoundError:
            # Create a simple default icon if favicon.ico is not found
            tray_icon = Image.new('RGB', (64, 64), (255, 255, 255))
            d = ImageDraw.Draw(tray_icon)
            d.text((10, 10), "Wi-Fi", fill=(0, 0, 0))

        menu = Menu(
            MenuItem("Open", on_show),
            MenuItem("Login", on_tray_login),
            MenuItem("Logout", on_tray_logout),
            MenuItem("Exit", on_tray_quit),
        )

        icon = Icon("VITAP Wi-Fi Tool", tray_icon, "VITAP Wi-Fi Tool", menu)
        icon.run()
    except Exception:
        pass

def on_show(icon, item):
    try:
        icon.stop()  # Stop the tray icon
        root.after(0, root.deiconify)  # Restore the Tkinter window
    except Exception:
        pass

def minimize_to_tray():
    global icon
    try:
        root.withdraw()  # Hide the window
        if icon is None:
            tray_thread = threading.Thread(target=setup_tray)
            tray_thread.start()
    except Exception:
        pass

def on_closing():
    minimize_to_tray()

def display_wifi_status():
    try:
        status = connect_to_available_networks()
        wifi_status_label.config(text=status)
    except Exception:
        pass

# Create the main window
root = tk.Tk()
root.title("VIT-AP Hostel Wi-Fi Login")

try:
    # Set a custom icon for the Tkinter window (use your .ico file)
    root.iconbitmap("c:/vitap_hostel_wifi/favicon.ico")
except Exception:
    pass

# Set window size
root.geometry("1920x1080")

# Change the background color using configure
root.configure(bg=bgColor)

# Override the close event to minimize to tray
root.protocol("WM_DELETE_WINDOW", on_closing)

# Bind the minimize event
root.bind(
    "<Unmap>", lambda event: minimize_to_tray() if root.state() == "iconic" else None
)

def on_login():
    try:
        username = username_entry.get()
        password = password_entry.get()

        # Save the credentials
        save_credentials(username, password)

        # Call the login function
        result = login(username, password)
        response_label.config(text=result)
    except Exception:
        pass

def on_logout():
    try:
        username = username_entry.get()
        password = password_entry.get()

        # Call the logout function
        result = logout(username, password)
        response_label.config(text=result)
    except Exception:
        pass

# Set custom fonts for labels and buttons
label_font = font.Font(family="Verdana", size=12, weight="normal")
button_font = font.Font(family="Arial", size=8, weight="bold")
input_font = font.Font(family="Arial", size=12, weight="bold")

# Center-align window on the screen
window_width = 424
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Load stored credentials if available
saved_username, saved_password = load_credentials()

# Wi-Fi status label at the top
wifi_status_label = tk.Label(root, text="", font=label_font, bg=bgColor, fg="#00FF40")
wifi_status_label.grid(
    row=0,
    column=0,
    columnspan=2,
    padx=8,
    pady=8,
)

# Username field
username_label = tk.Label(
    root, text="Username :", font=label_font, fg=primaryTextColor, bg=bgColor
)
username_label.grid(row=1, column=0, padx=8, pady=8, ipadx=4, ipady=4, sticky=tk.E)

username_entry = tk.Entry(root, width=15, fg=secondaryTextColor, bg=containerColor, font=input_font)
username_entry.grid(row=1, column=1, padx=8, pady=8, ipadx=4, ipady=4)

# Insert saved username
if saved_username:
    username_entry.insert(0, saved_username)

# Password field
password_label = tk.Label(
    root, text="Password :", font=label_font, fg=primaryTextColor, bg=bgColor
)
password_label.grid(row=2, column=0, padx=8, pady=8, ipadx=4, ipady=4, sticky=tk.E)

password_entry = tk.Entry(root, show="*", width=15, fg=secondaryTextColor, bg=containerColor, font=input_font)
password_entry.grid(row=2, column=1, padx=8, pady=8, ipadx=4, ipady=4)

# Insert saved password
if saved_password:
    password_entry.insert(0, saved_password)

# Login button
login_button = tk.Button(
    root,
    text="Login",
    command=on_login,
    width=10,
    font=button_font,
    fg=bgColor,
    bg=activeColor,
)
login_button.grid(row=3, column=0, padx=8, pady=8)

# Logout button
logout_button = tk.Button(
    root,
    text="Logout",
    command=on_logout,
    width=10,
    font=button_font,
    fg=bgColor,
    bg=activeColor,
)
logout_button.grid(row=3, column=1, padx=8, pady=8)

# Response label
response_label = tk.Label(root, text="", font=label_font, bg=bgColor, fg=primaryTextColor)
response_label.grid(row=4, column=0, columnspan=2, padx=8, pady=8)

# Start displaying Wi-Fi status
display_wifi_status()

# Run the main event loop
root.mainloop()
