import time
import pyautogui as pa

pa.alert('この後５秒以内にペイントツールをアクティブにしてください。')
time.sleep(5)

bx = 400
by = 400

pa.moveTo(bx, by)
pa.dragTo(bx+300, by+300,2,button='left')
pa.dragTo(-300, 0, 2,button='left')
pa.dragTo(0, -300, 2,button='left')

sec = 0.1
for i in range(5):
    d=i*10+10
    pa.moveTo(bx+d, by+d)
    pa.dragTo(0, 300+d, sec, button='left')
    pa.dragTo(300+d, 0, sec, button='left')
    pa.dragTo(0, -300-d, sec, button='left')
    pa.dragTo(-300-d, 0, sec, button='left')