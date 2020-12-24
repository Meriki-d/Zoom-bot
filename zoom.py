import pyautogui
import subprocess
import time
import pandas as pd
from datetime import datetime as dt
import cv2


def zoom(uname, passw):
    subprocess.Popen(
        'C:\\Users\\Meriki D\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    print('done')
    time.sleep(3)
    loc = pyautogui.locateOnScreen('join.png')
    print(loc)
    pyautogui.moveTo(loc)
    pyautogui.click()
    time.sleep(4)
    # insert meeting id

    meeting = pyautogui.locateCenterOnScreen(
        'meet.png', grayscale=True, confidence=.5)
    pyautogui.moveTo(meeting)
    pyautogui.click()
    pyautogui.write(uname)

    # uncheck audio and video
    checker = pyautogui.locateAllOnScreen('checkbox.png')
    for check in checker:
        pyautogui.moveTo(check)
        pyautogui.click()
        time.sleep(1)

    # click join button
    join = pyautogui.locateCenterOnScreen('jn.png')
    print(join)
    pyautogui.moveTo(join)
    pyautogui.click()
    time.sleep(5)

    # enter password

    psw = pyautogui.locateCenterOnScreen('pass.png')
    pyautogui.moveTo(psw)
    pyautogui.click()
    pyautogui.write(passw)
    pyautogui.press('enter')


#   retrieve login details
df = pd.read_csv('logins.csv')
# print(df[df['time'] == '12:30'].iloc[0,1])
# print(type(dt.now().strftime('%H:%M')))

while True:
    currenttime = dt.now().strftime('%H:%M')
    if currenttime in list(df['time']):
        logindetails = df.loc[df['time'] == currenttime]
        loginid = str(logindetails.iloc[0, 1])
        loginpassw = str(logindetails.iloc[0, 2])
        zoom(loginid, loginpassw)
        time.sleep(60)

# zoom('9995950536', '54321')
