'''
Type "Hello World!" in Windows Notepad
--------------------------------------
Description: This basic program utilizes Python's 'os' command to open a new notepad file.
After notepad is open, the Python pyautogui package sends keyboard and mouse commands to the windows.
--------------------------------------

Instructions:
1. Install Python 3 (I'm using 3.6) and use "pip install pyautogui" to install pyautogui on Windows
For more information in PyAutoGui: https://pyautogui.readthedocs.io

2. Add a shortcut to Notepad on your desktop, right click the shortcut, go to Properties.
Under "Run", change "Normal" to "Maximized" so the program opens in full screen.

3. In the script below, change the filepath to point toward the shortcut on your desktop.
Be conscious of the / versus \ !

'''

import os
import pyautogui as pg

#change the filepath below to match the shortcut on your desktop
filepath = "C:/Users/srosenfeld/desktop/notepadshortcut"

#opens the file specified in filepath
os.startfile(filepath)

#changes the number of seconds that each step waits until next one
pg.PAUSE = 1

#if True, the program will close when mouse goes to top-left corner
pg.FAILSAFE = False

#left clicks at the x-y coordinates 960, 200
pg.click(960, 200, 1, 0, button='left')

#sends the keyboard command to the selected window at the seconds specified in interval
pg.typewrite('Hello world!\n', interval = 0.01)
