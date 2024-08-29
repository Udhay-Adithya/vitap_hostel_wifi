import subprocess


def turn_on_wifi():
    try:
        subprocess.run(
            ["netsh", "interface", "set", "interface", "Wi-Fi", "enabled"], check=True
        )
        return "Wi-Fi turned on"
    except subprocess.CalledProcessError as e:
        return f"Failed to turn on Wi-Fi: {e}"


def connect_to_wifi(ssid):
    try:
        subprocess.run(["netsh", "wlan", "connect", f"name={ssid}"], check=True)
        return f"Connected to {ssid} Wi-Fi"
    except subprocess.CalledProcessError as e:
        return f"Failed to connect to {ssid}: {e}"


def connect_to_available_networks():
    networks = ["HOSTEL", "VITAP-HOSTEL"]

    result = subprocess.run(
        ["netsh", "interface", "show", "interface", "name=Wi-Fi"],
        capture_output=True,
        text=True,
    )
    if "Disabled" in result.stdout:
        wifi_status = turn_on_wifi()
        if "Failed" in wifi_status:
            return wifi_status

    for ssid in networks:
        try:
            result = subprocess.run(
                ["netsh", "wlan", "show", "network"], capture_output=True, text=True
            )
            if ssid in result.stdout:
                return connect_to_wifi(ssid)
        except subprocess.CalledProcessError as e:
            return f"Error checking network availability: {e}"

    return "Please turn On your Wi-Fi"
