from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")


def dot():
    dots = [":", " "]
    seconds = strftime("%S")
    if (int(seconds) % 2) == 0:
        dt_1 = str(dots[0])
        return (dt_1)
    else:
        dt_2 = str(dots[1])
        return (dt_2)


def time():
    string = strftime("%I{0}%M{1}%S %p".format(dot(), dot()))
    label.config(text=string)
    label.after(1000, time)


# bg = #1B1E26
# fg = #FFE222
label = Label(root, font=("digital numbers", 70), background="#1B1E26", foreground="#FFE222")
label.pack(anchor="center")
label.master.overrideredirect(True)
label.master.geometry('+10+930')
# label.master.wm_attributes("-transparentcolor","#FFE221")
# label.master.wm_attributes("-alpha",0.5)
label.master.wm_attributes("-topmost", True)
label.master.lift()
time()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
print(ws, 'x', hs)
mainloop()
