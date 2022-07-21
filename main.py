from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Score Panel")
window.geometry('800x500')
window.resizable(width=0, height=0)

#Add buttons
img_arrow_up = image = ImageTk.PhotoImage(file="pict/up.jpg")
btn_up = Button(window, image=img_arrow_up, command=lambda: print('click'), relief = 'flat')
btn_up.grid(column=0, row=0)

img_arrow_down = image = ImageTk.PhotoImage(file="pict/down.jpg")
btn_down = Button(window, image=img_arrow_down, command=lambda: print('click'), relief = 'flat')
btn_down.grid(column=1, row=1)

window.mainloop()

