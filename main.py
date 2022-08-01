from tkinter import *
import codecs
import pyglet
from global_hotkeys import *

window = Tk()
window.title("Score Panel")
window.geometry('815x500')
window.resizable(width=0, height=0)

background = PhotoImage(file="pict/layer.png")
background_label = Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

mainmenu = Menu(window)
window.config(menu=mainmenu)

pyglet.font.add_file('fonts/Digital Numbers.ttf')
pyglet.font.add_file("fonts/square sans serif 7.ttf")

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Bullits")

mainmenu.add_cascade(label="Game", menu=filemenu)

# Define variables
score_team1 = 0
score_team2 = 0
period = 1
period_time = 0
penalty_left_first_time = 120
penalty_left_second_time = 120
penalty_right_first_time = 120
penalty_right_second_time = 120
game_started = False
paused_main_timer = False
penalty_left_first_started = False
penalty_left_first_paused = True
penalty_left_second_started = False
penalty_left_second_paused = True
penalty_right_first_started = False
penalty_right_first_paused = True
penalty_right_second_started = False
penalty_right_second_paused = True
write_files = True
team1_write = ""
team2_write = ""


# Score team left
def nClick_score_left_up():
    global score_team1
    score_team1 += 1
    lbl_score_left.config(text=score_team1)
    with open("output/score_team1.txt", "w") as file:
        file.write(str(score_team1))


def nClick_score_left_down():
    global score_team1
    score_team1 -= 1
    if score_team1 < 0:
        score_team1 = 0
    lbl_score_left.config(text=score_team1)
    with open("output/score_team1.txt", "w") as file:
        file.write(str(score_team1))


btn_score_left_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_score_left_up, relief='flat',
                           borderwidth=0)
btn_score_left_up.place(x=60, y=80, width=40, height=40)
btn_score_left_down = Button(window, text="-", font=("digital numbers", 30), command=nClick_score_left_down,
                             relief='flat', borderwidth=0)
btn_score_left_down.place(x=60, y=280, width=40, height=40)

lbl_score_left = Label(window, text="00", bg="black", fg="#feba00", font=("digital numbers", 75))
lbl_score_left.place(x=5, y=130, width=150, height=140)


# Score team right
def nClick_score_right_up():
    global score_team2
    score_team2 += 1
    lbl_score_right.config(text=score_team2)
    with open("output/score_team2.txt", "w") as file:
        file.write(str(score_team2))


def nClick_score_right_down():
    global score_team2
    score_team2 -= 1
    if score_team2 < 0:
        score_team2 = 0
    lbl_score_right.config(text=score_team2)
    with open("output/score_team2.txt", "w") as file:
        file.write(str(score_team2))


btn_score_left_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_score_right_up, relief='flat',
                           borderwidth=0)
btn_score_left_up.place(x=715, y=80, width=40, height=40)
btn_score_left_down = Button(window, text="-", font=("digital numbers", 30), command=nClick_score_right_down,
                             relief='flat', borderwidth=0)
btn_score_left_down.place(x=715, y=280, width=40, height=40)

lbl_score_right = Label(window, text="00", bg="black", fg="#feba00", font=("digital numbers", 75))
lbl_score_right.place(x=660, y=130, width=150, height=140)


# Game Period
def nClick_period_up():
    global period
    period += 1
    lbl_period.config(text=period)
    with open("output/period.txt", "w") as file:
        file.write(str(period))


def nClick_period_down():
    global period
    period -= 1
    if period < 0:
        period = 0
    lbl_period.config(text=period)
    with open("output/period.txt", "w") as file:
        file.write(str(period))


btn_score_left_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_period_up, relief='flat',
                           borderwidth=0)
btn_score_left_up.place(x=450, y=400, width=40, height=40)
btn_score_left_down = Button(window, text="-", font=("digital numbers", 30), command=nClick_period_down, relief='flat',
                             borderwidth=0)
btn_score_left_down.place(x=320, y=400, width=40, height=40)

lbl_period_name = Label(window, text="Period", bg="#404040", fg="white", font=("square sans serif 7", 24))
lbl_period_name.place(x=340, y=460)

lbl_period = Label(window, text="1", bg="black", fg="#03bd02", font=("digital numbers", 60))
lbl_period.place(x=367, y=360, width=75, height=100)


# Penalty Team Left
def update_penalty_left_first_timer():
    global penalty_left_first_time
    global paused_main_timer
    global penalty_left_first_started
    if not paused_main_timer and penalty_left_first_started:
        penalty_left_first_time = penalty_left_first_time - 1
        if penalty_left_first_time >= 0:
            m, s = divmod(penalty_left_first_time, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            lbl_penalty_left1.config(text=min_sec_format)
            window.after(1000, update_penalty_left_first_timer)
            with open("output/penalty_left_first.txt", "w") as file:
                file.write(str(min_sec_format))


def chk_penalty_left_first():
    check1left = chk_penalty_left_first_state.get()
    global penalty_left_first_started
    global penalty_left_first_paused
    penalty_left_first_started = check1left
    penalty_left_first_paused = not penalty_left_first_started


chk_penalty_left_first_state = BooleanVar()
chk_penalty_left_first_state.set(False)
chk_penalty_left_first_btn = Checkbutton(window, text='', var=chk_penalty_left_first_state,
                                         command=chk_penalty_left_first, bg="#404040", fg="#03bd02",
                                         selectcolor='black', activebackground="#404040",
                                         font=("square sans serif 7", 25))
chk_penalty_left_first_btn.place(x=130, y=360)


def nClick_penalty_left_first_minutes_up():
    global penalty_left_first_time
    penalty_left_first_time += 60
    m, s = divmod(penalty_left_first_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_left1.config(text=min_sec_format)


def nClick_penalty_left_first_minutes_down():
    global penalty_left_first_time
    penalty_left_first_time -= 60
    if penalty_left_first_time < 0:
        penalty_left_first_time = 0
    m, s = divmod(penalty_left_first_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_left1.config(text=min_sec_format)


btn_penalty_left_first_up = Button(window, text="+", font=("digital numbers", 22),
                                   command=nClick_penalty_left_first_minutes_up,
                                   relief='flat', borderwidth=0)
btn_penalty_left_first_up.place(x=208, y=365, width=35, height=35)
btn_penalty_left_first_down = Button(window, text="-", font=("digital numbers", 22),
                                     command=nClick_penalty_left_first_minutes_down,
                                     relief='flat', borderwidth=0)
btn_penalty_left_first_down.place(x=173, y=365, width=35, height=35)


def update_penalty_left_second_timer():
    global penalty_left_second_time
    global paused_main_timer
    global penalty_left_second_started
    if not paused_main_timer and penalty_left_second_started:
        penalty_left_second_time = penalty_left_second_time - 1
        if penalty_left_second_time >= 0:
            m, s = divmod(penalty_left_second_time, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            lbl_penalty_left2.config(text=min_sec_format)
            window.after(1000, update_penalty_left_second_timer)
            with open("output/penalty_left_second.txt", "w") as file:
                file.write(str(min_sec_format))


def chk_penalty_left_second():
    check2left = chk_penalty_left_second_state.get()
    global penalty_left_second_started
    global penalty_left_second_paused
    penalty_left_second_started = check2left
    penalty_left_second_paused = not penalty_left_second_started


chk_penalty_left_second_state = BooleanVar()
chk_penalty_left_second_state.set(False)
chk_penalty_left_second_btn = Checkbutton(window, text='', var=chk_penalty_left_second_state,
                                          command=chk_penalty_left_second, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
chk_penalty_left_second_btn.place(x=130, y=410)


def nClick_penalty_left_second_minutes_up():
    global penalty_left_second_time
    penalty_left_second_time += 60
    m, s = divmod(penalty_left_second_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_left2.config(text=min_sec_format)


def nClick_penalty_left_second_minutes_down():
    global penalty_left_second_time
    penalty_left_second_time -= 60
    if penalty_left_second_time < 0:
        penalty_left_second_time = 0
    m, s = divmod(penalty_left_second_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_left2.config(text=min_sec_format)


btn_penalty_left_second_up = Button(window, text="+", font=("digital numbers", 22),
                                    command=nClick_penalty_left_second_minutes_up,
                                    relief='flat', borderwidth=0)
btn_penalty_left_second_up.place(x=208, y=414, width=35, height=35)
btn_penalty_left_second_down = Button(window, text="-", font=("digital numbers", 22),
                                      command=nClick_penalty_left_second_minutes_down,
                                      relief='flat', borderwidth=0)
btn_penalty_left_second_down.place(x=173, y=414, width=35, height=35)

lbl_penalty_left1 = Label(window, text="02:00", bg="black", fg="#feba00", font=("digital numbers", 20))
lbl_penalty_left1.place(x=10, y=360)

lbl_penalty_left2 = Label(window, text="02:00", bg="black", fg="#feba00", font=("digital numbers", 20))
lbl_penalty_left2.place(x=10, y=410)

lbl_penalty_name_left = Label(window, text="Penalty", bg="#404040", fg="white", font=("square sans serif 7", 20))
lbl_penalty_name_left.place(x=45, y=460)


# Penalty Team Right

def update_penalty_right_first_timer():
    global penalty_right_first_time
    global paused_main_timer
    global penalty_right_first_started
    if not paused_main_timer and penalty_right_first_started:
        penalty_right_first_time = penalty_right_first_time - 1
        if penalty_right_first_time >= 0:
            m, s = divmod(penalty_right_first_time, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            lbl_penalty_right1.config(text=min_sec_format)
            window.after(1000, update_penalty_right_first_timer)
            with open("output/penalty_right_first.txt", "w") as file:
                file.write(str(min_sec_format))


def chk_penalty_right_first():
    check1right = chk_penalty_right_first_state.get()
    global penalty_right_first_started
    global penalty_right_first_paused
    penalty_right_first_started = check1right
    penalty_right_first_paused = not penalty_right_first_started


chk_penalty_right_first_state = BooleanVar()
chk_penalty_right_first_state.set(False)
chk_penalty_right_first_btn = Checkbutton(window, text='', var=chk_penalty_right_first_state,
                                          command=chk_penalty_right_first, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
chk_penalty_right_first_btn.place(x=660, y=360)


def nClick_penalty_right_first_minutes_up():
    global penalty_right_first_time
    penalty_right_first_time += 60
    m, s = divmod(penalty_right_first_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_right1.config(text=min_sec_format)


def nClick_penalty_right_first_minutes_down():
    global penalty_right_first_time
    penalty_right_first_time -= 60
    if penalty_right_first_time < 0:
        penalty_right_first_time = 0
    m, s = divmod(penalty_right_first_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_right1.config(text=min_sec_format)


btn_penalty_right_first_up = Button(window, text="+", font=("digital numbers", 22),
                                    command=nClick_penalty_right_first_minutes_up,
                                    relief='flat', borderwidth=0)
btn_penalty_right_first_up.place(x=607, y=365, width=35, height=35)
btn_penalty_right_first_down = Button(window, text="-", font=("digital numbers", 22),
                                      command=nClick_penalty_right_first_minutes_down,
                                      relief='flat', borderwidth=0)
btn_penalty_right_first_down.place(x=573, y=365, width=35, height=35)


def update_penalty_right_second_timer():
    global penalty_right_second_time
    global paused_main_timer
    global penalty_right_second_started
    if not paused_main_timer and penalty_right_second_started:
        penalty_right_second_time = penalty_right_second_time - 1
        if penalty_right_second_time >= 0:
            m, s = divmod(penalty_right_second_time, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            lbl_penalty_right2.config(text=min_sec_format)
            window.after(1000, update_penalty_right_second_timer)
            with open("output/penalty_right_second.txt", "w") as file:
                file.write(str(min_sec_format))


def chk_penalty_right_second():
    check2right = chk_penalty_right_second_state.get()
    global penalty_right_second_started
    global penalty_right_second_paused
    penalty_right_second_started = check2right
    penalty_right_second_paused = not penalty_right_second_started


chk_penalty_right_second_state = BooleanVar()
chk_penalty_right_second_state.set(False)
chk_penalty_right_second_btn = Checkbutton(window, text='', var=chk_penalty_right_second_state,
                                           command=chk_penalty_right_second, bg="#404040", fg="#03bd02",
                                           activebackground="#404040", selectcolor='black',
                                           font=("square sans serif 7", 25))
chk_penalty_right_second_btn.place(x=660, y=410)


def nClick_penalty_right_second_minutes_up():
    global penalty_right_second_time
    penalty_right_second_time += 60
    m, s = divmod(penalty_right_second_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_right2.config(text=min_sec_format)


def nClick_penalty_right_second_minutes_down():
    global penalty_right_second_time
    penalty_right_second_time -= 60
    if penalty_right_second_time < 0:
        penalty_right_second_time = 0
    m, s = divmod(penalty_right_second_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_right2.config(text=min_sec_format)


btn_penalty_right_second_up = Button(window, text="+", font=("digital numbers", 22),
                                     command=nClick_penalty_right_second_minutes_up,
                                     relief='flat', borderwidth=0)
btn_penalty_right_second_up.place(x=607, y=414, width=35, height=35)
btn_penalty_right_second_down = Button(window, text="-", font=("digital numbers", 22),
                                       command=nClick_penalty_right_second_minutes_down,
                                       relief='flat', borderwidth=0)
btn_penalty_right_second_down.place(x=573, y=414, width=35, height=35)

lbl_penalty_right1 = Label(window, text="02:00", bg="black", fg="#feba00", font=("digital numbers", 20))
lbl_penalty_right1.place(x=688, y=360)

lbl_penalty_right2 = Label(window, text="02:00", bg="black", fg="#feba00", font=("digital numbers", 20))
lbl_penalty_right2.place(x=688, y=410)

lbl_penalty_name_right = Label(window, text="Penalty", bg="#404040", fg="white", font=("square sans serif 7", 20))
lbl_penalty_name_right.place(x=615, y=460)


# Main Timer
def nClick_minutes_up():
    global period_time
    period_time += 60
    m, s = divmod(period_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_timer.config(text=min_sec_format)


def nClick_minutes_down():
    global period_time
    period_time -= 60
    if period_time < 0:
        period_time = 0
    m, s = divmod(period_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_timer.config(text=min_sec_format)


btn_minutes_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_minutes_up, relief='flat',
                        borderwidth=0)
btn_minutes_up.place(x=305, y=180, width=40, height=40)
btn_minutes_down = Button(window, text="-", font=("digital numbers", 30), command=nClick_minutes_down, relief='flat',
                          borderwidth=0)
btn_minutes_down.place(x=275, y=180, width=40, height=40)


def nClick_seconds_up():
    global period_time
    period_time += 1
    m, s = divmod(period_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_timer.config(text=min_sec_format)


def nClick_seconds_down():
    global period_time
    period_time -= 1
    if period_time < 0:
        period_time = 0
    m, s = divmod(period_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_timer.config(text=min_sec_format)


btn_seconds_up = Button(window, text="+", font=("digital numbers", 30), command=nClick_seconds_up, relief='flat',
                        borderwidth=0)
btn_seconds_up.place(x=500, y=180, width=40, height=40)
btn_seconds_down = Button(window, text="-", font=("digital numbers", 30), command=nClick_seconds_down, relief='flat',
                          borderwidth=0)
btn_seconds_down.place(x=470, y=180, width=40, height=40)

lbl_timer = Label(window, text=period_time, bg="black", fg="#fe0000", font=("digital numbers", 60))
lbl_timer.place(x=250, y=70, width=320, height=100)


# Reset timers
def reset_main_timer():
    global period_time
    global paused_main_timer
    global game_started
    global penalty_left_first_time
    global penalty_left_second_time
    global penalty_right_first_time
    global penalty_right_second_time
    global penalty_left_first_paused
    global penalty_left_second_paused
    global penalty_right_first_paused
    global penalty_right_second_paused
    global penalty_left_first_started
    global penalty_left_second_started
    global penalty_right_first_started
    global penalty_right_second_started
    period_time = 0
    lbl_timer.config(text="00:00")
    var.set(0)
    game_started = False
    paused_main_timer = False
    btn_pause_main_timer.config(bg='black')
    penalty_left_first_time = 120
    penalty_left_second_time = 120
    penalty_right_first_time = 120
    penalty_right_second_time = 120
    lbl_penalty_left1.config(text="02:00")
    lbl_penalty_left2.config(text="02:00")
    lbl_penalty_right1.config(text="02:00")
    lbl_penalty_right2.config(text="02:00")
    chk_penalty_left_first_state.set(False)
    chk_penalty_left_second_state.set(False)
    chk_penalty_right_first_state.set(False)
    chk_penalty_right_second_state.set(False)
    penalty_left_first_paused = True
    penalty_left_second_paused = True
    penalty_right_first_paused = True
    penalty_right_second_paused = True
    penalty_left_first_started = False
    penalty_left_second_started = False
    penalty_right_first_started = False
    penalty_right_second_started = False
    with open("output/main_timer.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_left_first.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_left_second.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_right_first.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_right_second.txt", "w") as file:
        file.write("00:00")


btn_reset_main_timer = Button(window, text="RESET TIMERS", font=("square sans serif 7", 17), command=reset_main_timer,
                              relief='flat',
                              bg='black', fg='#00fffe', borderwidth=0)
btn_reset_main_timer.place(x=180, y=290)


# New game
def new_game():
    global period_time
    global paused_main_timer
    global game_started
    global penalty_left_first_time
    global penalty_left_second_time
    global penalty_right_first_time
    global penalty_right_second_time
    global penalty_left_first_paused
    global penalty_left_second_paused
    global penalty_right_first_paused
    global penalty_right_second_paused
    global penalty_left_first_started
    global penalty_left_second_started
    global penalty_right_first_started
    global penalty_right_second_started
    global score_team1
    global score_team2
    global period
    period_time = 0
    lbl_timer.config(text="00:00")
    var.set(0)
    game_started = False
    paused_main_timer = False
    btn_pause_main_timer.config(bg='black')
    penalty_left_first_time = 120
    penalty_left_second_time = 120
    penalty_right_first_time = 120
    penalty_right_second_time = 120
    lbl_penalty_left1.config(text="02:00")
    lbl_penalty_left2.config(text="02:00")
    lbl_penalty_right1.config(text="02:00")
    lbl_penalty_right2.config(text="02:00")
    chk_penalty_left_first_state.set(False)
    chk_penalty_left_second_state.set(False)
    chk_penalty_right_first_state.set(False)
    chk_penalty_right_second_state.set(False)
    penalty_left_first_paused = True
    penalty_left_second_paused = True
    penalty_right_first_paused = True
    penalty_right_second_paused = True
    penalty_left_first_started = False
    penalty_left_second_started = False
    penalty_right_first_started = False
    penalty_right_second_started = False
    score_team1 = 0
    lbl_score_left.config(text=score_team1)
    score_team2 = 0
    lbl_score_right.config(text=score_team2)
    period = 1
    lbl_period.config(text=period)
    team1.delete(0, END)
    team2.delete(0, END)
    with open("output/score_team1.txt", "w") as file:
        file.write("0")
    with open("output/score_team2.txt", "w") as file:
        file.write("0")
    with open("output/period.txt", "w") as file:
        file.write("1")
    with open("output/main_timer.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_left_first.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_left_second.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_right_first.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_right_second.txt", "w") as file:
        file.write("00:00")


btn_new_game = Button(window, text="NEW GAME", font=("square sans serif 7", 17), command=new_game, relief='flat',
                      bg='black', fg='#00fffe', borderwidth=0)
btn_new_game.place(x=440, y=290)


# Start_Pause Main Timer
def update_main_timer():
    global period_time
    global paused_main_timer
    if paused_main_timer:
        btn_pause_main_timer.config(bg='yellow')
        return
    btn_pause_main_timer.config(bg='black')
    period_time = period_time - 1

    if period_time >= 0:
        m, s = divmod(period_time - 1, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)

        lbl_timer.config(text=min_sec_format)

        window.after(1000, update_main_timer)

        with open("output/main_timer.txt", "w") as file:
            file.write(str(min_sec_format))

        team1_write = team1.get()
        team2_write = team2.get()
        with codecs.open("output/team1.txt", "w", encoding='utf-8') as file:
            file.write(str(team1_write))
        with codecs.open("output/team2.txt", "w", encoding='utf-8') as file:
            file.write(str(team2_write))


def start_main_timer(timer):
    global period_time
    global game_started
    if game_started:
        return
    else:
        game_started = True
        m, s = divmod(period_time - 1, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        period_time = timer
        lbl_timer.config(text=min_sec_format)

        window.after(1000, update_main_timer)


btn_start_main_timer = Button(window, text="START", font=("square sans serif 7", 20),
                              command=lambda: start_main_timer(period_time),
                              relief='flat', bg='black', fg='#fe0000', borderwidth=0)
btn_start_main_timer.place(x=265, y=230)


def pause():
    global paused_main_timer
    global penalty_left_first_paused
    global penalty_left_first_started
    global penalty_left_second_paused
    global penalty_left_second_started
    global penalty_right_first_paused
    global penalty_right_first_started
    global penalty_right_second_paused
    global penalty_right_second_started
    paused_main_timer = not paused_main_timer
    if not paused_main_timer:
        update_main_timer()
        if penalty_left_first_started:
            update_penalty_left_first_timer()
        if penalty_left_second_started:
            update_penalty_left_second_timer()
        if penalty_right_first_started:
            update_penalty_right_first_timer()
        if penalty_right_second_started:
            update_penalty_right_second_timer()


btn_pause_main_timer = Button(window, text="PAUSE", font=("square sans serif 7", 20), command=pause,
                              relief='flat', bg='black', fg='#fe0000', borderwidth=0)
btn_pause_main_timer.place(x=410, y=230)


# Add radiobuttons default period time

def check_radio_btn():
    radio_button = var.get()
    global period_time
    period_time = radio_button
    if var.get() == 300:
        period_time = 300
    elif var.get() == 600:
        period_time = 600
    elif var.get() == 900:
        period_time = 900
    elif var.get() == 1200:
        period_time = 1200
    m, s = divmod(period_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    with open("output/main_timer.txt", "w") as file:
        file.write(str(min_sec_format))
    team1_write = team1.get()
    team2_write = team2.get()
    with codecs.open("output/team1.txt", "w", encoding='utf-8') as file:
        file.write(str(team1_write))
    with codecs.open("output/team2.txt", "w", encoding='utf-8') as file:
        file.write(str(team2_write))


var = IntVar()
var.set(0)
rad1 = Radiobutton(window, text='05:00', value=300, variable=var, command=check_radio_btn, bg="#404040", fg="#feba00",
                   selectcolor='black', font=("arial", 12))
rad2 = Radiobutton(window, text='10:00', value=600, variable=var, command=check_radio_btn, bg="#404040", fg="#feba00",
                   selectcolor='black', font=("arial", 12))
rad3 = Radiobutton(window, text='15:00', value=900, variable=var, command=check_radio_btn, bg="#404040", fg="#feba00",
                   selectcolor='black', font=("arial", 12))
rad4 = Radiobutton(window, text='20:00', value=1200, variable=var, command=check_radio_btn, bg="#404040", fg="#feba00",
                   selectcolor='black', font=("arial", 12))
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

with open("output/score_team1.txt", "w") as file:
    file.write("0")
with open("output/score_team2.txt", "w") as file:
    file.write("0")
with open("output/period.txt", "w") as file:
    file.write("1")
with open("output/main_timer.txt", "w") as file:
    file.write("00:00")
with open("output/penalty_left_first.txt", "w") as file:
    file.write("00:00")
with open("output/penalty_left_second.txt", "w") as file:
    file.write("00:00")
with open("output/penalty_right_first.txt", "w") as file:
    file.write("00:00")
with open("output/penalty_right_second.txt", "w") as file:
    file.write("00:00")

# Add hotkeys
is_alive = True


def exit_application():
    global is_alive
    stop_checking_hotkeys()
    is_alive = False


bindings = [
    [["control", "numpad_7"], None, nClick_score_left_up],
    [["control", "numpad_1"], None, nClick_score_left_down],
    [["control", "numpad_9"], None, nClick_score_right_up],
    [["control", "numpad_3"], None, nClick_score_right_down],
    [["control", "numpad_5"], None, pause],
    [["control", "shift", "9"], None, exit_application],
]

register_hotkeys(bindings)
start_checking_hotkeys()

window.mainloop()
