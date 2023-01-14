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









def shot_team2():
    global statistics_params
    statistics_params['shot_team2'] += 1
    with open("output/shot_team2.txt", "w") as file:
        file.write(str(statistics_params['shot_team2']))
    update_statistics_values()

def shot_gates_team2():
    global statistics_params
    statistics_params['shot_gates_team2'] += 1
    with open("output/shot_gates_team2.txt", "w") as file:
        file.write(str(statistics_params['shot_gates_team2']))
    safety_factor_team1()
    update_statistics_values()

def face_off_team2():
    global statistics_params
    statistics_params['face_off_team2'] += 1
    with open("output/face_off_team2.txt", "w") as file:
        file.write(str(statistics_params['face_off_team2']))
    update_statistics_values()

def penalty_team2():
    global statistics_params
    statistics_params['penalty_team2'] += 1
    with open("output/penalty_team2.txt", "w") as file:
        file.write(str(statistics_params['penalty_team2']))
    update_statistics_values()

def safety_factor_team1():
    global statistics_params
    statistics_params['safety_factor_team1'] = round((100 * (statistics_params['shot_gates_team2'] - score_team2)) / statistics_params['shot_gates_team2'],2)
    with open("output/safety_factor_team1.txt", "w") as file:
        file.write(str(statistics_params['safety_factor_team1']))

def safety_factor_team2():
    global statistics_params
    statistics_params['safety_factor_team2'] = round((100 * (statistics_params['shot_gates_team1'] - score_team1)) / statistics_params['shot_gates_team1'],2)
    with open("output/safety_factor_team2.txt", "w") as file:
        file.write(str(statistics_params['safety_factor_team2']))






