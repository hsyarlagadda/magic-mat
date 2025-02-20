import subprocess
import os
import webbrowser

def launch():
    target = "https://www.linkedin.com"  # Replace this with actual application path or URL
    
    if target.startswith("https"):
        webbrowser.open(target)  # Opens a website
        print(f"Opening web link: {target}")
    elif os.path.exists(target):
        subprocess.call(["open", target])  # Opens a local application (macOS)
        print(f"Launching application: {target}")
    else:
        print(f"Invalid or missing target: {target}")

if __name__ == "__main__":
    launch()
