from tkinter import *
from tkinter import messagebox
import database
import items
import subjects
import scores
import checking

class NewStudent :
    def __init__(self, student) -> None:
        self.student = student

    def add_new_students(self) :
        self.student.title("Add New Student")

        self.fname_lbl = Label(self.student, text="First Name\t")
        self.fname_lbl.grid(row=1, column=0)
        self.fname = Entry(self.student)
        self.fname.grid(row=1, column=1)

        self.lname_lbl = Label(self.student, text="Last Name\t")
        self.lname_lbl.grid(row=2, column=0)
        self.lname = Entry(self.student)
        self.lname.grid(row=2, column=1)

        self.add_student = Button(self.student, text="add new student" , width=13, command=self.database_student)
        self.add_student.grid(row=1,column=2,sticky=W)
        self.close = Button(self.student, text="close",  width=13, command=self.close)
        self.close.grid(row=2, column=2,sticky=W)

    def database_student(self) :
        get_items = checking.name_check(self.fname.get())
        if get_items :
            student_data = database.DatabaseHandlerForStudent(self.fname.get(), self.lname.get())
            student_data.database_for_student()

            self.student.destroy()

            add_subjects = subjects.Subject(Tk(), self.fname.get(), self.lname.get())
            add_subjects.add_new_subjects()

        else :
            messagebox.showwarning("Warnning", "You are already logged in.")
            
    def close(self) :
        pass


