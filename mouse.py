import sys
import keyboard 
import pyautogui
from helper import *
from PyQt5.QtCore import QObject
from overlay import DesktopOverlay
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QMouseEvent

app = QApplication(sys.argv)

display = pyautogui.size()
_helper = helper()
_helper.change_mapping({1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8})

starting_quadrants = _helper.calculate_quadrants(display.width, display.height)
last_width = display.width
last_height = display.height
special_mode = False


def key_pressed_callback(key, overlay):
    """
    Callback function

    @param string {key} User input 
    @param DesktopOverlay {overlay} Class to enable rendering guidelines on screen
    """
    global starting_quadrants, last_width, last_height, display, special_mode, move_delta
    try:
        if key.name == ".":
            """
            LEFT Mouseclick
            """
            pyautogui.click()

        elif key.name == ",":
            """
            RESET Key to reset everything to start values
            """
            special_mode = False
            last_width = display.width
            last_height = display.height
            starting_quadrants = _helper.calculate_quadrants(
                last_width, last_height, 0, 0)
            pyautogui.moveTo(
                starting_quadrants[_helper.mapping[5]][0], starting_quadrants[_helper.mapping[5]][1])
            try:
                overlay.setQuadrants(starting_quadrants, last_width, last_height),
            except Exception as e:
                # if our overlay crashed, we should still provide mouse capability
                pass

        elif key.name == "-":
            """
            RIGHT Mouseclick
            """
            pyautogui.rightClick()

        elif key.name == "0":
            """
            SPECIAL mode switch. 
            """
            special_mode = not special_mode
        elif key.name == "esc":
            """
            EXIT
            """
            app.exit(0)
        else:
            if not special_mode:
                """
                NORMAL mode. Calculate new quadrants and show overlay
                """
                quadrant = int(key.name)

                # move mousepointer to target
                pyautogui.moveTo(
                    starting_quadrants[_helper.mapping[quadrant]][0], starting_quadrants[_helper.mapping[quadrant]][1])

                # new area to show quadrants in
                left = starting_quadrants[_helper.mapping[quadrant]][0]-(last_width//6)
                top = starting_quadrants[_helper.mapping[quadrant]][1]-(last_height//6)
                width, height = last_width//3, last_height//3
                last_width, last_height = width, height

                starting_quadrants = _helper.calculate_quadrants(
                    width, height, left=left, top=top)
                try:
                    # draws the overlay
                    overlay.setQuadrants(starting_quadrants, last_width, last_height)
                except Exception as e:
                    None
            else:
                """
                Special mode allows to move the mouse pointer for
                `delta` pixels.
                """
                quadrant = int(key.name)
                position = pyautogui.position()
                pyautogui.moveTo(
                    position.x+_helper.move_delta[_helper.mapping[quadrant]][0], position.y+_helper.move_delta[_helper.mapping[quadrant]][1], _pause=False)

    except Exception as e:
        # this is fine...
        None


if __name__ == "__main__":
    overlay = DesktopOverlay(app.primaryScreen(),_helper)
    overlay.show()
    # Register all event listeners
    for key in list(map(lambda x: str(x), list(range(1, 10))))+[".", "-", ",", "0", "esc"]:
        keyboard.on_press_key(
            key, lambda _: key_pressed_callback(_, overlay), suppress=True)


    app.exec_()