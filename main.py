from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Score Panel")
window.geometry('800x500')
window.resizable(width=0, height=0)
window['bg'] = 'azure'
img_arrow_up = ImageTk.PhotoImage(file="pict/up.png")
img_arrow_down = ImageTk.PhotoImage(file="pict/down.png")
img_start = ImageTk.PhotoImage(file="pict/start.png")
img_stop = ImageTk.PhotoImage(file="pict/stop.png")


def buttons(direction, x, y):
    if direction == 'up':
        btn_up = Button(window, image=img_arrow_up, command=lambda: print('click'), relief='flat', borderwidth=0,
                        width=60, height=44)
        btn_up.place(x=x, y=y)
    elif direction == 'down':
        btn_down = Button(window, image=img_arrow_down, command=lambda: print('click'), relief='flat', width=60,
                          borderwidth=0, height=44)
        btn_down.place(x=x, y=y)
    elif direction == 'start':
        btn_down = Button(window, image=img_start, command=lambda: print('click'), relief='flat', borderwidth=0,
                          width=80, height=80)
        btn_down.place(x=x, y=y)
    elif direction == 'stop':
        btn_down = Button(window, image=img_stop, command=lambda: print('click'), relief='flat', borderwidth=0,
                          width=80, height=68)
        btn_down.place(x=x, y=y)


#Add text input
team1 = Entry(window,width=20,bg="white", fg="blue4", justify = "center", font=("times new roman Bold", 18))
team1.insert(0,"Team 1")
team1.place(x=10,y=20)

team2 = Entry(window,width=20,bg="white", fg="blue4",justify = "center", font=("times new roman Bold", 18))
team2.insert(0,"Team 2")
team2.place(x=520,y=20)

#Add labels
lbl1 = Label(window, text="PERIOD",bg="azure", fg="blue4",font=("times new roman Bold", 18))
lbl1.place(x=358,y=345)



# Add buttons
btn_score_left_up = buttons("up", 25, 100)
btn_score_left_down = buttons("down", 25, 230)

btn_score_right_up = buttons("up", 715, 100)
btn_score_right_down = buttons("down", 715, 230)

btn_score_period_up = buttons("up", 300, 300)
btn_score_period_down = buttons("down", 450, 300)

btn_start = buttons("start", 366, 400)
# btn_stop = buttons("stop", 366, 395)


window.mainloop()
