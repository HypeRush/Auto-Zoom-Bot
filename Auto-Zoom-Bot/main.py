import datetime
import os
import subprocess
import sys
import cv2

import pyautogui
from termcolor import cprint

import time

path2 = R"C:\Users\$USERNAME\AppData\Roaming\Zoom\bin\Zoom.exe"
exp_var2 = os.path.expandvars(path2)


def join(id, password, exp_var2):
    subprocess.call(exp_var2)
    while True:
        join1 = pyautogui.locateOnScreen('join1.png')
        if join1 is not None:
            pyautogui.click(join1)
            cprint("Pressed join field.", 'green', attrs=['bold'], file=sys.stderr)
            break
        else:
            cprint("Cannot find join field.", 'red', attrs=['bold'], file=sys.stderr)
            time.sleep(2)

    while True:
        feild = pyautogui.locateOnScreen('feild.png')
        if feild is not None:
            pyautogui.click(feild)
            cprint("Pressed password field.", 'green', attrs=['bold'], file=sys.stderr)
            pyautogui.typewrite(id)
            pyautogui.click(pyautogui.locateOnScreen('join2.png'))
            break
        else:
            cprint("Cannot find id field.", 'red', attrs=['bold'], file=sys.stderr)

    while True:
        feild2 = pyautogui.locateOnScreen('feild2.png')
        if feild2 is not None:
            pyautogui.click(feild2)
            cprint("Pressed password field", 'green', attrs=['bold'], file=sys.stderr)
            pyautogui.typewrite(password)
            pyautogui.click(pyautogui.locateOnScreen('join3.png'))
            break
        else:
            cprint("Cannot find password field.", 'red', attrs=['bold'], file=sys.stderr)


while True:
    now = datetime.datetime.now()
    current_time: str = (now.strftime("%A-%H:%M"))

    if current_time == "Wednesday-11:20" or current_time == "Thursday-12:40" or current_time == "Friday-11:20" or current_time == "Monday-13:24":#You can change times for your planned meetings
        print("Joining Meeting")
        pyautogui.FAILSAFE = 0
        join("YOUR_MEETING_ID", "YOUR_MEETING_PASSWORD", exp_var2)
        break
    else:
        cprint("Not Now", 'red', attrs=['bold'], file=sys.stderr)
        cprint(current_time, 'cyan', attrs=['bold'], file=sys.stderr)
        time.sleep(10)
