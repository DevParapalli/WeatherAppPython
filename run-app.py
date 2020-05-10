import os 
import sys
# complex logic to get multiple versions of the app working...
cwd = os.getcwd()
remi_cwd = cwd + "\\remi_app\\"
qt_cwd = cwd + "\\qt_app\\"
tkinter_cwd = cwd + "\\tkinter_app\\"

# printing menu
print("-----------------------------------------")
print("DevParapalli App Launcher")
print("Select from the following...")
print("")
print("1. tkinter version [1, tkinter]")
print("2. remi version [2, remi]")
print("3. pyqt version [3, qt, pyqt]")
print("")
print("-----------------------------------------")
# User Input choice
choice = input("Enter Choice: ")
# Choice logic
if choice in ("1", "tkinter"):
    print("Selecting tkinter...")
    sys.path.insert(1, tkinter_cwd)
    import tk_init    
elif choice in ("2", "remi"):
    print("Selecting Remi...")
    print("The App will open in a web browser")
    print("if it doesn't navigate to 127.0.0.1:42069")
    sys.path.insert(1, remi_cwd)
    import remi_init
elif choice in ("3", "qt", "pyqt"):
    print("Selecting PyQt...")
    sys.path.insert(1, qt_cwd)
    import qt_init
else:
    print("Wrong Choice...")
    print("Defaulting to tkinter")
    print("Selecting tkinter...")
    sys.path.insert(1, tkinter_cwd)
    import tk_init
