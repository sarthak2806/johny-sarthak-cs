from tkinter import *
first=''
last=''
def close():
    master.destroy()
def show():
    global first
    global last
    first,last=e1.get(),e2.get()
master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master, text='Enter', command=lambda:[show(),close()]).grid(row=3, column=1, sticky=W, pady=4)
name=first+' '+last
master.mainloop()