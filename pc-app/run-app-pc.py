import os 
import sys
import ast

# change working directory to the one with script
if "\\" in sys.argv[0] or "/" in sys.argv[0]: 
    print("Script is running from Absolute Path")
    head, tail = os.path.split(sys.argv[0])
    os.chdir(head)
elif "\\" not in sys.argv[0] or "/" not in sys.argv[0]:
    print("Script is running from CWD")

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
# options.txt update function
def update_options(mode: str): 
    with open('options.txt', "r") as options_file:
        options_dict = ast.literal_eval(options_file.read())
    options_dict['mode'] = mode
    with open('options.txt', "w") as options_file:
        print(str(options_dict), file=options_file) 
# Choice logic

if choice in ("1", "tkinter"):
    print("Selecting tkinter...")
    update_options('tkinter')
elif choice in ("2", "remi"):
    print("Selecting Remi...")
    print("The App will open in a web browser")
    print("if it doesn't navigate to 127.0.0.1:42069")
    update_options('remi')
elif choice in ("3", "qt", "pyqt"):
    print("Selecting PyQt...")
    update_options('pyqt')
else:
    print("Wrong Choice...")
    print("Defaulting to tkinter")
    print("Selecting tkinter...")
    update_options('tkinter')

import initial_script

