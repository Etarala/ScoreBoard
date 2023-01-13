"""

from tkinter import *
from datetime import datetime

temp = 0
after_id = ''

def tick_tack():
    global temp, after_id
    after_id = root.after(1000, tick_tack)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label.configure(text = str(f_temp))
    temp +=1

def start_sw():
    button_1.grid_forget()
    button_2.grid(row = 1, columnspan = 2, sticky='ew')
    tick_tack()

def stop_sw():
    button_2.grid_forget()
    button_3.grid(row = 1, column = 0, sticky = 'ew')
    button_4.grid(row = 1, column = 1, sticky = 'ew')
    root.after_cancel(after_id)

def continue_sw():
    button_3.grid_forget()
    button_4.grid_forget()
    button_2.grid(row=1, columnspan = 2, sticky = 'ew')
    tick_tack()

def reset_sw():
    global temp
    temp = 0
    label.configure(text = '00:00')
    button_3.grid_forget()
    button_4.grid_forget()
    button_1.grid(row=1, columnspan = 2, sticky = 'ew')



root = Tk()
root.title('StopWatch')
label = Label(root, width = 5, font = ('Arial', 100), text = '00:00', bg = 'black', fg = "white")
label.grid(row = 0, columnspan = 2)

button_1 = Button(root, text='Start', font = ('Arial', 30), command = start_sw)
button_2 = Button(root, text='Stop', font = ('Arial', 30), command = stop_sw)
button_3 = Button(root, text='Continue', font = ('Arial', 30), command = continue_sw)
button_4 = Button(root, text='Reset', font = ('Arial', 30), command = reset_sw)

button_1.grid(row=1, columnspan = 2, sticky = 'ew')

root.mainloop()
"""
from tkinter import *
from datetime import datetime

clean_time = 0
after_id = ''

def tick_tack():
    global clean_time, after_id
    after_id = root.after(1000, tick_tack)
    f_temp = datetime.fromtimestamp(clean_time).strftime('%M:%S')
    label.configure(text = str(f_temp))
    clean_time +=1

def start_sw():
    global clean_time
    clean_time = 0
    button_1.grid_forget()
    button_2.grid(row = 1, columnspan = 2, sticky='ew')
    tick_tack()

def stop_sw():
    button_2.grid_forget()
    button_1.grid(row=1, columnspan = 2, sticky = 'ew')
    root.after_cancel(after_id)


root = Tk()
root.title('StopWatch')
label = Label(root, width = 5, font = ('Arial', 100), text = '00:00', bg = 'black', fg = "white")
label.grid(row = 0, columnspan = 2)

button_1 = Button(root, text='Start', font = ('Arial', 30), command = start_sw)
button_2 = Button(root, text='Stop', font = ('Arial', 30), command = stop_sw)


button_1.grid(row=1, columnspan = 2, sticky = 'ew')

root.mainloop()













def openNewWindow_statistics():
    newWindow = Toplevel(window)

    global statistics_widgets
    statistics_widgets['lbl_stat_value_left_goal'] = lbl_stat_value_left_goal

    lbl_stat_value_left_goal = Label(newWindow, text=statistics_widgets['lbl_stat_value_left_goal'],)
    lbl_stat_value_left_goal.place(x=230, y=60)

def update_statistics_values():
    global statistics_widgets
    global score_team1
    statistics_widgets['lbl_stat_value_left_goal'] = str(score_team1)