import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

tk.Tk().withdraw()

dirpath = fd.askdirectory(
    title='実行するフォルダを指定してください',
    initialdir='./'
)

mb.showinfo('対象フォルダ',dirpath)