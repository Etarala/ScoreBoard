from tkinter import *

import time
window = Tk()
window.title("Score Panel")
window.geometry('815x500')



class Clock():
    def __init__(self):
        self.root = tkinter.window()
        self.label = tkinter.Label(text='', bg="black", fg="#fe0000", font=("digital numbers", 60))
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app = Clock()
'''lbl_timer = Label(window, text=main_timer, bg="black", fg="#fe0000", font=("digital numbers", 60))
lbl_timer.place(x=250, y=70, width=320, height=100)'''

'''btn_start_main_timer = Button(window, text="START/PAUSE", font=("square sans serif 7", 20), command=app,
                     relief='flat', bg='black', fg='#fe0000', borderwidth=0)
btn_start_main_timer.place(x=275, y=230)'''


#window.mainloop()