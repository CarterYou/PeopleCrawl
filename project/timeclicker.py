import time

import pyautogui
import keyboard

length = [1,50,65,55,72,47,76,76,92,68,70,66]
def getposition():
    mouseX, mouseY = pyautogui.position()
    return mouseX, mouseY
def move(x,y):
    pyautogui.move(x,y)

def click(x,y):
    pyautogui.click(x,y)

if __name__ == "__main__":
    # while True:
    #     if keyboard.read_key() == "p":
    #         print(getposition())
    #     elif keyboard.read_key() == "1":
    #         break
    for i in length:
        time.sleep(3)
        click(769,498)
        time.sleep(1)
        click(1571,922)
        time.sleep(i*60)
        print(i)


