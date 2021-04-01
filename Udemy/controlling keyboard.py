"""
PyAutoGUI's virtual key presses will go the window the currently has focus.
typewrite() can be passed a string of characters to type. It also has an "interval" keyword argument.
Passing a list of strings to typewrite() lets you use hard-to-type keyboard keys, like ‘shift' or ‘f1'.
These keyboard key strings are in the pyautogui.KEYBOARD_KEYS list.
pyautogui.press() will press a single key.
pyautogui.hotkey() can be used for keyboard shortcuts, like Ctrl-O.
"""

import pyautogui

pyautogui.click(500,500)
pyautogui.write("Hello World", interval = 0.2)
pyautogui.write(["a", "b", "left", "left", "l", "X"], interval = 0.2)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.press("f1")
pyautogui.hotkey("ctrl", "s")