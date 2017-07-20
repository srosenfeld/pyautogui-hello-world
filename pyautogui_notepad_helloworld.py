'''
Type "Hello World!" in Windows Notepad
--------------------------------------
Description: This basic program utilizes Python's 'os' command to open a new notepad file.
After notepad is open and focused, the Python pyautogui package sends keyboard and mouse commands to the windows.
--------------------------------------

Instructions:

Install Python 3 (I'm using 3.6) and use "pip install pyautogui" to install pyautogui on Windows
For more information in PyAutoGui: https://pyautogui.readthedocs.io

'''

import os
import pyautogui as pg
import time

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

#change the filepath below to match the shortcut on your desktop
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

#Names file "Hello world" + date and saves it by closing "Save" window
pg.typewrite(('Hello world ' + str(time.strftime("%d-%m-%Y ")) + str(time.strftime("%H-%M-%S"))), interval = 0.01)
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
