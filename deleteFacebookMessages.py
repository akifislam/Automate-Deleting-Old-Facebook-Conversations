# © Akif Islam | 2022 | github.com/akifislam

# This python script can run without any kind of Facebook authentication (email/password)
# This script is a GUI controlling program, so it the x_axis and y_axis value might be different according to your screen
# This is created for 'Messanger App' of Facebook running on a Macbook Air Retina 13 inch Screen and it works buttery smooth.

# AutoGUI Documentation
# 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
# 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',

import pyautogui
import time

[x,y] = [230,160] #Data generated from Cursor Method

def detect_cursor():
    time.sleep(6)
    print("Waiting to setup a position...")
    location = [pyautogui.position().x, pyautogui.position().y]
    print("Mouse position detected at : ", pyautogui.position())
    return location

def delete_message():
    pyautogui.moveTo(x, y)
    time.sleep(.2)
    pyautogui.rightClick()
    time.sleep(.2)
    pyautogui.press('up')
    time.sleep(.2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)

    #Delay might be helpful for FACEBOOK API to digest auto deletion


def main():
    time.sleep(10)
    deleteCounter = 1

    try:
        for message_thread in range(1,50):
            delete_message()
            deleteCounter+=1
    except:
        print(f"Deleted {deleteCounter} messages from your FACEBOOK MESSENGER")


if __name__ == "__main__":
    main()
# [x,y] = detect_cursor()



