import sys
import subprocess

#Check to see if pyautogui is installed
try:
    import pyautogui as pg
    print("pyautogui already installed")

#If not installed, use subprocess to send command to shell
except ImportError:
    print("Installing pyautogui")
    subprocess.call("pip install pyautogui")
    sys.exit(1)
    import pyautogui as pg
