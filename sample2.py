from tkinter import *

root = Tk()
root.geometry("200x200")
root.title("My Button Increaser")

global counter
counter = 0

def nClick():
    global counter
    counter += 1
    mButton1.config(text = counter)

mButton1 = Button(text = counter, command = nClick, fg = "darkgreen", bg = "white")
mButton1.pack()

root.mainloop()