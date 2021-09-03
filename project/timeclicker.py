import pyautogui
import keyboard

length = {}
def getposition():
    mouseX, mouseY = pyautogui.position()
    return mouseX, mouseY
def move(x,y):
    pyautogui.move(x,y)

def click(x,y):
    pyautogui(x,y)

if __name__ == "__main__":
    while True:
        if keyboard.read_key() == "p":
            print(getposition())
            break
