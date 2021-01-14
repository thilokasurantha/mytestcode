from tkinter import *
root = Tk()
root.geometry("1350x700+0+0")

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

root.mainloop()