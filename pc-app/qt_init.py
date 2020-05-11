import pip
import tkinter
import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try: 
    import requests
except ImportError:
    install("requests")

try: 
    import PySimpleGUIQt
except ImportError:
    install("PySimpleGUIQt")

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
    import q_internal
except KeyError:
    print("GUI_API not found")
    exit()

