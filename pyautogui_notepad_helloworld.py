'''
Type "Hello World!" in Windows Notepad
--------------------------------------
Description:
This basic program utilizes several modules to open a new notepad file, type "Hello world", and save it to the desktop.
After notepad is open and focused, the Python pyautogui package sends keyboard and mouse commands to the windows.
The script will check to see if pyautogui is installed on the current machine and, if not, will install and continue the script.

Note:
This program currently only works on Windows 10. I'm still researching ways for this to work on earlier versions of Windows.
--------------------------------------
'''

import os
import time
import sys
import subprocess

#Starts timer for measuring speed of script
start = time.time()

#Check to see if pyautogui is installed
try:
    import pyautogui as pg
    print("Script proceeding - pyautogui already installed")

#If not installed, use subprocess to send command to shell
except ImportError:
    print("Installing pyautogui")
    subprocess.call("pip install pyautogui")
    sys.exit(1)
    print("Script proceeding - pyautogui now installed")
    import pyautogui as pg

#Sets Home Directory for Current User
homedir = os.environ['HOME']

#Opens Task View Interface
pg.keyDown('winleft')
pg.press('tab')
pg.keyUp('winleft')

#Create new virtual desktop
pg.keyDown('winleft')
pg.keyDown('ctrl')
pg.press('d')
pg.keyUp('winleft')
pg.keyUp('ctrl')

#Select new virtual desktop
pg.press('enter')

#Wait 2 seconds
pg.PAUSE = 2

#change the filepath below to match the application path
filepath = "C:/Windows/System32/notepad.exe"

#opens the file specified in filepath
os.startfile(filepath)

#changes the number of seconds that each step waits until next one
pg.PAUSE = 1

#Opens Task View Interface
pg.keyDown('winleft')
pg.press('tab')
pg.keyUp('winleft')

#Selects Notepad as top-level program
pg.press('enter')

#if True, the program will close when mouse goes to top-left corner
pg.FAILSAFE = False

#sends the keyboard command to the selected window at the seconds specified in interval
pg.typewrite('Hello world!\n', interval = 0.01)

#Saves file
pg.keyDown('ctrl')
pg.press('s')
pg.keyUp('ctrl')

#Names file "Hello world" + date and saves it to the desktop by closing "Save" window
pg.typewrite((homedir + '\Desktop\\' + 'Hello world ' + str(time.strftime("%d-%m-%Y ")) + str(time.strftime("%H-%M-%S"))), interval = 0.01)
pg.press('enter')

#Closes Notepad
pg.keyDown('altleft')
pg.press('space')
pg.press('c')
pg.keyUp('altleft')

#Close current virtual desktop
pg.keyDown('winleft')
pg.keyDown('ctrl')
pg.press('f4')
pg.keyUp('winleft')
pg.keyUp('ctrl')

#Ends timer for measuring time of script
end = time.time()

#Prints "Complete"
print("Script complete. Time elapsed: " + str(end-start) + "seconds")
