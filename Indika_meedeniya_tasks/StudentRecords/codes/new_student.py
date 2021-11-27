from tkinter import *
from tkinter import messagebox
import main as main
import database as db


class NewStudent :
    def __init__(self, std):
        self.std = std

    def add_new_student_window(self):
        self.std.title("Add New Student")

        fname_lbl = Label(self.std, text="First Name\t")
        fname_lbl.grid(row=1, column=0)
        self.fname = Entry(self.std)
        self.fname.grid(row=1, column=1)

        lname_lbl = Label(self.std, text="Last Name\t")
        lname_lbl.grid(row=2, column=0)
        self.lname = Entry(self.std)
        self.lname.grid(row=2, column=1)

        add_student = Button(self.std, text="add new student", command=self.add_student_db, width=13)
        add_student.grid(row=1,column=2,sticky=W)
        close = Button(self.std, text="close", command=self.student_close, width=13)
        close.grid(row=2, column=2,sticky=W)

    def add_student_db(self) :
        first_name = self.fname.get()
        last_name = self.lname.get()
        
        myDatabaseHandler = db.DatabaseHandlerForNames(first_name, last_name)
        boolean_value = myDatabaseHandler.database_handler_for_names()

        if  boolean_value:
            info = messagebox.showinfo("Information", "You are now registered.")

            if info :
                self.std.destroy()
                StudentRecordWindow = main.MainStudentRecordGUI(Tk())
                StudentRecordWindow.create_window()

        else :
            messagebox.showwarning("Warning", "You are already logged.")
            self.fname.delete(0,END)
            self.lname.delete(0,END)
        
    def student_close(self) :
        self.std.destroy()
        StudentRecordWindow = main.MainStudentRecordGUI(Tk())
        StudentRecordWindow.create_window()