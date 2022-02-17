import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd

tk.Tk().withdraw()

name = sd.askstring(
    '名前入力', 'お名前は？',
    initialvalue='くじら')

mb.showinfo('挨拶','こんにちは' + name + 'さん')
