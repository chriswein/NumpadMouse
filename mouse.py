from platform import python_branch
from PyQt5.QtCore import QObject
import keyboard  # using module keyboard
from dis import dis
import pyautogui
from overlay import DesktopOverlay
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QMouseEvent
from PyQt5 import *

display = pyautogui.size()

class KeyPressEater(QObject):

    # subclassing for eventFilter


    def eventFilter(self, obj, event):
        if isinstance(event,QMouseEvent):
            print("MAUS")
            return True
        return False

app = QApplication(sys.argv)
eater = KeyPressEater()
app.installEventFilter(eater)
overlay = DesktopOverlay(app.primaryScreen())
overlay.show()

def calculate_quadrants(width, height, left=0, top=0):
    return [
        [left+width//6, top+height//6],
        [left+3*width//6, top+height//6],
        [left+5*width//6, top+height//6],
        [left+width//6, top+3*height//6],
        [left+3*width//6, top+3*height//6],
        [left+5*width//6, top+3*height//6],
        [left+width//6, top+5*height//6],
        [left+3*width//6, top+5*height//6],
        [left+5*width//6, top+5*height//6],
    ]


delta = 20
move_delta = [
    [-delta, -delta],
    [0, -delta],
    [delta, -delta],
    [-delta, 0],
    [0, 0],
    [delta, 0],
    [-delta, delta],
    [0, delta],
    [delta, delta],
]

starting_quadrants = calculate_quadrants(display.width, display.height)
last_width = display.width
last_height = display.height
special_mode = False

mapping = { 1: 6, 2: 7, 3: 8, 4: 3, 5: 4, 6: 5, 7: 0, 8: 1, 9: 2}

def key_pressed_callback(key):
    global starting_quadrants, last_width, last_height, display, special_mode, move_delta
    try:
        if key.name == "+":
            pyautogui.click()
        elif key.name == "*":
            special_mode = False
            last_width = display.width
            last_height = display.height
            starting_quadrants = calculate_quadrants(
                last_width, last_height, 0, 0)
            pyautogui.moveTo(
                    starting_quadrants[mapping[5]][0], starting_quadrants[mapping[5]][1])
            try:
                    overlay.setQuadrants(starting_quadrants)
            except Exception as e:
                    print(e)
        elif key.name == "0":
            special_mode = not special_mode
            print(special_mode)
        else:
            if not special_mode:
                quadrant = int(key.name)
                pyautogui.moveTo(
                    starting_quadrants[mapping[quadrant]][0], starting_quadrants[mapping[quadrant]][1])
                left = starting_quadrants[mapping[quadrant]][0]-(last_width//6)
                top = starting_quadrants[mapping[quadrant]][1]-(last_height//6)
                width = last_width//3
                height = last_height//3
                last_width = width
                last_height = height
                starting_quadrants = calculate_quadrants(width, height, left=left, top=top)
                try:
                    overlay.setQuadrants(starting_quadrants)
                except Exception as e:
                    print(e)
            else:
                quadrant = int(key.name)
                position = pyautogui.position()
                pyautogui.moveTo(
                    position.x+move_delta[mapping[quadrant]][0], position.y+move_delta[mapping[quadrant]][1],_pause=False)

    except Exception as e:
        print(e)
    print(key)


keyboard.on_press_key("1", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("2", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("3", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("4", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("5", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("6", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("7", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("8", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("9", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("+", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("*", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("0", lambda _: key_pressed_callback(_), suppress=True)
keyboard.on_press_key("enter", lambda _: sys.exit(), suppress=True)

app.exec_()
keyboard.wait()