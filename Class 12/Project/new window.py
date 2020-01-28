from tkinter import *
master = Tk() 
def command():
    master2 = Tk()
    master2.geometry("300x300")
    master2.title("New Window")
    label = Label(master2, text="This is the new window")
    label.pack()
    master2.mainloop()
newwindow = Button(master, text="Open New Window", command=lambda:[command(),master.destroy()])
newwindow.pack()
master.mainloop()