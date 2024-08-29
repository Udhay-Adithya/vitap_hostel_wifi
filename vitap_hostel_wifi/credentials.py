import os

CREDENTIALS_FILE = 'credentials.txt'

def save_credentials(username, password):
    """
    Save username and password to a file.
    """
    with open(CREDENTIALS_FILE, 'w') as f:
        f.write(f"{username}\n{password}")

def load_credentials():
    """
    Load saved username and password from the file.
    """
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as f:
            lines = f.readlines()
            if len(lines) >= 2:
                return lines[0].strip(), lines[1].strip()
    return None, None
