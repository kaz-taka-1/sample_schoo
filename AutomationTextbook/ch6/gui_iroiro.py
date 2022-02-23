import PySimpleGUI as sg
from datetime import datetime

layout = [
    [sg.Text('いろいろなGUI部品を使ってみよう！')],
    [sg.OK(),sg.Cancel()],
    [sg.Text('InputText:'),sg.InputText('あいうえお')],
    [sg.Text('Checkbox:'), sg.Checkbox('チェック')],
    [sg.Text('Radio:'), sg.Radio('ラジオ',group_id='r')],
[sg.Text('Spin:'),sg.Spin([1,2,3,4,5])],
    [sg.Text('Listbox'),sg.Listbox([1,2,3,4,5]).size=(40,5)],

]