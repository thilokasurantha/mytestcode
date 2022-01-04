from tkinter import *
from tkinter import messagebox
import random
import database
import edit

class RegistrationForm :
    def __init__(self, reg) -> None:
        self.reg = reg

    def registration_form(self) :
        frame_4 = Frame(self.reg)
        frame_4.grid(row=4)

        self.label_1 = Label(self.reg, text="First Name", font=("Source Sans Pro",12,'bold'))
        self.label_1.grid(row=1,column=0, sticky=W)
        self.fname = Entry(self.reg, font=("Source Sans Pro",12,'bold'))
        self.fname.grid(row=1,column=1)

        self.label_2 = Label(self.reg, text="Last Name", font=("Source Sans Pro",12,'bold'))
        self.label_2.grid(row=2,column=0, sticky=W)
        self.lname = Entry(self.reg, font=("Source Sans Pro",12,'bold'))
        self.lname.grid(row=2,column=1)

        self.genarate = Button(frame_4, text="GENARATE", font=("Source Sans Pro",12,'bold'), command=self.genarate_form)
        self.genarate.grid(row=4,column=0, sticky=W)
        self.close = Button(frame_4, text="CLOSE", font=("Source Sans Pro",12,'bold'), command=self.close_window)
        self.close.grid(row=4, column=1, sticky=W)

        self.reg.mainloop()

    def genarate_form(self) :
        f = self.fname.get()
        l = self.lname.get()

        genarate = database.DatabaseHandlerForNames(f,l) 
        answer = genarate.db_handler_names()

        if answer :
            messagebox.showwarning("Warrning", "You are already logged in.")

        else :
            messagebox.showinfo("Information", "Successfully Saved in a database")

            self.reg.destroy()

            subject = edit.EditAndAddSubjects(Tk(), f)
            subject.window()

    def close_window(self) :
        pass

if __name__ == "__main__" :
    register = RegistrationForm(Tk())
    register.registration_form()