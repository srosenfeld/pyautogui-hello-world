# pyautogui-hello-world
This basic program will create a new text file called 'Hello world' with that text in the document. This happens by following several steps:

1. Opening the Task View Interface and creating a virtual desktop
2. Opening Notepad, located at C:/Windows/System32/notepad.exe
3. Typing "Hello world!" into notepad, then saving the file to the desktop with the date/time in the name
4. Closing the virtual desktop

Modules used in this program: os, time, sys, subprocess, and pyautogui

--------------------------------------

Instructions:
1. Note: This script will only run on Windows 10 machines, as it utilizes keyboard shortcuts 'Win + Tab' followed by 'Win + Ctrl + D' to create a virtual desktop.

2. Install Python 3 (I'm using 3.6) and let the script run! It will check to see if pyautogui is already installed and, if not, installs it using subprocess.call("pip install pyautogui") before runtime

For more information in PyAutoGui: https://pyautogui.readthedocs.io

--------------------------------------
Further goals:

1. Get program to operate on any version of Windows, then any OS
