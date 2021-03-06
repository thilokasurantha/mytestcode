from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login To The Calculator")

def OK():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("" ,"INCORRECT")

    elif (uname == "thiloka" and password == "thiloka123"):
        messagebox.showinfo("", "CORRECT")
        
        root = Tk()
        root.title("calculator")

        e = Entry(root, width=35, borderwidth=5)
        e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


        def button_click(number):
            current = e.get()
            e.delete(0, END)
            e.insert(0, str(current) + str(number))


        def button_clear():
            e.delete(0, END)


        def button_add():
            first_number = e.get()
            global f_num
            global math
            math = "addition"
            f_num = int(first_number)
            e.delete(0, END)


        def button_equal():
            second_number = e.get()
            e.delete(0, END)
            if math == "addition":
                e.insert(0, f_num + int(second_number))
            if math == "subtraction":
                e.insert(0, f_num - int(second_number))
            if math == "multipication":
                e.insert(0, f_num * int(second_number))
            if math == "division":
                e.insert(0, f_num / int(second_number))


        def button_subtract():
            first_number = e.get()
            global f_num
            global math
            math = "subtraction"
            f_num = int(first_number)
            e.delete(0, END)


        def button_multiply():
            first_number = e.get()
            global f_num
            global math
            math = "multipication"
            f_num = int(first_number)
            e.delete(0, END)


        def button_divide():
            first_number = e.get()
            global f_num
            global math
            math = "division"
            f_num = int(first_number)
            e.delete(0, END)


        Button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
        Button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
        Button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
        Button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
        Button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
        Button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
        Button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
        Button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
        Button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
        Button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
        Button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
        Button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
        Button_clear = Button(root, text="clear", padx=79, pady=20, command=button_clear)

        Button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
        Button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
        Button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

        Button_1.grid(row=3, column=0)
        Button_2.grid(row=3, column=1)
        Button_3.grid(row=3, column=2)

        Button_4.grid(row=2, column=0)
        Button_5.grid(row=2, column=1)
        Button_6.grid(row=2, column=2)

        Button_7.grid(row=1, column=0)
        Button_8.grid(row=1, column=1)
        Button_9.grid(row=1, column=2)

        Button_0.grid(row=4, column=0)
        Button_clear.grid(row=4, column=1, columnspan=2)
        Button_add.grid(row=5, column=0)
        Button_equal.grid(row=5, column=1, columnspan=2)

        Button_subtract.grid(row=6, column=0)
        Button_multiply.grid(row=6, column=1)
        Button_divide.grid(row=6, column=2)

        root.mainloop()
        
    else :
         messagebox.showinfo("", "INCORRECT USERNAME OR PASSWORD")

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
