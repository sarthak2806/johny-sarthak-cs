from tkinter import *
import tkinter.ttk as ttk
win=Tk()
n=ttk.Notebook(win)
frame1=ttk.Frame(n)
frame2=ttk.Frame(n)
label_one = ttk.Label(frame1, text="We are in frame 1")
label_two = ttk.Label(frame2, text="We are in frame 2")
n.add(frame1, text="Frame One")
n.add(frame2, text="Frame Two")
n.pack(fill=BOTH, expand=1)
label_one.pack(fill=BOTH, expand=1)
label_two.pack(fill=BOTH, expand=1)
win.mainloop()