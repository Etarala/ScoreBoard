import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Score Panel")
        self.geometry('815x500')
        self.resizable(width=0, height=0)

        self.initUI()

        self.mainloop()

    def initUI(self):
        tk.Button(self, text='Click me!', command=self.button1click).grid(column=0, row=0)
        tk.Button(self, text='Click me! again').grid(column=1, row=0)

    def button1click(self):
        popup = tk.Toplevel(self)
        popup.geometry('200x100')
        popup.title('I am a popup!')
        tk.Label(popup, text="I am a popup!").place(x=0,y=0)