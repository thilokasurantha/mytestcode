from tkinter import *
from tkinter import messagebox

import database
import score
import registration

class EditAndAddSubjects :
    def __init__(self, edit, first) -> None:
        self.edit = edit
        self.first = first

    def window(self) :
        frame = Frame(self.edit)
        frame.pack()

        add_subject = Button(frame, text="Add New Subject", font=("Source Sans Pro",12,'bold'), width=40, height=4, command=self.add_new_subject)
        add_subject.pack()
        succeed = Button(frame, text="Succeed", font=("Source Sans Pro",12,'bold'), width=40, height=4, command=self.complete)
        succeed.pack()


        self.edit.mainloop()

    def add_new_subject(self) :
        self.s_name = Entry(self.edit)
        self.s_name.insert(0, "Enter Subject")
        self.s_name.pack(side=LEFT)
        self.s_marks = Entry(self.edit)
        self.s_marks.pack(side=LEFT)
        self.s_marks.insert(0, "Enter Marks")
        self.s_btn = Button(self.edit, text="add", command=self.add)
        self.s_btn.pack(side=RIGHT)

    def add(self) :
        s_names = self.s_name.get()
        u_names = self.first
        s_mark = self.s_marks.get()

        self.s_name.forget()
        self.s_btn.forget()
        self.s_marks.forget()

        add = database.DatabaseHandlerForSubjects(s_names, u_names, s_mark)
        result = add.db_handler_subjects()

        if result :
           show_name = Button(self.edit, text=f"{s_names} : {s_mark}", font=("Source Sans Pro",12,'bold'), width=40, justify="left")
           show_name.pack()
 
        else :
            messagebox.showerror("Error", "This Subject is alredy in the database.")

    def complete(self) :
        self.edit.destroy()

        register = registration.RegistrationForm(Tk())
        register.registration_form()