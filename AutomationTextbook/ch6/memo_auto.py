import time,subprocess, platform
import pyautogui as pa


if platform.system() == 'Darwin':
    subprocess.Popen(['open','/System/Applications/TextEdit.app'])
    time.sleep(2)
    pa.hotkey('command', 'n')
    time.sleep(2)

pa.write('Hello, Python!')

