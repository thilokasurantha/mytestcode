from doctest import master
from re import X
import tkinter as tk
from turtle import left

class MyApp(object):
    def __init__(self, master):
        self.text = tk.Text(master)
        self.text.bind('<space>', self.callback)
        self.text.pack()

    def callback(self, event):
        print()

root = tk.Tk()
app = MyApp(root)
root.mainloop()