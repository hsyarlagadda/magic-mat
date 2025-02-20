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

def launch():
    try:
        # Open Recents folder in Finder
        subprocess.call(["open", "file://localhost/System/Library/CoreServices/Finder.app/Contents/Resources/MyLibraries/myDocuments.cannedSearch"])
        print("Opening Recents folder on macOS...")
    except Exception as e:
        print(f"Failed to open Recents folder: {e}")

if __name__ == "__main__":
    launch()
