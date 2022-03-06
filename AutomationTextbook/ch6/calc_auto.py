import time, subprocess, platform
import pyautogui as pa

calc_png='clac.png'
if platform.system()=='Windows':
    app = [r'c:¥Windows¥System32¥calc.exe']