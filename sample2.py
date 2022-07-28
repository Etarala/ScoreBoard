from tkinter import *
from tkinter.ttk import Checkbutton

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')

check1 = False
def check1f():
    check1_button = chk_state.get()
    global check1
    check1 = check1_button
    print(check1)


chk_state = BooleanVar()
chk_state.set(False)  # задайте проверку состояния чекбокса
chk = Checkbutton(window, text='Выбрать', var=chk_state, command = check1f, onvalue=1, offvalue=0)
chk.grid(column=0, row=0)
#print(check1)
window.mainloop()


def update_main_timer():
    global period_time
    global paused_main_timer
    if paused_main_timer:
        btn_pause_main_timer.config(bg='yellow')
        return
    btn_pause_main_timer.config(bg='black')
    period_time = period_time - 1

    if period_time >= 0:
        m, s = divmod(period_time, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)

        lbl_timer.config(text=min_sec_format)

        window.after(1000, update_main_timer)


def start_main_timer(timer):
    global period_time
    global game_started
    if game_started:
        return
    else:
        game_started = True
        m, s = divmod(period_time+1, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        period_time = timer
        lbl_timer.config(text=min_sec_format)

        window.after(1000, update_main_timer)

btn_start_main_timer = Button(window, text="START", font=("square sans serif 7", 20), command=lambda: start_main_timer(period_time),
                     relief='flat', bg='black', fg='#fe0000', borderwidth=0)
btn_start_main_timer.place(x=265, y=230)

def pause():
    global paused_main_timer
    global paused_penalty_left_first
    paused_main_timer = not paused_main_timer
    paused_penalty_left_first = not paused_penalty_left_first

    if not paused_penalty_left_first:
        update_penalty_left_first_timer()
    if not paused_main_timer:
        update_main_timer()




penalty_left_first_started = False
paused_penalty_left_first_started = True







penalty_left_first_time = 120
penalty_left_second_time = 120
penalty_right_first_time = 120
penalty_right_second_time = 120


