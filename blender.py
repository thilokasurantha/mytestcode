from tkinter import *
from tkinter import messagebox


def OK():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("" ,"INCORRECT")
    elif (uname == "thiloka" and password == "thiloka123"):
        messagebox.showinfo("", "CORRECT")
        root = Tk()
        
        def add():
        
            e3 = Entry(root)
            e3.grid(row=2 , column=3)
            
        add = Button(root , text="ADD" , command=add , font=("Bold" , 10))
        add.grid(row=1 , column=1)


        
        root.mainloop()
    else :
         messagebox.showinfo("", "INCORRECT USERNAME OR PASSWORD")


root = Tk()
root.title("Login To The Software")
root.iconbitmap('favicon.ico')

global e1
global e2


Label_1 = Label(root, text="Enter Your Username :" , font=("Broadway" , 12))
Label_2 = Label(root, text="Enter Your Password :" , font=("Broadway" , 12))
Label_1.grid(row=1 , column=1)
Label_2.grid(row=3 , column=1)

e1 = Entry(root)
e2 = Entry(root)
e2.grid(row=3 , column=2)
e2.config(show="*")

e1.grid(row=1 , column=2)


Button_1 = Button(root , text="SUBMIT" , width=8 , height=2 , command=OK)
Button_1.grid(row=5 , column=1)



root.mainloop()