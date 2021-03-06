"""
A screenshot is an image of the screen's content.
The pyautogui.screenshot() will return an Image object of the screen, or you can pass it a filename to save it to a file
locateOnScreen() is passed a sample image file, and returns the coordinates of where it is on the screen.
locateCenterOnScreen() will return an (x, y) tuple of where the image is on the screen.
Combining the keyboard/mouse/screenshot functions lets you make awesome stuff!
"""


import pyautogui
import os

os.chdir("Udemy")
#pyautogui.screenshot("screenshot_example.png")
#print(pyautogui.locateOnScreen("screenshot_example_terminal.png"))

print(pyautogui.locateCenterOnScreen("screenshot_example_terminal.png"))
pyautogui.moveTo((573,755))