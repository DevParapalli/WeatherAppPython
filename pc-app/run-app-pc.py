import os 
import sys

# printing menu
print("-----------------------------------------")
print("DevParapalli App Launcher")
print("Select from the following...")
print("")
print("1. tkinter version [1, tkinter]  - Fully Working")
print("2. remi version [2, remi]  - Fully Working")
print("3. pyqt version [3, qt, pyqt]  - Image Not Working")
print("")
print("-----------------------------------------")
# User Input choice
choice = input("Enter Choice: ")
# Choice logic
if choice in ("1", "tkinter"):
    print("Selecting tkinter...")
    import tk_init    
elif choice in ("2", "remi"):
    print("Selecting Remi...")
    print("The App will open in a web browser")
    print("if it doesn't navigate to 127.0.0.1:42069")
    import remi_init
elif choice in ("3", "qt", "pyqt"):
    print("Selecting PyQt...")
    import qt_init
else:
    print("Wrong Choice...")
    print("Defaulting to tkinter")
    print("Selecting tkinter...")
    import tk_init
