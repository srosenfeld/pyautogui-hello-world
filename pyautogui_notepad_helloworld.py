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

filepath = "C:/Users/srosenfeld/desktop/notepadshortcut"

os.startfile(filepath)

pg.position()

pg.size()
#(1920,1080)

pg.PAUSE = 0.5
pg.FAILSAFE = False

pg.moveTo(960, 540, 0.2)
pg.moveTo(960, 200, 0.2)

pg.click(960, 200, 1, 0, button='left')

pg.typewrite('Hello world!\n', interval = 0.01)
