import subprocess
import os
import webbrowser

def launch():
    target = "/Applications/Air Hockey.app"  # Corrected path

    if target.startswith("https"):
        webbrowser.open(target)  # Opens a website
        print(f"Opening web link: {target}")
    elif os.path.exists(target):
        subprocess.call(["open", "-a", target])  # Open application
        print(f"Launching application: {target}")
    else:
        print(f"Invalid or missing target: {target}")

if __name__ == "__main__":
    launch()
