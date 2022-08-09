"""

- Добавить настройку отключения горячих клавишь
- Добавить буллиты
- Добавить составы команд

"""
from tkinter import *
from tkinter import ttk

root = Tk()
note = ttk.Notebook(root)

ms = ttk.Frame(note)
note.add(ms, text = "Main-Screen")
mn = ttk.Frame(note)
note.add(mn, text = "Manual")
note.pack()

root.mainloop()