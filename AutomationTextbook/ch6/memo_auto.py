import time,subprocess, platform
import pyautogui as pa


if platform.system() == 'Darwin':
    subprocess.Popen(['open','/System/Applications/TextEdit.app'])
    time.sleep(3)
    pa.hotkey('command', 'n')
    time.sleep(3)

pa.write('Hello, Python!')

