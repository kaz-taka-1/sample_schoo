import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
tk.Tk().withdraw()
filepath = fd.askopenfilename(
    filetypes=[('Pythonファイル','py')],
    initialdir='./')

mb.showinfo('対象ファイル', filepath)
