import pip
import tkinter

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try: 
    import requests
except ImportError:
    install("requests")

try: 
    import PySimpleGUIWeb
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
    import internal
except KeyError:
    print("GUI_API not found")
    exit()

