from tkinter import *
class MakeGUI :
    def __init__(self,root) :
        self.root = root
    def making(self) :
        self.label = Label(self.root , text="this is a label")
        self.label.pack()
        self.root.mainloop()
x = MakeGUI(Tk())
x.making()