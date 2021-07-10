# Numpad Mouse

This project allows you to use full mouse functionality via your numpad or number keys.

This can be useful when mouse usage is scarce (e.g. programming) or unavailable. Usage without a numpad is possible as well, but not as intuitive.

## Features 

Control your mousepointer either via:  
*  quadrant navigation   
    -------------------
    |  x  |  x  |  x  |
    -------------------   
    |  x  |  x  |  x  |
    -------------------    
    |  x  |  x  |  x  |
    -------------------
*  predetermined amount of pixels.  
* Left click  
* Right click  

## Key bindings

| Key        | Binding           
| :-------------: |:-------------| 
| \+      | Left click | 
| \.      | Right click | 
| 0      | Mode switch (quadrants and pixel toggle) | 
| \*      | Reset grid and quadrants | 
| \,     | Exit the program | 

## Future features that would be useful

* Multimonitor support
* Fix errors on mac os x
* Disabling the mouse and or overlay while still running
* Convenience features like menus and preferences

### Uses

* PyQt5 to display guidelines onscreen
* pyautogui to control the mouse pointer
* keyboard to get systemwide keyboard input regardless of window/ application focus (hooking) 

