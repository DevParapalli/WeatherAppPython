import tkinter
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try: 
    import requests
except ImportError:
    install("requests")

try: 
    import PySimpleGUI
except ImportError:
    install("PySimpleGUI")

try:
    import logo
except:
    print("Logo Image (Base64) not found")
    exit()

try:
    import icons
except:
    print("Icons (Base64) not found")
    exit()

try:
    import internal_script
except :
    print("tkinter_GUI_API not found")
    exit()

