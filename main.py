from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Score Panel")
window.geometry('800x500')
window.resizable(width=0, height=0)
window['bg'] = 'white'
img_arrow_up = image = ImageTk.PhotoImage(file="pict/up.jpg")
img_arrow_down = image = ImageTk.PhotoImage(file="pict/down.jpg")
img_start = image = ImageTk.PhotoImage(file="pict/start.png")
img_stop = image = ImageTk.PhotoImage(file="pict/stop.png")

def buttons(direction, x, y):
    if direction == 'up':
        btn_up = Button(window, image=img_arrow_up, command=lambda: print('click'), relief = 'flat',borderwidth=0, width=60,  height=44)
        btn_up.place(x=x, y=y)
    elif direction == 'down':
        btn_down = Button(window, image=img_arrow_down, command=lambda: print('click'), relief = 'flat', width=60, borderwidth=0, height=44)
        btn_down.place(x=x, y=y)
    elif direction == 'start':
        btn_down = Button(window, image=img_start, command=lambda: print('click'), relief = 'flat', borderwidth=0, width=80, height=80)
        btn_down.place(x=x, y=y)
    elif direction == 'stop':
        btn_down = Button(window, image=img_stop, command=lambda: print('click'), relief = 'flat', borderwidth=0, width=80, height=68)
        btn_down.place(x=x, y=y)

#Add buttons
btn_score_left_up = buttons("up", 25, 100)
btn_score_left_down = buttons("down", 25, 230)

btn_score_right_up = buttons("up", 715, 100)
btn_score_right_down = buttons("down", 715, 230)

btn_score_left_up = buttons("up", 300, 300)
btn_score_left_down = buttons("down", 450, 300)

btn_start = buttons("start", 366, 400)
#btn_stop = buttons("stop", 366, 395)


window.mainloop()

