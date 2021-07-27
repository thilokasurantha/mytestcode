from tkinter import *
def search_function():
    pass
def making_gui(root) :
    # Billin Software making Label

    text_billing_system_frame = LabelFrame(root, fg="red", bg="#054465", relief=RAISED, bd=10)
    text_billing_system_frame.pack(fill=X)

    biling_system = Label(text_billing_system_frame, text="Billing Software", font=("Britannic Bold", 28), justify="center", fg="#EAD03D", bg="#054465")
    biling_system.pack()
    # Customer Details
    text_costomer_details = LabelFrame(root, text="Customer Details", fg="#EAD03D", bg="#054465", font=("Britannic Bold", 11), relief=RAISED, bd=10)
    text_costomer_details.pack(fill=X)

    customer_name = Label(text_costomer_details, text="Customer Name ", font=("Britannic Bold", 13), bg="#054465",fg="white")
    customer_name.pack(side=LEFT)
    customer_name_entry = Entry(text_costomer_details, font=("Britannic Bold", 13))
    customer_name_entry.pack(side=LEFT)

    con_num = Label(text_costomer_details, text="Contact No. ", font=("Britannic Bold", 13), bg="#054465", fg="white")
    con_num.pack(side=LEFT)
    con_num_entry = Entry(text_costomer_details, font=("Britannic Bold", 13))
    con_num_entry.pack(side=LEFT)

    bill_no = Label(text_costomer_details, text="Bill Nomber ", font=("Britannic Bold", 13), bg="#054465", fg="white")
    bill_no.pack(side=LEFT)
    bill_no_entry = Entry(text_costomer_details, font=("Britannic Bold", 13))
    bill_no_entry.pack(side=LEFT)

    serach = Button(text_costomer_details, text="search", command=search_function, width=35,font=("Britannic Bold", 10))
    serach.pack(side=RIGHT)

    # Cosmetics
    cosmetics_frame = LabelFrame(root, text="Customer Details", fg="#EAD03D", bg="#054465", font=("Britannic Bold", 11), relief=RAISED, bd=10)
    cosmetics_frame.pack(fill=Y,side=LEFT)

    bath_suop = Label(cosmetics_frame,text="Bath Soup ",font=("Britannic Bold", 13), bg="#054465",fg="#90EEAD")
    bath_suop.pack(side=LEFT,anchor=N)
    bath_suop_entry = Entry(cosmetics_frame, font=("Britannic Bold", 13), width=10)
    bath_suop_entry.pack(side=RIGHT,anchor=N)

    face_cream = Label(cosmetics_frame, text="Face Cream ", font=("Britannic Bold", 13), bg="#054465", fg="#90EEAD")
    face_cream.place(y=25)
    face_cream_entry = Entry(cosmetics_frame, font=("Britannic Bold", 13),width=10)
    face_cream_entry.place(y=25,x=88)

    face_wash = Label(cosmetics_frame, text="Face Wash ", font=("Britannic Bold", 13), bg="#054465", fg="#90EEAD")
    face_wash.place(y=50)
    face_wash_entry = Entry(cosmetics_frame, font=("Britannic Bold", 13),width=10)
    face_wash_entry.place(y=50,x=88)

root = Tk()
gui_width = 1280
gui_height = 720

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = (screen_width//2 - gui_width//2)
center_y = (screen_height//2 - gui_height//2)

root.geometry("{}x{}+{}+{}".format(gui_width, gui_height, center_x, center_y))
making_gui(root)
root.mainloop()



