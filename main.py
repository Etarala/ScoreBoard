from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Score Panel")
window.geometry('815x500')
window.resizable(width=0, height=0)
window['bg'] = '#404040'
img_arrow_up = ImageTk.PhotoImage(file="pict/up.jpg")
img_arrow_down = ImageTk.PhotoImage(file="pict/down.jpg")
img_start = ImageTk.PhotoImage(file="pict/start.png")
img_stop = ImageTk.PhotoImage(file="pict/stop.png")


def buttons(direction, x, y):
    if direction == 'up':
        btn = Button(window, text="+", font=("digital numbers", 30), command=lambda: print('click'), relief='flat',
                          borderwidth=0)
        btn.place(x=x, y=y, width=40,height=40)
    elif direction == 'down':
        btn = Button(window, text="-", font=("digital numbers", 30), command=lambda: print('click'), relief='flat',
                          borderwidth=0)
        btn.place(x=x, y=y, width=40,height=40)
    elif direction == 'start':
        btn = Button(window, text="START/PAUSE", font=("square sans serif 7", 20), command=lambda: print('click'), relief='flat',
                          bg='black',fg='#fe0000', borderwidth=0)
        btn.place(x=x, y=y)
    elif direction == 'penalty':
        btn = Button(window, text="START", font=("square sans serif 7", 15), command=lambda: print('click'),
                          relief='flat', bg='black', fg='#03bd02', borderwidth=0)
        btn.place(x=x, y=y)


#Add text input
team1 = Entry(window,width=20,bg="black", fg="#feba00", justify = "center", font=("square sans serif 7", 20))
team1.insert(0,"TEAM 1")
team1.place(x=5,y=20, width=380,height=40)

team2 = Entry(window,width=20,bg="black", fg="#feba00",justify = "center", font=("square sans serif 7", 20))
team2.insert(0,"TEAM 2")
team2.place(x=428,y=20, width=380,height=40)

#Add labels
lbl_period_name = Label(window, text="Period",bg="#404040", fg="white",font=("square sans serif 7", 24))
lbl_period_name.place(x=340,y=400)

lbl_score_left = Label(window, text="00",bg="black", fg="#feba00",font=("digital numbers", 75))
lbl_score_left.place(x=5,y=130, width=150,height=140)

lbl_score_right = Label(window, text="00",bg="black", fg="#feba00",font=("digital numbers", 75))
lbl_score_right.place(x=660,y=130, width=150,height=140)

lbl_period = Label(window, text="1",bg="black", fg="#03bd02",font=("digital numbers", 60))
lbl_period.place(x=367,y=301, width=75,height=100)

lbl_timer = Label(window, text="20:00",bg="black", fg="#fe0000",font=("digital numbers", 60))
lbl_timer.place(x=250,y=70, width=320,height=100)

lbl_penalty_name_left = Label(window, text="Penalty",bg="#404040", fg="white",font=("square sans serif 7", 20))
lbl_penalty_name_left.place(x=10,y=460)

lbl_penalty_name_right = Label(window, text="Penalty",bg="#404040", fg="white",font=("square sans serif 7", 20))
lbl_penalty_name_right.place(x=650,y=460)

lbl_penalty_left1 = Label(window, text="02:00",bg="black", fg="#feba00",font=("digital numbers", 20))
lbl_penalty_left1.place(x=10,y=360)

lbl_penalty_left2 = Label(window, text="02:00",bg="black", fg="#feba00",font=("digital numbers", 20))
lbl_penalty_left2.place(x=10,y=410)

lbl_penalty_right1 = Label(window, text="02:00",bg="black", fg="#feba00",font=("digital numbers", 20))
lbl_penalty_right1.place(x=688,y=360)

lbl_penalty_right2 = Label(window, text="02:00",bg="black", fg="#feba00",font=("digital numbers", 20))
lbl_penalty_right2.place(x=688,y=410)

# Add buttons
btn_score_left_up = buttons("up", 60, 80)
btn_score_left_down = buttons("down", 60, 280)

btn_score_right_up = buttons("up", 715, 80)
btn_score_right_down = buttons("down", 715, 280)

btn_score_period_up = buttons("up", 450, 360)
btn_score_period_down = buttons("down", 320, 360)

btn_penalty_left_start1 = buttons("penalty", 130, 370)
btn_penalty_left_start2 = buttons("penalty", 130, 420)

btn_penalty_right_start1 = buttons("penalty", 580, 370)
btn_penalty_right_start2 = buttons("penalty", 580, 420)

btn_start = buttons("start", 278, 435)
# btn_stop = buttons("stop", 366, 395)


window.mainloop()
