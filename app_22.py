# import subprocess
# import os
# import webbrowser

# def launch():
#     target = "https://www.instagram.com"  # Replace this with actual application path or URL
    
#     if target.startswith("https"):
#         webbrowser.open(target)  # Opens a website
#         print(f"Opening web link: {target}")
#     elif os.path.exists(target):
#         subprocess.call(["open", target])  # Opens a local application (macOS)
#         print(f"Launching application: {target}")
#     else:
#         print(f"Invalid or missing target: {target}")

# if __name__ == "__main__":
#     launch()


import subprocess
import time

def launch():
    try:
        # Open System Settings
        subprocess.call(["open", "/System/Applications/System Settings.app"])
        print("Opening System Settings...")

        # Small delay to allow System Settings to open
        time.sleep(1)

        # Simulate keyboard shortcut to search "Bluetooth"
        subprocess.call(["osascript", "-e", 'tell application "System Events" to keystroke "Bluetooth"'])

        print("Navigating to Bluetooth settings...")
    except Exception as e:
        print(f"Failed to open Bluetooth settings: {e}")

if __name__ == "__main__":
    launch()
