from tkinter import *
import main_form 
from tkinter import messagebox

class NewStudentForm :
    def __init__(self, tk, db_handler) -> None:
        self.tk = tk
        self.db_handler = db_handler

    def form(self) :
        self.fname_lbl = Label(self.tk, text="First Name", font=("Soerce Sans Pro",12,'bold'))
        self.fname_lbl.grid(row=0, column=0)
        self.fname = Entry(self.tk, font=("Source Sans Pro",12,'bold'))
        self.fname.grid(row=0, column=1)

        self.lname_lbl = Label(self.tk, text="Last Name", font=("Source San Pro",12,'bold'))
        self.lname_lbl.grid(row=1,column=0)
        self.lname = Entry(self.tk, font=("Source Sans Pro",12,'bold'))
        self.lname.grid(row=1,column=1)

        self.submit_btn = Button(self.tk, text="SUBMIT", font=("Source Sans Pro",12,'bold'), command=self.submit)
        self.submit_btn.grid(row=2, column=0)
        self.cancle = Button(self.tk, text="CLOSE", font=("Source Sans Pro",12,'bold'), command=self.close)
        self.cancle.grid(row=2, column=1)

        self.tk.mainloop()

    def submit(self) :
        first_name = self.fname.get()
        last_name = self.lname.get()

        checkStd = self.db_handler.check_students(first_name, last_name)

        if checkStd == True :
            self.db_handler.add_new_students(first_name, last_name)

            btn = messagebox.showinfo("Information", "Your Details are successfully saved on database.")

            if btn == "ok" :
                self.clear_form()

        else :
            warning = messagebox.showwarning("Warning", "You are already sing in the database\n {}".format(checkStd))

            if warning == "ok" :
                self.clear_form()

    def  clear_form(self):
        self.fname.delete(0, END)
        self.lname.delete(0, END)

    def close(self) :
        self.tk.destroy()
        
        cancle = main_form.MainForm(Tk())
        cancle.form()
