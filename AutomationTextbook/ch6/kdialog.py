import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import tkinter.simpledialog as sd

tk.Tk().withdraw()

def info(message, title='情報'):
    mb.showinfo(title, message)

def warning(message, title='情報'):
    mb.showwarning(title, message)

def yesno(message, title='質問'):
    return mb.askyesno(title, message)

def input(message, title='質問', value=''):
    return sd.askstring(
        title,message,
        initialvalue=value)


def select_file(initdir='./'):
    return fd.askopenfilename(
        initialdir=initdir)

def select_savefile(initdir='./'):
    return fd.asksaveasfilename(
        initialdir=initdir)

def select_dir(initdir='./'):
    return fd.askdirectory(
        initialdir=initdir)

import kdialog as kd
name = kd.input('お名前は？')
if not kd.yesno(name+'さん、実行しますか？'):
    kd.info('中止しました')
    quit()

kd.info('対象ファイルを選んでください。')
fname = kd.select_file()
kd.info('選択:'+fname)