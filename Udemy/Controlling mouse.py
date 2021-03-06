"""
Controlling the mouse and keyboard is called GUI automation.
The PyAutoGUI third-party module has many functions to control the mouse and keyboard.
pyautogui.size() returns the screen resolution, pyautogui.position() returns the mouse position. These are returned as tuples of two integers.
pyautogui.moveTo(x, y) moves the mouse to an x, y coordinate on the screen.
The mouse move is instantaneous, unless you pass an int for the "duration" keyword argument.
pyautogui.moveRel() moves the mouse relative to its current position.
PyAutoGUI's click(), doubleClick(), rightClick(), and middleClick() click the mouse buttons.
dragTo() and dragRel() will move the mouse while holding down a mouse button.
If your program gets out of control, quickly move the mouse cursor to the top-left corner to stop it.
There's more documentation at pyautogui.readthedocs.org.
"""

import pyautogui

print(pyautogui.size())

print(pyautogui.position())

#pyautogui.moveTo(500, 500, duration=2)
#pyautogui.moveRel(200, 0, duration = 2)
#pyautogui.moveRel(0, -100, duration = 2)


#pyautogui.moveTo(376, 22, duration=2)
pyautogui.click(376, 22)

pyautogui.displayMousePosition()