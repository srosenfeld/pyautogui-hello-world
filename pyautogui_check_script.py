import sys
try:
    import pyautogui
    print("pyautogui installed")
except ImportError:
    print("Sorry, no dice")
    sys.exit(1)
