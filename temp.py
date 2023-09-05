import tkinter as tk
import time

class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Таймер обратного отсчета")
        self.master.geometry("300x150")

        self.label = tk.Label(self.master, text="5:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.master, text="Старт", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.master, text="Стоп", command=self.stop_timer)
        self.stop_button.pack(side=tk.RIGHT, padx=10)

        self.reverse_button = tk.Button(self.master, text="Обратный таймер", command=self.reverse_timer)
        self.reverse_button.pack(side=tk.BOTTOM, pady=20)

        self.seconds_left = 0
        self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            self.seconds_left = 300
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False

    def update_timer(self):
        minutes, seconds = divmod(self.seconds_left, 60)
        time_str = "{:02d}:{:02d}".format(minutes, seconds)
        self.label.configure(text=time_str)

        if self.timer_running and self.seconds_left > 0:
            self.seconds_left -= 1
            self.master.after(1000, self.update_timer)
        elif self.seconds_left == 0:
            self.timer_running = False

    def reverse_timer(self):
        if not self.timer_running:
            self.seconds_left = 0
            self.timer_running = True
            self.update_reverse_timer()

    def update_reverse_timer(self):
        minutes, seconds = divmod(self.seconds_left, 60)
        time_str = "{:02d}:{:02d}".format(minutes, seconds)
        self.label.configure(text=time_str)

        if self.timer_running and self.seconds_left < 300:
            self.seconds_left += 1
            self.master.after(1000, self.update_reverse_timer)
        elif self.seconds_left == 300:
            self.timer_running = False

root = tk.Tk()
timer = Timer(root)
root.mainloop()