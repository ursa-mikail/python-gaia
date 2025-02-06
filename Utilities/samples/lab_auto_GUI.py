import pyautogui, time
pyautogui.PAUSE = 1 # PyAutoGUI function call will wait N secs after performing its action. Non-PyAutoGUI instructions will not have this pause.
pyautogui.FAILSAFE = True


import datetime
import time


def type_words():
    #pyautogui.click(100, 100)
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
    #time.sleep(2)
    #pyautogui.hotkey('alt', '3')


####################################
## main
####################################
if __name__ == "__main__":
    # type_words()
    target_date = datetime.datetime(2018, 10, 31, 0, 0, 0)

    if (datetime.datetime.now() < target_date):
        time_left = target_date - datetime.datetime.now()
        print("time_left: ", time_left)
        print("days: ", time_left.days)

        print("secs: ", time_left.seconds)

"""
import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
"""

"""
im = pyautogui.screenshot()
im.save('screen_shot.png')


width, height = pyautogui.size()
print("width, height (of screen) = ", width, "\t", height)

time.sleep(5)
scroll_up_by_N_lines = 10
scroll_down_by_N_lines = -100
pyautogui.scroll(scroll_down_by_N_lines) #

# pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
# pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

import pyautogui
import pyperclip

def click():
    try:
        pyautogui.click()
    except:
        pass


pyperclip.copy('I AM HERE')
# pyautogui.moveTo(4796, 714)
# click()
# pyperclip.paste()
# pyautogui.hotkey('ctrl', 'v', interval = 0.15)
"""

"""
for i in range(10):	# move mouse
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    # relative to its current position.
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)
    x, y =pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print("position: ", positionStr)
    

pyautogui.click(10, 5)

time.sleep(5)
pyautogui.click() # click to put drawing program in focus
   distance = 200
   while distance > 0:
pyautogui.dragRel(distance, 0, duration=0.2) # drag move right
distance = distance - 5
pyautogui.dragRel(0, distance, duration=0.2) # move down
pyautogui.dragRel(-distance, 0, duration=0.2) # move left
       distance = distance - 5
       pyautogui.dragRel(0, -distance, duration=0.2)  # move up

# Hotkey Combinations

pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')

pyautogui.hotkey('ctrl', 'c')

"""

"""
moveTo(x, y) Moves the mouse cursor to the given x and y coordinates.
moveRel(xOffset, yOffset) Moves the mouse cursor relative to its current position.
dragTo(x, y) Moves the mouse cursor while the left button is held down.
dragRel(xOffset, yOffset) Moves the mouse cursor relative to its current
position while the left button is held down.
click(x, y, button) Simulates a click (left button by default).
rightClick() Simulates a right-button click.
middleClick() Simulates a middle-button click.
doubleClick() Simulates a double left-button click.
mouseDown(x, y, button) Simulates pressing down the given button at the position x, y.
mouseUp(x, y, button) Simulates releasing the given button at the position x, y.
scroll(units) Simulates the scroll wheel. A positive argument scrolls up; a negative argument scrolls down.
typewrite(message) Types the characters in the given message string.
typewrite([key1, key2, key3]) Types the given keyboard key strings.
press(key) Presses the given keyboard key string.
keyDown(key) Simulates pressing down the given keyboard key.
keyUp(key) Simulates releasing the given keyboard key.
hotkey([key1, key2, key3]) Simulates pressing the given keyboard key strings down in order and then releasing them in reverse order.
screenshot() Returns a screenshot as an Image object. 
"""