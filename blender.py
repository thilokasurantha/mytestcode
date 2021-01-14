from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login To The Software")
root.iconbitmap('favicon.ico')


def OK():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("" ,"INCORRECT")
    elif (uname == "thiloka" and password == "thiloka123"):
        messagebox.showinfo("", "CORRECT")

        root = Tk()
        root.geometry("1350x700+0+0")
        root.title("Billing Software")
        root.iconbitmap("favicon (1).ico")

        Label_1 = Label(root, text="Billing Software" , font=("Berlin Sans FB Demi" , 26))
        Label_1.pack()

        Label_frame = LabelFrame(root, text="Costomer Details" , font=("Berlin Sans FB Demi" , 14))
        Label_frame.pack(expand='yes' , fill = 'both')

        cn = Label(Label_frame, text="Costomer Name :" ,  font=("Berlin Sans FB Demi" , 15))
        cn.grid(row=1 , column=1, padx=10)

        cnb = Entry(Label_frame )
        cnb.grid(row=1 , column=2, padx=10)

        cnom = Label(Label_frame,text="Costomer Number :" ,  font=("Berlin Sans FB Demi" , 15))
        cnom.grid(row=1 , column=5, padx=10)

        cnb = Entry(Label_frame )
        cnb.grid(row=1 , column=6, padx=10)

        bn = Label(Label_frame,text="Bill Number :" ,  font=("Berlin Sans FB Demi" , 15))
        bn.grid(row=1 , column=7, padx=10)

        cnb = Entry(Label_frame )
        cnb.grid(row=1 , column=8 , padx=10)

        btn1 = Button(Label_frame, text="Search" ,width=8 , height=1)
        btn1.grid(row=1 , column=17,padx=10)

        Label_frame = LabelFrame(root)
        Label_frame.pack(expand='yes' , fill = 'both')

        root.mainloop()
        #thiloka


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