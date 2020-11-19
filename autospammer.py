import pyautogui
import time
from time import sleep
time.sleep(10)
f = open("beemovie",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")