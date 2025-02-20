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
import os

def launch():
    target = "~/Downloads"  # This is the actual path to the Downloads folder on macOS

    if os.path.exists(os.path.expanduser(target)):  # Check if Downloads directory exists
        subprocess.call(["open", os.path.expanduser(target)])  # Open Downloads in Finder
        print(f"Opening Downloads folder on macOS: {target}")
    else:
        print("Downloads folder not found!")

if __name__ == "__main__":
    launch()
