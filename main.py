from tkinter import *
import datetime
import time
from time import strftime
import sys
import os

window = Tk()
window.title("Score Panel")
window.geometry('815x500')
window.resizable(width=0, height=0)
# window['bg'] = '#404040'


#C = Canvas(window, bg="blue", height=815, width=500)
fon = PhotoImage(file="pict/layer.png")
background_label = Label(window, image=fon)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#C.pack()

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Bullits")

mainmenu.add_cascade(label="Game", menu=filemenu)

#Define variables
score_team1 = 0
score_team2 = 0
period = 1
main_timer = 0

#Score team left
def nClick_score_left_up():
    global score_team1
    score_team1 += 1
    lbl_score_left.config(text=score_team1)
def nClick_score_left_down():
    global score_team1
    score_team1 -= 1
    if score_team1 < 0:
        score_team1 = 0
    lbl_score_left.config(text=score_team1)

btn_score_left_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_score_left_up, relief='flat', borderwidth=0)
btn_score_left_up.place(x=60, y=80, width=40, height=40)
btn_score_left_down = Button(window, text="-", font=("digital numbers", 30), command=nClick_score_left_down, relief='flat', borderwidth=0)
btn_score_left_down.place(x=60, y=280, width=40, height=40)

lbl_score_left = Label(window, text="00", bg="black", fg="#feba00", font=("digital numbers", 75))
lbl_score_left.place(x=5, y=130, width=150, height=140)


#Score team right
def nClick_score_right_up():
    global score_team2
    score_team2 += 1
    lbl_score_right.config(text=score_team2)
def nClick_score_right_down():
    global score_team2
    score_team2 -= 1
    if score_team2 < 0:
        score_team2 = 0
    lbl_score_right.config(text=score_team2)

btn_score_left_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_score_right_up, relief='flat', borderwidth=0)
btn_score_left_up.place(x=715, y=80, width=40, height=40)
btn_score_left_down = Button(window, text="-", font=("digital numbers", 30), command=nClick_score_right_down, relief='flat', borderwidth=0)
btn_score_left_down.place(x=715, y=280, width=40, height=40)

lbl_score_right = Label(window, text="00", bg="black", fg="#feba00", font=("digital numbers", 75))
lbl_score_right.place(x=660, y=130, width=150, height=140)


#Game Period
def nClick_period_up():
    global period
    period += 1
    lbl_period.config(text=period)
def nClick_period_down():
    global period
    period -= 1
    if period < 0:
        period = 0
    lbl_period.config(text=period)

btn_score_left_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_period_up, relief='flat', borderwidth=0)
btn_score_left_up.place(x=450, y=400, width=40, height=40)
btn_score_left_down = Button(window, text="-", font=("digital numbers", 30), command=nClick_period_down, relief='flat', borderwidth=0)
btn_score_left_down.place(x=320, y=400, width=40, height=40)

lbl_period_name = Label(window, text="Period", bg="#404040", fg="white", font=("square sans serif 7", 24))
lbl_period_name.place(x=340, y=460)

lbl_period = Label(window, text="1", bg="black", fg="#03bd02", font=("digital numbers", 60))
lbl_period.place(x=367, y=360, width=75, height=100)


#Penalty Team Left
def penalty_left_first():
    pass
def penalty_left_second():
    pass

btn_penalty_left_first = Button(window, text="START", font=("square sans serif 7", 15), command=lambda: print('click'),
                     relief='flat', bg='black', fg='#03bd02', borderwidth=0)
btn_penalty_left_first.place(x=130, y=370)
btn_penalty_left_second = Button(window, text="START", font=("square sans serif 7", 15), command=lambda: print('click'),
                     relief='flat', bg='black', fg='#03bd02', borderwidth=0)
btn_penalty_left_second.place(x=130, y=420)

lbl_penalty_name_left = Label(window, text="Penalty", bg="#404040", fg="white", font=("square sans serif 7", 20))
lbl_penalty_name_left.place(x=45, y=460)

lbl_penalty_left1 = Label(window, text="02:00", bg="black", fg="#feba00", font=("digital numbers", 20))
lbl_penalty_left1.place(x=10, y=360)

lbl_penalty_left2 = Label(window, text="02:00", bg="black", fg="#feba00", font=("digital numbers", 20))
lbl_penalty_left2.place(x=10, y=410)

#Penalty Team Right
def penalty_right_first():
    pass
def penalty_right_second():
    pass

btn_penalty_right_first = Button(window, text="START", font=("square sans serif 7", 15), command=lambda: print('click'),
                     relief='flat', bg='black', fg='#03bd02', borderwidth=0)
btn_penalty_right_first.place(x=580, y=370)

btn_penalty_right_second = Button(window, text="START", font=("square sans serif 7", 15), command=lambda: print('click'),
                     relief='flat', bg='black', fg='#03bd02', borderwidth=0)
btn_penalty_right_second.place(x=580, y=420)

lbl_penalty_name_right = Label(window, text="Penalty", bg="#404040", fg="white", font=("square sans serif 7", 20))
lbl_penalty_name_right.place(x=615, y=460)

lbl_penalty_right1 = Label(window, text="02:00", bg="black", fg="#feba00", font=("digital numbers", 20))
lbl_penalty_right1.place(x=688, y=360)

lbl_penalty_right2 = Label(window, text="02:00", bg="black", fg="#feba00", font=("digital numbers", 20))
lbl_penalty_right2.place(x=688, y=410)

#Timer
def nClick_minutes_up():
    global main_timer
    main_timer += 1
    lbl_timer.config(text=main_timer)
def nClick_minutes_down():
    global main_timer
    main_timer -= 1
    if main_timer < 0:
        main_timer = 0
    lbl_timer.config(text=main_timer)

btn_minutes_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_minutes_up, relief='flat', borderwidth=0)
btn_minutes_up.place(x=305, y=180, width=40, height=40)
btn_minutes_down = Button(window, text="-", font=("digital numbers", 30), command=nClick_minutes_down, relief='flat', borderwidth=0)
btn_minutes_down.place(x=275, y=180, width=40, height=40)

def nClick_seconds_up():
    global main_timer
    main_timer += 1
    lbl_timer.config(text=main_timer)
def nClick_seconds_down():
    global main_timer
    main_timer -= 1
    if main_timer < 0:
        main_timer = 0
    lbl_timer.config(text=main_timer)

btn_seconds_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_seconds_up, relief='flat', borderwidth=0)
btn_seconds_up.place(x=500, y=180, width=40, height=40)
btn_seconds_down = Button(window, text="-", font=("digital numbers", 30), command=nClick_seconds_down, relief='flat', borderwidth=0)
btn_seconds_down.place(x=470, y=180, width=40, height=40)

lbl_timer = Label(window, text=main_timer, bg="black", fg="#fe0000", font=("digital numbers", 60))
lbl_timer.place(x=250, y=70, width=320, height=100)


#Reset main timer
def reset_main_timer():
    pass

btn_reset_main_timer = Button(window, text="RESET TIMER", font=("square sans serif 7", 17), command=lambda: print('click'),relief='flat',
                     bg='black', fg='#00fffe', borderwidth=0)
btn_reset_main_timer.place(x=220, y=290)


#New game
def new_game():
    pass
    '''global score_team1
    score_team1 = 0
    global score_team2
    score_team2 = 0
    global period
    period = 1
    global main_timer
    main_timer = 0'''


btn_new_game = Button(window, text="NEW GAME", font=("square sans serif 7", 17), command=new_game, relief='flat',
                     bg='black', fg='#00fffe', borderwidth=0)
btn_new_game.place(x=460, y=290)




#Start_Pause Main Timer
def update_main_timer():
    global main_timer
    if main_timer >= 0:
        m, s = divmod(main_timer, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        main_timer = main_timer - 1
        lbl_timer.config(text=min_sec_format)

        window.after(1000, update_main_timer)


def start_main_timer(timer=3):
    global main_timer
    m, s = divmod(main_timer, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    main_timer = timer
    lbl_timer.config(text=min_sec_format)

    window.after(1000, update_main_timer)

btn_start_main_timer = Button(window, text="START/PAUSE", font=("square sans serif 7", 20), command=lambda: start_main_timer(10),
                     relief='flat', bg='black', fg='#fe0000', borderwidth=0)
btn_start_main_timer.place(x=275, y=230)


# Add radiobuttons default period time
var = IntVar()
var.set(20)
rad1 = Radiobutton(window, text='05:00', value=5, variable=var, bg="#404040", fg="#feba00", selectcolor='black', font=("arial", 12))
rad2 = Radiobutton(window, text='10:00', value=10, variable=var, bg="#404040", fg="#feba00", selectcolor='black', font=("arial", 12))
rad3 = Radiobutton(window, text='15:00', value=15, variable=var, bg="#404040", fg="#feba00", selectcolor='black', font=("arial", 12))
rad4 = Radiobutton(window, text='20:00', value=20, variable=var, bg="#404040", fg="#feba00", selectcolor='black', font=("arial", 12))
rad1.place(x=175, y=70)
rad2.place(x=175, y=95)
rad3.place(x=175, y=120)
rad4.place(x=175, y=145)

# Add text input
team1 = Entry(window, width=20, bg="black", fg="#feba00", justify="center", font=("square sans serif 7", 20))
team1.insert(0, "TEAM 1")
team1.place(x=5, y=20, width=380, height=40)

team2 = Entry(window, width=20, bg="black", fg="#feba00", justify="center", font=("square sans serif 7", 20))
team2.insert(0, "TEAM 2")
team2.place(x=428, y=20, width=380, height=40)


window.mainloop()
