from tkinter import *

root = Tk()
test = Text(root,length=600)
print(len(test))
test.insert(END, "Thlioka")
test.pack()

root.mainloop()
