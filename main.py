from tkinter import *
import codecs
import pyglet
from global_hotkeys import *
import shutil
from tkinter import messagebox
import webbrowser
from datetime import datetime

window = Tk()
window.title("ScoreBoard")
window.geometry('815x520')
window.resizable(width=0, height=0)
window.iconbitmap(r"pict/HdScoreboard.ico")

background = PhotoImage(file="pict/layer.png")
background_label = Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

pyglet.font.add_file('fonts/Digital Numbers.ttf')
pyglet.font.add_file('fonts/square sans serif 7.ttf')

mainmenu = Menu(window)
window.config(menu=mainmenu)

# Define variables
score_team1 = 0
score_team2 = 0
period = 1
period_time = 0
clean_time = 0
after_id = ''
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
bullit_left1_1 = False
bullit_left1_2 = False
bullit_left2_1 = False
bullit_left2_2 = False
bullit_left3_1 = False
bullit_left3_2 = False
bullit_left4_1 = False
bullit_left4_2 = False
bullit_left5_1 = False
bullit_left5_2 = False
bullit_left6_1 = False
bullit_left6_2 = False
bullit_left7_1 = False
bullit_left7_2 = False
bullit_left8_1 = False
bullit_left8_2 = False
bullit_left9_1 = False
bullit_left9_2 = False
bullit_left10_1 = False
bullit_left10_2 = False
bullit_right1_1 = False
bullit_right1_2 = False
bullit_right2_1 = False
bullit_right2_2 = False
bullit_right3_1 = False
bullit_right3_2 = False
bullit_right4_1 = False
bullit_right4_2 = False
bullit_right5_1 = False
bullit_right5_2 = False
bullit_right6_1 = False
bullit_right6_2 = False
bullit_right7_1 = False
bullit_right7_2 = False
bullit_right8_1 = False
bullit_right8_2 = False
bullit_right9_1 = False
bullit_right9_2 = False
bullit_right10_1 = False
bullit_right10_2 = False
clean_time_started = False
with open("output/clean_time.txt", "w") as file:
    file.write("00:00")
with open("output/shot_team1.txt", "w") as file:
    file.write('0')
with open("output/shot_gates_team1.txt", "w") as file:
    file.write('0')
with open("output/face_off_team1.txt", "w") as file:
    file.write('0')
with open("output/penalty_team1.txt", "w") as file:
    file.write('0')
with open("output/shot_team2.txt", "w") as file:
    file.write('0')
with open("output/shot_gates_team2.txt", "w") as file:
    file.write('0')
with open("output/face_off_team2.txt", "w") as file:
    file.write('0')
with open("output/penalty_team2.txt", "w") as file:
    file.write('0')
with open("output/safety_factor_team1.txt",  "w") as file:
    file.write('0')
with open("output/safety_factor_team2.txt", "w") as file:
    file.write('0')


is_alive = False


def global_hotkeys():
    global is_alive
    if is_alive == False:
        start_checking_hotkeys()
        is_alive = True
    elif is_alive == True:
        stop_checking_hotkeys()
        is_alive = False


# Bullets
def openNewWindow():
    global window
    newWindow = Toplevel(window)
    newWindow.geometry("400x510")
    newWindow.resizable(width=0, height=0)
    newWindow.title("Bullets")
    newWindow["bg"] = "#404040"
    newWindow.iconbitmap(r"pict/HdScoreboard.ico")

    lbl_separator = Label(newWindow, text="", fg="white")
    lbl_separator.place(x=198, y=0, width=10, height=510)

    lbl_bullits_name_left = Label(newWindow, text=team1.get(), bg="#404040", fg="#feba00",
                                  font=("square sans serif 7", 17))
    lbl_bullits_name_left.place(x=15, y=10)

    lbl_bullits_name_right = Label(newWindow, text=team2.get(), bg="#404040", fg="#feba00",
                                   font=("square sans serif 7", 17))
    lbl_bullits_name_right.place(x=220, y=10)

    lbl_bullits_name_left_miss = Label(newWindow, text="MISS", bg="#404040", fg="white",
                                       font=("square sans serif 7", 14))
    lbl_bullits_name_left_miss.place(x=14, y=70)

    lbl_bullits_name_left_goal = Label(newWindow, text="GOAL", bg="#404040", fg="white",
                                       font=("square sans serif 7", 14))
    lbl_bullits_name_left_goal.place(x=115, y=70)

    lbl_bullits_name_right_miss = Label(newWindow, text="MISS", bg="#404040", fg="white",
                                        font=("square sans serif 7", 14))
    lbl_bullits_name_right_miss.place(x=220, y=70)

    lbl_bullits_name_right_goal = Label(newWindow, text="GOAL", bg="#404040", fg="white",
                                        font=("square sans serif 7", 14))
    lbl_bullits_name_right_goal.place(x=320, y=70)

    shutil.copyfile("pict/1.png", "output/left_1.png")
    shutil.copyfile("pict/1.png", "output/left_2.png")
    shutil.copyfile("pict/1.png", "output/left_3.png")
    shutil.copyfile("pict/1.png", "output/left_4.png")
    shutil.copyfile("pict/1.png", "output/left_5.png")
    shutil.copyfile("pict/1.png", "output/left_6.png")
    shutil.copyfile("pict/1.png", "output/left_7.png")
    shutil.copyfile("pict/1.png", "output/left_8.png")
    shutil.copyfile("pict/1.png", "output/left_9.png")
    shutil.copyfile("pict/1.png", "output/left_10.png")
    shutil.copyfile("pict/1.png", "output/right_1.png")
    shutil.copyfile("pict/1.png", "output/right_2.png")
    shutil.copyfile("pict/1.png", "output/right_3.png")
    shutil.copyfile("pict/1.png", "output/right_4.png")
    shutil.copyfile("pict/1.png", "output/right_5.png")
    shutil.copyfile("pict/1.png", "output/right_6.png")
    shutil.copyfile("pict/1.png", "output/right_7.png")
    shutil.copyfile("pict/1.png", "output/right_8.png")
    shutil.copyfile("pict/1.png", "output/right_9.png")
    shutil.copyfile("pict/1.png", "output/right_10.png")

    # Bullits team left

    def chk_bullits_left_11():
        global bullit_left1_1
        check_11_left = chk_bullits_left_11_state.get()
        bullit_left_11 = check_11_left
        if bullit_left_11 == True:
            shutil.copyfile("pict/2.png", "output/left_1.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_1.png")

    chk_bullits_left_11_state = BooleanVar()
    chk_bullits_left_11_state.set(False)
    chk_bullits_left_11_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_11_state,
                                          command=chk_bullits_left_11, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_11_btn.place(x=30, y=90)

    def chk_bullits_left_12():
        global bullit_left1_2
        check_12_left = chk_bullits_left_12_state.get()
        bullit_left_12 = check_12_left
        if bullit_left_12 == True:
            shutil.copyfile("pict/3.png", "output/left_1.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_1.png")

    chk_bullits_left_12_state = BooleanVar()
    chk_bullits_left_12_state.set(False)
    chk_bullits_left_12_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_12_state,
                                          command=chk_bullits_left_12, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_12_btn.place(x=130, y=90)

    def chk_bullits_left_21():
        global bullit_left2_1
        check_21_left = chk_bullits_left_21_state.get()
        bullit_left_21 = check_21_left
        if bullit_left_21 == True:
            shutil.copyfile("pict/2.png", "output/left_2.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_2.png")

    chk_bullits_left_21_state = BooleanVar()
    chk_bullits_left_21_state.set(False)
    chk_bullits_left_21_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_21_state,
                                          command=chk_bullits_left_21, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_21_btn.place(x=30, y=130)

    def chk_bullits_left_22():
        global bullit_left2_2
        check_22_left = chk_bullits_left_22_state.get()
        bullit_left_22 = check_22_left
        if bullit_left_22 == True:
            shutil.copyfile("pict/3.png", "output/left_2.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_2.png")

    chk_bullits_left_22_state = BooleanVar()
    chk_bullits_left_22_state.set(False)
    chk_bullits_left_22_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_22_state,
                                          command=chk_bullits_left_22, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_22_btn.place(x=130, y=130)

    def chk_bullits_left_31():
        global bullit_left3_1
        check_31_left = chk_bullits_left_31_state.get()
        bullit_left_31 = check_31_left
        if bullit_left_31 == True:
            shutil.copyfile("pict/2.png", "output/left_3.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_3.png")

    chk_bullits_left_31_state = BooleanVar()
    chk_bullits_left_31_state.set(False)
    chk_bullits_left_31_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_31_state,
                                          command=chk_bullits_left_31, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_31_btn.place(x=30, y=170)

    def chk_bullits_left_32():
        global bullit_left3_2
        check_32_left = chk_bullits_left_32_state.get()
        bullit_left_32 = check_32_left
        if bullit_left_32 == True:
            shutil.copyfile("pict/3.png", "output/left_3.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_3.png")

    chk_bullits_left_32_state = BooleanVar()
    chk_bullits_left_32_state.set(False)
    chk_bullits_left_32_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_32_state,
                                          command=chk_bullits_left_32, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_32_btn.place(x=130, y=170)

    def chk_bullits_left_41():
        global bullit_left4_1
        check_41_left = chk_bullits_left_41_state.get()
        bullit_left_41 = check_41_left
        if bullit_left_41 == True:
            shutil.copyfile("pict/2.png", "output/left_4.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_4.png")

    chk_bullits_left_41_state = BooleanVar()
    chk_bullits_left_41_state.set(False)
    chk_bullits_left_41_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_41_state,
                                          command=chk_bullits_left_41, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_41_btn.place(x=30, y=210)

    def chk_bullits_left_42():
        global bullit_left4_2
        check_42_left = chk_bullits_left_42_state.get()
        bullit_left_42 = check_42_left
        if bullit_left_42 == True:
            shutil.copyfile("pict/3.png", "output/left_4.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_4.png")

    chk_bullits_left_42_state = BooleanVar()
    chk_bullits_left_42_state.set(False)
    chk_bullits_left_42_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_42_state,
                                          command=chk_bullits_left_42, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_42_btn.place(x=130, y=210)

    def chk_bullits_left_51():
        global bullit_left5_1
        check_51_left = chk_bullits_left_51_state.get()
        bullit_left_51 = check_51_left
        if bullit_left_51 == True:
            shutil.copyfile("pict/2.png", "output/left_5.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_5.png")

    chk_bullits_left_51_state = BooleanVar()
    chk_bullits_left_51_state.set(False)
    chk_bullits_left_51_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_51_state,
                                          command=chk_bullits_left_51, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_51_btn.place(x=30, y=250)

    def chk_bullits_left_52():
        global bullit_left5_2
        check_52_left = chk_bullits_left_52_state.get()
        bullit_left_52 = check_52_left
        if bullit_left_52 == True:
            shutil.copyfile("pict/3.png", "output/left_5.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_5.png")

    chk_bullits_left_52_state = BooleanVar()
    chk_bullits_left_52_state.set(False)
    chk_bullits_left_52_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_52_state,
                                          command=chk_bullits_left_52, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_52_btn.place(x=130, y=250)


    def chk_bullits_left_61():
        global bullit_left6_1
        check_61_left = chk_bullits_left_61_state.get()
        bullit_left_61 = check_61_left
        if bullit_left_61 == True:
            shutil.copyfile("pict/2.png", "output/left_6.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_6.png")

    chk_bullits_left_61_state = BooleanVar()
    chk_bullits_left_61_state.set(False)
    chk_bullits_left_61_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_61_state,
                                          command=chk_bullits_left_61, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_61_btn.place(x=30, y=290)

    def chk_bullits_left_62():
        global bullit_left6_2
        check_62_left = chk_bullits_left_62_state.get()
        bullit_left_62 = check_62_left
        if bullit_left_62 == True:
            shutil.copyfile("pict/3.png", "output/left_6.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_6.png")

    chk_bullits_left_62_state = BooleanVar()
    chk_bullits_left_62_state.set(False)
    chk_bullits_left_62_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_62_state,
                                          command=chk_bullits_left_62, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_62_btn.place(x=130, y=290)

    def chk_bullits_left_71():
        global bullit_left7_1
        check_71_left = chk_bullits_left_71_state.get()
        bullit_left_71 = check_71_left
        if bullit_left_71 == True:
            shutil.copyfile("pict/2.png", "output/left_7.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_7.png")

    chk_bullits_left_71_state = BooleanVar()
    chk_bullits_left_71_state.set(False)
    chk_bullits_left_71_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_71_state,
                                          command=chk_bullits_left_71, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_71_btn.place(x=30, y=330)

    def chk_bullits_left_72():
        global bullit_left7_2
        check_72_left = chk_bullits_left_72_state.get()
        bullit_left_72 = check_72_left
        if bullit_left_72 == True:
            shutil.copyfile("pict/3.png", "output/left_7.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_7.png")

    chk_bullits_left_72_state = BooleanVar()
    chk_bullits_left_72_state.set(False)
    chk_bullits_left_72_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_72_state,
                                          command=chk_bullits_left_72, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_72_btn.place(x=130, y=330)

    def chk_bullits_left_81():
        global bullit_left8_1
        check_81_left = chk_bullits_left_81_state.get()
        bullit_left_81 = check_81_left
        if bullit_left_81 == True:
            shutil.copyfile("pict/2.png", "output/left_8.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_8.png")

    chk_bullits_left_81_state = BooleanVar()
    chk_bullits_left_81_state.set(False)
    chk_bullits_left_81_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_81_state,
                                          command=chk_bullits_left_81, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_81_btn.place(x=30, y=370)

    def chk_bullits_left_82():
        global bullit_left8_2
        check_82_left = chk_bullits_left_82_state.get()
        bullit_left_82 = check_82_left
        if bullit_left_82 == True:
            shutil.copyfile("pict/3.png", "output/left_8.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_8.png")

    chk_bullits_left_82_state = BooleanVar()
    chk_bullits_left_82_state.set(False)
    chk_bullits_left_82_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_82_state,
                                          command=chk_bullits_left_82, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_82_btn.place(x=130, y=370)


    def chk_bullits_left_91():
        global bullit_left9_1
        check_91_left = chk_bullits_left_91_state.get()
        bullit_left_91 = check_91_left
        if bullit_left_91 == True:
            shutil.copyfile("pict/2.png", "output/left_9.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_9.png")

    chk_bullits_left_91_state = BooleanVar()
    chk_bullits_left_91_state.set(False)
    chk_bullits_left_91_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_91_state,
                                          command=chk_bullits_left_91, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_91_btn.place(x=30, y=410)

    def chk_bullits_left_92():
        global bullit_left9_2
        check_92_left = chk_bullits_left_92_state.get()
        bullit_left_92 = check_92_left
        if bullit_left_92 == True:
            shutil.copyfile("pict/3.png", "output/left_9.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_9.png")

    chk_bullits_left_92_state = BooleanVar()
    chk_bullits_left_92_state.set(False)
    chk_bullits_left_92_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_92_state,
                                          command=chk_bullits_left_92, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_92_btn.place(x=130, y=410)


    def chk_bullits_left_101():
        global bullit_left10_1
        check_101_left = chk_bullits_left_101_state.get()
        bullit_left_101 = check_101_left
        if bullit_left_101 == True:
            shutil.copyfile("pict/2.png", "output/left_10.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_10.png")

    chk_bullits_left_101_state = BooleanVar()
    chk_bullits_left_101_state.set(False)
    chk_bullits_left_101_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_101_state,
                                          command=chk_bullits_left_101, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_101_btn.place(x=30, y=450)

    def chk_bullits_left_102():
        global bullit_left10_2
        check_102_left = chk_bullits_left_102_state.get()
        bullit_left_102 = check_102_left
        if bullit_left_102 == True:
            shutil.copyfile("pict/3.png", "output/left_10.png")
        else:
            shutil.copyfile("pict/1.png", "output/left_10.png")

    chk_bullits_left_102_state = BooleanVar()
    chk_bullits_left_102_state.set(False)
    chk_bullits_left_102_btn = Checkbutton(newWindow, text='', var=chk_bullits_left_102_state,
                                          command=chk_bullits_left_102, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_left_102_btn.place(x=130, y=450)




    # Bullits team right

    def chk_bullits_right_11():
        global bullit_right1_1
        check_11_right = chk_bullits_right_11_state.get()
        bullit_right_11 = check_11_right
        if bullit_right_11 == True:
            shutil.copyfile("pict/2.png", "output/right_1.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_1.png")

    chk_bullits_right_11_state = BooleanVar()
    chk_bullits_right_11_state.set(False)
    chk_bullits_right_11_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_11_state,
                                           command=chk_bullits_right_11, bg="#404040", fg="#fe0000",
                                           selectcolor='black', activebackground="#404040",
                                           font=("square sans serif 7", 25))
    chk_bullits_right_11_btn.place(x=235, y=90)

    def chk_bullits_right_12():
        global bullit_right1_2
        check_12_right = chk_bullits_right_12_state.get()
        bullit_right_12 = check_12_right
        if bullit_right_12 == True:
            shutil.copyfile("pict/3.png", "output/right_1.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_1.png")

    chk_bullits_right_12_state = BooleanVar()
    chk_bullits_right_12_state.set(False)
    chk_bullits_right_12_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_12_state,
                                           command=chk_bullits_right_12, bg="#404040", fg="#03bd02",
                                           selectcolor='black', activebackground="#404040",
                                           font=("square sans serif 7", 25))
    chk_bullits_right_12_btn.place(x=335, y=90)

    def chk_bullits_right_21():
        global bullit_right2_1
        check_21_right = chk_bullits_right_21_state.get()
        bullit_right_21 = check_21_right
        if bullit_right_21 == True:
            shutil.copyfile("pict/2.png", "output/right_2.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_2.png")

    chk_bullits_right_21_state = BooleanVar()
    chk_bullits_right_21_state.set(False)
    chk_bullits_right_21_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_21_state,
                                           command=chk_bullits_right_21, bg="#404040", fg="#fe0000",
                                           selectcolor='black', activebackground="#404040",
                                           font=("square sans serif 7", 25))
    chk_bullits_right_21_btn.place(x=235, y=130)

    def chk_bullits_right_22():
        global bullit_right2_2
        check_22_right = chk_bullits_right_22_state.get()
        bullit_right_22 = check_22_right
        if bullit_right_22 == True:
            shutil.copyfile("pict/3.png", "output/right_2.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_2.png")

    chk_bullits_right_22_state = BooleanVar()
    chk_bullits_right_22_state.set(False)
    chk_bullits_right_22_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_22_state,
                                           command=chk_bullits_right_22, bg="#404040", fg="#03bd02",
                                           selectcolor='black', activebackground="#404040",
                                           font=("square sans serif 7", 25))
    chk_bullits_right_22_btn.place(x=335, y=130)

    def chk_bullits_right_31():
        global bullit_right3_1
        check_31_right = chk_bullits_right_31_state.get()
        bullit_right_31 = check_31_right
        if bullit_right_31 == True:
            shutil.copyfile("pict/2.png", "output/right_3.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_3.png")

    chk_bullits_right_31_state = BooleanVar()
    chk_bullits_right_31_state.set(False)
    chk_bullits_right_31_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_31_state,
                                           command=chk_bullits_right_31, bg="#404040", fg="#fe0000",
                                           selectcolor='black', activebackground="#404040",
                                           font=("square sans serif 7", 25))
    chk_bullits_right_31_btn.place(x=235, y=170)

    def chk_bullits_right_32():
        global bullit_right3_2
        check_32_right = chk_bullits_right_32_state.get()
        bullit_right_32 = check_32_right
        if bullit_right_32 == True:
            shutil.copyfile("pict/3.png", "output/right_3.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_3.png")

    chk_bullits_right_32_state = BooleanVar()
    chk_bullits_right_32_state.set(False)
    chk_bullits_right_32_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_32_state,
                                           command=chk_bullits_right_32, bg="#404040", fg="#03bd02",
                                           selectcolor='black', activebackground="#404040",
                                           font=("square sans serif 7", 25))
    chk_bullits_right_32_btn.place(x=335, y=170)

    def chk_bullits_right_41():
        global bullit_right4_1
        check_41_right = chk_bullits_right_41_state.get()
        bullit_right_41 = check_41_right
        if bullit_right_41 == True:
            shutil.copyfile("pict/2.png", "output/right_4.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_4.png")

    chk_bullits_right_41_state = BooleanVar()
    chk_bullits_right_41_state.set(False)
    chk_bullits_right_41_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_41_state,
                                           command=chk_bullits_right_41, bg="#404040", fg="#fe0000",
                                           selectcolor='black', activebackground="#404040",
                                           font=("square sans serif 7", 25))
    chk_bullits_right_41_btn.place(x=235, y=210)

    def chk_bullits_right_42():
        global bullit_right4_2
        check_42_right = chk_bullits_right_42_state.get()
        bullit_right_42 = check_42_right
        if bullit_right_42 == True:
            shutil.copyfile("pict/3.png", "output/right_4.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_4.png")

    chk_bullits_right_42_state = BooleanVar()
    chk_bullits_right_42_state.set(False)
    chk_bullits_right_42_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_42_state,
                                           command=chk_bullits_right_42, bg="#404040", fg="#03bd02",
                                           selectcolor='black', activebackground="#404040",
                                           font=("square sans serif 7", 25))
    chk_bullits_right_42_btn.place(x=335, y=210)

    def chk_bullits_right_51():
        global bullit_right5_1
        check_51_right = chk_bullits_right_51_state.get()
        bullit_right_51 = check_51_right
        if bullit_right_51 == True:
            shutil.copyfile("pict/2.png", "output/right_5.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_5.png")

    chk_bullits_right_51_state = BooleanVar()
    chk_bullits_right_51_state.set(False)
    chk_bullits_right_51_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_51_state,
                                           command=chk_bullits_right_51, bg="#404040", fg="#fe0000",
                                           selectcolor='black', activebackground="#404040",
                                           font=("square sans serif 7", 25))
    chk_bullits_right_51_btn.place(x=235, y=250)

    def chk_bullits_right_52():
        global bullit_right5_2
        check_52_right = chk_bullits_right_52_state.get()
        bullit_right_52 = check_52_right
        if bullit_right_52 == True:
            shutil.copyfile("pict/3.png", "output/right_5.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_5.png")

    chk_bullits_right_52_state = BooleanVar()
    chk_bullits_right_52_state.set(False)
    chk_bullits_right_52_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_52_state,
                                           command=chk_bullits_right_52, bg="#404040", fg="#03bd02",
                                           selectcolor='black', activebackground="#404040",
                                           font=("square sans serif 7", 25))
    chk_bullits_right_52_btn.place(x=335, y=250)


    def chk_bullits_right_61():
        global bullit_right6_1
        check_61_right = chk_bullits_right_61_state.get()
        bullit_right_61 = check_61_right
        if bullit_right_61 == True:
            shutil.copyfile("pict/2.png", "output/right_6.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_6.png")

    chk_bullits_right_61_state = BooleanVar()
    chk_bullits_right_61_state.set(False)
    chk_bullits_right_61_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_61_state,
                                          command=chk_bullits_right_61, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_right_61_btn.place(x=235, y=290)

    def chk_bullits_right_62():
        global bullit_right6_2
        check_62_right = chk_bullits_right_62_state.get()
        bullit_right_62 = check_62_right
        if bullit_right_62 == True:
            shutil.copyfile("pict/3.png", "output/right_6.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_6.png")

    chk_bullits_right_62_state = BooleanVar()
    chk_bullits_right_62_state.set(False)
    chk_bullits_right_62_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_62_state,
                                          command=chk_bullits_right_62, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_right_62_btn.place(x=335, y=290)

    def chk_bullits_right_71():
        global bullit_right7_1
        check_71_right = chk_bullits_right_71_state.get()
        bullit_right_71 = check_71_right
        if bullit_right_71 == True:
            shutil.copyfile("pict/2.png", "output/right_7.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_7.png")

    chk_bullits_right_71_state = BooleanVar()
    chk_bullits_right_71_state.set(False)
    chk_bullits_right_71_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_71_state,
                                          command=chk_bullits_right_71, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_right_71_btn.place(x=235, y=330)

    def chk_bullits_right_72():
        global bullit_right7_2
        check_72_right = chk_bullits_right_72_state.get()
        bullit_right_72 = check_72_right
        if bullit_right_72 == True:
            shutil.copyfile("pict/3.png", "output/right_7.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_7.png")

    chk_bullits_right_72_state = BooleanVar()
    chk_bullits_right_72_state.set(False)
    chk_bullits_right_72_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_72_state,
                                          command=chk_bullits_right_72, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_right_72_btn.place(x=335, y=330)

    def chk_bullits_right_81():
        global bullit_right8_1
        check_81_right = chk_bullits_right_81_state.get()
        bullit_right_81 = check_81_right
        if bullit_right_81 == True:
            shutil.copyfile("pict/2.png", "output/right_8.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_8.png")

    chk_bullits_right_81_state = BooleanVar()
    chk_bullits_right_81_state.set(False)
    chk_bullits_right_81_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_81_state,
                                          command=chk_bullits_right_81, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_right_81_btn.place(x=235, y=370)

    def chk_bullits_right_82():
        global bullit_right8_2
        check_82_right = chk_bullits_right_82_state.get()
        bullit_right_82 = check_82_right
        if bullit_right_82 == True:
            shutil.copyfile("pict/3.png", "output/right_8.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_8.png")

    chk_bullits_right_82_state = BooleanVar()
    chk_bullits_right_82_state.set(False)
    chk_bullits_right_82_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_82_state,
                                          command=chk_bullits_right_82, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_right_82_btn.place(x=335, y=370)


    def chk_bullits_right_91():
        global bullit_right9_1
        check_91_right = chk_bullits_right_91_state.get()
        bullit_right_91 = check_91_right
        if bullit_right_91 == True:
            shutil.copyfile("pict/2.png", "output/right_9.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_9.png")

    chk_bullits_right_91_state = BooleanVar()
    chk_bullits_right_91_state.set(False)
    chk_bullits_right_91_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_91_state,
                                          command=chk_bullits_right_91, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_right_91_btn.place(x=235, y=410)

    def chk_bullits_right_92():
        global bullit_right9_2
        check_92_right = chk_bullits_right_92_state.get()
        bullit_right_92 = check_92_right
        if bullit_right_92 == True:
            shutil.copyfile("pict/3.png", "output/right_9.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_9.png")

    chk_bullits_right_92_state = BooleanVar()
    chk_bullits_right_92_state.set(False)
    chk_bullits_right_92_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_92_state,
                                          command=chk_bullits_right_92, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_right_92_btn.place(x=335, y=410)


    def chk_bullits_right_101():
        global bullit_right10_1
        check_101_right = chk_bullits_right_101_state.get()
        bullit_right_101 = check_101_right
        if bullit_right_101 == True:
            shutil.copyfile("pict/2.png", "output/right_10.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_10.png")

    chk_bullits_right_101_state = BooleanVar()
    chk_bullits_right_101_state.set(False)
    chk_bullits_right_101_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_101_state,
                                          command=chk_bullits_right_101, bg="#404040", fg="#fe0000",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_right_101_btn.place(x=235, y=450)

    def chk_bullits_right_102():
        global bullit_right10_2
        check_102_right = chk_bullits_right_102_state.get()
        bullit_right_102 = check_102_right
        if bullit_right_102 == True:
            shutil.copyfile("pict/3.png", "output/right_10.png")
        else:
            shutil.copyfile("pict/1.png", "output/right_10.png")

    chk_bullits_right_102_state = BooleanVar()
    chk_bullits_right_102_state.set(False)
    chk_bullits_right_102_btn = Checkbutton(newWindow, text='', var=chk_bullits_right_102_state,
                                          command=chk_bullits_right_102, bg="#404040", fg="#03bd02",
                                          selectcolor='black', activebackground="#404040",
                                          font=("square sans serif 7", 25))
    chk_bullits_right_102_btn.place(x=335, y=450)


# New window Statistic
statistics_widgets = {}
def openNewWindow_statistics():
    global window
    newWindow = Toplevel(window)
    newWindow.geometry("600x400")
    newWindow.resizable(width=0, height=0)
    newWindow.title("Statistics")
    newWindow["bg"] = "#404040"
    newWindow.iconbitmap(r"pict/HdScoreboard.ico")
    global score_team1
    global score_team1
    global statistics_widgets
    global statistics_params
    statistics_widgets = {}
    def on_closing():
        global statistics_widgets
        statistics_widgets = {}
        newWindow.destroy()


    statistics_widgets = {}

    lbl_separator = Label(newWindow, text="", fg="white")
    lbl_separator.place(x=300, y=0, width=5, height=400)

    lbl_stat_name_left = Label(newWindow, text=team1.get(), bg="#404040", fg="#feba00",
                                  font=("square sans serif 7", 18))
    lbl_stat_name_left.place(x=15, y=10)

    lbl_stat_name_right = Label(newWindow, text=team2.get(), bg="#404040", fg="#feba00",
                                   font=("square sans serif 7", 18))
    lbl_stat_name_right.place(x=320, y=10)

    lbl_stat_name_left_goal = Label(newWindow, text="ГОЛ", bg="#404040", fg="white",
                                       font=("square sans serif 7", 17))
    lbl_stat_name_left_goal.place(x=14, y=60)

    lbl_stat_value_left_goal = Label(newWindow, text=str(score_team1), bg="#404040", fg="#feba00",
                                    font=("square sans serif 7", 22))
    lbl_stat_value_left_goal.place(x=230, y=60)
    statistics_widgets['lbl_stat_value_left_goal'] = lbl_stat_value_left_goal

    lbl_stat_name_left_shot_team1 = Label(newWindow, text="БРОСОК", bg="#404040", fg="white",
                                    font=("square sans serif 7", 17))
    lbl_stat_name_left_shot_team1.place(x=14, y=100)
    lbl_stat_value_left_shot_team1 = Label(newWindow, text=str(statistics_params['shot_team1']), bg="#404040", fg="#feba00",
                                     font=("square sans serif 7", 22))
    lbl_stat_value_left_shot_team1.place(x=230, y=100)
    statistics_widgets['lbl_stat_value_left_shot_team1'] = lbl_stat_value_left_shot_team1

    lbl_stat_name_left_shot_gates_team1 = Label(newWindow, text="БРОСОК ПО", bg="#404040", fg="white",
                                          font=("square sans serif 7", 17))
    lbl_stat_name_left_shot_gates_team1.place(x=14, y=140)
    lbl_stat_name_left_shot_gates_team1_2 = Label(newWindow, text="ВОРОТАМ", bg="#404040", fg="white",
                                                font=("square sans serif 7", 17))
    lbl_stat_name_left_shot_gates_team1_2.place(x=14, y=160)
    lbl_stat_value_left_shot_gates_team1 = Label(newWindow, text=str(statistics_params['shot_gates_team1']), bg="#404040",
                                           fg="#feba00", font=("square sans serif 7", 22))
    lbl_stat_value_left_shot_gates_team1.place(x=230, y=150)
    statistics_widgets['lbl_stat_value_left_shot_gates_team1'] = lbl_stat_value_left_shot_gates_team1


    newWindow.protocol("WM_DELETE_WINDOW", on_closing)


def update_statistics_values():
    global statistics_widgets
    global score_team1
    global score_team1
    global statistics_params
    if statistics_widgets == {}:
        return
    else:
        statistics_widgets['lbl_stat_value_left_goal'].config(text=str(score_team1))
        statistics_widgets['lbl_stat_value_left_shot_team1'].config(text=str(statistics_params['shot_team1']))
        statistics_widgets['lbl_stat_value_left_shot_gates_team1'].config(text=str(statistics_params['shot_gates_team1']))


# Hotkeys

def hotkeys():
    messagebox.showinfo('Hotkeys',
                        ' ***GAME***\n <Enter> = Start Game\n <Left Ctrl> = Left team 1 score UP\n '
                        '<Right Ctrl> = Right team 1 score UP\n <Space> = Pause\n < 8 > = Period UP \n\n '
                        '***MAIN TIMER***\n < 0 > = Main Timer minutes UP\n < 9 > = Main Timer minutes DOWN\n '
                        '< + > = Main Timer seconds UP\n < - > = Main Timer seconds DOWN\n\n ***CLEAN TIMER***\n '
                        '< 6 > = Start Clean Time Timer\n < 7 > = Stop Clean Time Timer\n\n ***PENALTY***\n '
                        '< z > = Penalty Team left Set\n < / > = Penalty Team Right Set\n\n ***STATISTICS***\n '
                        ' Left Team:\n < F2 > = Shot\n < F3 > = Shot on goal\n < F4 > = Face off\n < F5 > = Penalty\n '
                        ' Right Team:\n < F6 > = Shot\n < F7 > = Shot on goal\n < F8 > = Face off\n < F9 > = Penalty')


def about():
    messagebox.showinfo('About',
                        ' This programm is made by: ETarala\n If you have any questions or suggetions please contact me in\n Email: etarala@mail.ru\n Thank you for downloading the Scoreboard')


def donate():
    webbrowser.open("https://yoomoney.ru/to/41001654796610", new=0, autoraise=True)


filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Bullets", command=openNewWindow)
filemenu.add_command(label="Statistics", command=openNewWindow_statistics)
filemenu.add_checkbutton(label="Global Hotkeys", command=global_hotkeys)
mainmenu.add_cascade(label="Options", menu=filemenu)
helpmenu = Menu(mainmenu, tearoff=0)

helpmenu.add_command(label="Hotkeys", command=hotkeys)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Donate", command=donate)
mainmenu.add_cascade(label="Help", menu=helpmenu)


# Score team left
def nClick_score_left_up():
    global score_team1
    score_team1 += 1
    lbl_score_left.config(text=score_team1)
    with open("output/score_team1.txt", "w") as file:
        file.write(str(score_team1))
    shot_gates_team1()
    update_statistics_values()


def nClick_score_left_down():
    global score_team1
    score_team1 -= 1
    if score_team1 < 0:
        score_team1 = 0
    lbl_score_left.config(text=score_team1)
    with open("output/score_team1.txt", "w") as file:
        file.write(str(score_team1))
    update_statistics_values()


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
    shot_gates_team2()
    update_statistics_values()


def nClick_score_right_down():
    global score_team2
    score_team2 -= 1
    if score_team2 < 0:
        score_team2 = 0
    lbl_score_right.config(text=score_team2)
    with open("output/score_team2.txt", "w") as file:
        file.write(str(score_team2))
    update_statistics_values()


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
    update_statistics_values()


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
    global penalty_left_first_time
    check1left = chk_penalty_left_first_state.get()
    if check1left == False:
        penalty_left_first_time = 120
        lbl_penalty_left1.config(text="02:00")
    global penalty_left_first_started
    global penalty_left_first_paused
    penalty_left_first_started = check1left
    penalty_left_first_paused = not penalty_left_first_started
    m, s = divmod(penalty_left_first_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    with open("output/penalty_left_first.txt", "w") as file:
        file.write(str(min_sec_format))


def set_penalty_left_first():
    check1left = chk_penalty_left_first_state.get()
    if check1left == False:
        chk_penalty_left_first_state.set(True)
    else:
        chk_penalty_left_first_state.set(False)
    chk_penalty_left_first()


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
    with open("output/penalty_left_first.txt", "w") as file:
        file.write(str(min_sec_format))


def nClick_penalty_left_first_minutes_down():
    global penalty_left_first_time
    penalty_left_first_time -= 60
    if penalty_left_first_time < 0:
        penalty_left_first_time = 0
    m, s = divmod(penalty_left_first_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_left1.config(text=min_sec_format)
    with open("output/penalty_left_first.txt", "w") as file:
        file.write(str(min_sec_format))


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
    global penalty_left_second_time
    check2left = chk_penalty_left_second_state.get()
    if check2left == False:
        penalty_left_second_time = 120
        lbl_penalty_left2.config(text="02:00")
    global penalty_left_second_started
    global penalty_left_second_paused
    penalty_left_second_started = check2left
    penalty_left_second_paused = not penalty_left_second_started
    m, s = divmod(penalty_left_second_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    with open("output/penalty_left_second.txt", "w") as file:
        file.write(str(min_sec_format))


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
    with open("output/penalty_left_second.txt", "w") as file:
        file.write(str(min_sec_format))


def nClick_penalty_left_second_minutes_down():
    global penalty_left_second_time
    penalty_left_second_time -= 60
    if penalty_left_second_time < 0:
        penalty_left_second_time = 0
    m, s = divmod(penalty_left_second_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_left2.config(text=min_sec_format)
    with open("output/penalty_left_second.txt", "w") as file:
        file.write(str(min_sec_format))


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
    global penalty_right_first_time
    check1right = chk_penalty_right_first_state.get()
    if check1right == False:
        penalty_right_first_time = 120
        lbl_penalty_right1.config(text="02:00")
    global penalty_right_first_started
    global penalty_right_first_paused
    penalty_right_first_started = check1right
    penalty_right_first_paused = not penalty_right_first_started
    m, s = divmod(penalty_right_first_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    with open("output/penalty_right_first.txt", "w") as file:
        file.write(str(min_sec_format))


def set_penalty_right_first():
    check1right = chk_penalty_right_first_state.get()
    if check1right == False:
        chk_penalty_right_first_state.set(True)
    else:
        chk_penalty_right_first_state.set(False)
    chk_penalty_right_first()


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
    with open("output/penalty_right_first.txt", "w") as file:
        file.write(str(min_sec_format))


def nClick_penalty_right_first_minutes_down():
    global penalty_right_first_time
    penalty_right_first_time -= 60
    if penalty_right_first_time < 0:
        penalty_right_first_time = 0
    m, s = divmod(penalty_right_first_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_right1.config(text=min_sec_format)
    with open("output/penalty_right_first.txt", "w") as file:
        file.write(str(min_sec_format))


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
    global penalty_right_second_time
    check2right = chk_penalty_right_second_state.get()
    if check2right == False:
        penalty_right_second_time = 120
        lbl_penalty_right2.config(text="02:00")
    global penalty_right_second_started
    global penalty_right_second_paused
    penalty_right_second_started = check2right
    penalty_right_second_paused = not penalty_right_second_started
    m, s = divmod(penalty_right_second_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    with open("output/penalty_right_second.txt", "w") as file:
        file.write(str(min_sec_format))


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
    with open("output/penalty_right_second.txt", "w") as file:
        file.write(str(min_sec_format))


def nClick_penalty_right_second_minutes_down():
    global penalty_right_second_time
    penalty_right_second_time -= 60
    if penalty_right_second_time < 0:
        penalty_right_second_time = 0
    m, s = divmod(penalty_right_second_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_penalty_right2.config(text=min_sec_format)
    with open("output/penalty_right_second.txt", "w") as file:
        file.write(str(min_sec_format))


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
    with open("output/main_timer.txt", "w") as file:
        file.write(str(min_sec_format))


def nClick_minutes_down():
    global period_time
    period_time -= 60
    if period_time < 0:
        period_time = 0
    m, s = divmod(period_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_timer.config(text=min_sec_format)
    with open("output/main_timer.txt", "w") as file:
        file.write(str(min_sec_format))


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
    with open("output/main_timer.txt", "w") as file:
        file.write(str(min_sec_format))


def nClick_seconds_down():
    global period_time
    period_time -= 1
    if period_time < 0:
        period_time = 0
    m, s = divmod(period_time, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    lbl_timer.config(text=min_sec_format)
    with open("output/main_timer.txt", "w") as file:
        file.write(str(min_sec_format))


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
    global clean_time
    period_time = 0
    clean_time = 0
    clean_timer.config(text="00:00")
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
    with open("output/clean_time.txt", "w") as file:
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
    global clean_time
    global statistics_params
    global statistics_widgets
    statistics_widgets = {}
    period_time = 0
    clean_time = 0
    clean_timer.config(text="00:00")
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
    with open("output/clear_time.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_left_first.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_left_second.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_right_first.txt", "w") as file:
        file.write("00:00")
    with open("output/penalty_right_second.txt", "w") as file:
        file.write("00:00")
    with open("output/clean_time.txt", "w") as file:
        file.write("00:00")
    with open("output/shot_team1.txt", "w") as file:
        file.write('0')
    with open("output/shot_gates_team1.txt", "w") as file:
        file.write('0')
    with open("output/face_off_team1.txt", "w") as file:
        file.write('0')
    with open("output/penalty_team1.txt", "w") as file:
        file.write('0')
    with open("output/shot_team2.txt", "w") as file:
        file.write('0')
    with open("output/shot_gates_team2.txt", "w") as file:
        file.write('0')
    with open("output/face_off_team2.txt", "w") as file:
        file.write('0')
    with open("output/penalty_team2.txt", "w") as file:
        file.write('0')
    with open("output/safety_factor_team1.txt", "w") as file:
        file.write('0')
    with open("output/safety_factor_team2.txt", "w") as file:
        file.write('0')
    statistics_params = empty_statistics_params()
    #update_statistics_values()
    shutil.copyfile("pict/1.png", "output/left_1.png")
    shutil.copyfile("pict/1.png", "output/left_2.png")
    shutil.copyfile("pict/1.png", "output/left_3.png")
    shutil.copyfile("pict/1.png", "output/left_4.png")
    shutil.copyfile("pict/1.png", "output/left_5.png")
    shutil.copyfile("pict/1.png", "output/right_1.png")
    shutil.copyfile("pict/1.png", "output/right_2.png")
    shutil.copyfile("pict/1.png", "output/right_3.png")
    shutil.copyfile("pict/1.png", "output/right_4.png")
    shutil.copyfile("pict/1.png", "output/right_5.png")


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
        if min_sec_format == "-1:59":
            m, s = divmod(period_time, 60)
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
    if period_time <= 0:
        return
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
    window.focus_set()


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
shutil.copyfile("pict/1.png", "output/left_1.png")
shutil.copyfile("pict/1.png", "output/left_2.png")
shutil.copyfile("pict/1.png", "output/left_3.png")
shutil.copyfile("pict/1.png", "output/left_4.png")
shutil.copyfile("pict/1.png", "output/left_5.png")
shutil.copyfile("pict/1.png", "output/right_1.png")
shutil.copyfile("pict/1.png", "output/right_2.png")
shutil.copyfile("pict/1.png", "output/right_3.png")
shutil.copyfile("pict/1.png", "output/right_4.png")
shutil.copyfile("pict/1.png", "output/right_5.png")


# Add clean time
def tick_tack():
    global clean_time, after_id
    after_id = window.after(1000, tick_tack)
    f_temp = datetime.fromtimestamp(clean_time).strftime('%M:%S')
    clean_time += 1
    clean_timer.config(text=f_temp)
    with open("output/clean_time.txt", "w") as file:
        file.write(str(f_temp))


def start_sw():
    global clean_time
    global clean_time_started
    if clean_time_started:
        return
    else:
        clean_time_started = True
        clean_time = 0
        tick_tack()


def stop_sw():
    global clean_time_started
    clean_time_started = False
    window.after_cancel(after_id)


clean_timer = Label(window, text=clean_time, bg="black", fg="#fe0000", font=("digital numbers", 17))
clean_timer.place(x=573, y=95, width=90, height=33)
lbl_clean_name = Label(window, text="Cl.time", bg="#404040", fg="white", font=("square sans serif 7", 14))
lbl_clean_name.place(x=573, y=70)

# Add Statistics
statistics_params = {'shot_team1': 0, 'shot_gates_team1': 0, 'face_off_team1': 0, 'penalty_team1': 0, 'shot_team2': 0,
                     'shot_gates_team2': 0, 'face_off_team2': 0, 'penalty_team2': 0, 'safety_factor_team1' : 0, 'safety_factor_team2' : 0, }

def empty_statistics_params():
    return {'shot_team1': 0, 'shot_gates_team1': 0, 'face_off_team1': 0, 'penalty_team1': 0, 'shot_team2': 0,
                     'shot_gates_team2': 0, 'face_off_team2': 0, 'penalty_team2': 0, 'safety_factor_team1' : 0, 'safety_factor_team2' : 0, }

def shot_team1():
    global statistics_params
    statistics_params['shot_team1'] += 1
    with open("output/shot_team1.txt", "w") as file:
        file.write(str(statistics_params['shot_team1']))
    update_statistics_values()

def shot_gates_team1():
    global statistics_params
    statistics_params['shot_gates_team1'] += 1
    with open("output/shot_gates_team1.txt", "w") as file:
        file.write(str(statistics_params['shot_gates_team1']))
    safety_factor_team2()
    update_statistics_values()

def face_off_team1():
    global statistics_params
    statistics_params['face_off_team1'] += 1
    with open("output/face_off_team1.txt", "w") as file:
        file.write(str(statistics_params['face_off_team1']))
    update_statistics_values()

def penalty_team1():
    global statistics_params
    statistics_params['penalty_team1'] += 1
    with open("output/penalty_team1.txt", "w") as file:
        file.write(str(statistics_params['penalty_team1']))
    update_statistics_values()

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


# Add hotkeys
bindings = [
    [["left_control"], None, nClick_score_left_up],
    [["+"], None, nClick_seconds_up],
    [["-"], None, nClick_seconds_down],
    [["0"], None, nClick_minutes_up],
    [["9"], None, nClick_minutes_down],
    [["8"], None, nClick_period_up],
    [["6"], None, start_sw],
    [["7"], None, stop_sw],
    [["right_control"], None, nClick_score_right_up],
    [["z"], None, set_penalty_left_first],
    [["/"], None, set_penalty_right_first],
    [["space"], None, pause],
    [["f2"], None, shot_team1],
    [["f3"], None, shot_gates_team1],
    [["f4"], None, face_off_team1],
    [["f5"], None, penalty_team1],
    [["f6"], None, shot_team2],
    [["f7"], None, shot_gates_team2],
    [["f8"], None, face_off_team2],
    [["f9"], None, penalty_team2],
    [["enter"], None, lambda: start_main_timer(period_time)],

]
register_hotkeys(bindings)

window.mainloop()
