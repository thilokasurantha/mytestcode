from tkinter import *
root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

filebar  = Menu(menubar)
menubar.add_cascade(label="File")
filebar.add_command(label="Bye")
menubar.add_separator()
root.mainloop()