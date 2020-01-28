import tkinter
from tkinter import *
import sys
import time


root = Tk()
root.title('Logging')
Label(text='Time logging').pack(side=TOP,padx=100,pady=100)

entry = Entry(root, width=25)
entry.pack(side=TOP,padx=25,pady=25)

def onok():
    x, y = entry.get().split('x')
    for row in range(int(y)):
        for col in range(int(x)):
            print((col, row))

Button(root, text='Log Time', command=onok).pack(side=LEFT)
Button(root, text='CLOSE').pack(side= RIGHT)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)