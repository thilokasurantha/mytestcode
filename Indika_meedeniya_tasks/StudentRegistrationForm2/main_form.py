from tkinter import *
from tkinter.messagebox import showerror
import new_student
import database
import sqlite3
import new_subject
import add_marks

class MainForm :
    def __init__(self, tk) -> None:
        self.tk = tk
        connect = sqlite3.connect("/media/thlioka-ubuntu/Programming/GIT_UBUNTU/mytestcode/Indika_meedeniya_tasks/StudentRegistrationForm2/details.db")
        cursor = connect.cursor()
        self.db_handler = database.DatabaseHandler(connect, cursor)

    def form(self) :
        self.tk.title("Main Form")
        self.tk.resizable(False, False)

        new_student = Button(self.tk, text="Add New Student", font=("Source Sans Pro",12,'bold'), command=self.add_new_students, width=20, height=5)
        new_student.grid(row=0, column=0)

        new_subject = Button(self.tk, text="Add New Subject", font=("Source Sans Pro",12,'bold'), command=self.add_new_subjects, width=20, height=5)
        new_subject.grid(row=1, column=0)

        new_marks = Button(self.tk, text="Add New Marks", font=("Source Sans Pro",12,'bold'), command=self.add_new_marks, width=20, height=5)
        new_marks.grid(row=2, column=0)

        print_student = Button(self.tk, text="Print All Student", font=("Source Sans Pro",12,'bold'), command=self.print_all_students, width=20, height=5)
        print_student.grid(row=0, column=1)

        print_subject = Button(self.tk, text="Print All Subject", font=("Source Sans Pro",12,'bold'), command=self.print_all_subjects, width=20, height=5)
        print_subject.grid(row=1, column=1)

        print_marks = Button(self.tk, text="Print All Marks", font=("Source Sans Pro",12,'bold'), command=self.print_all_marks , width=20, height=5)
        print_marks.grid(row=2, column=1)

        self.tk.mainloop()

    def print_all_students(self) :
        showStds = self.db_handler.print_all_students()
        print("This is Students Name List")
        for i in showStds :
            print(i.show_student_details())

    def print_all_subjects(self) :
        showSubs = self.db_handler.print_all_subjects()
        print("This is Students Subjects List")
        for j in showSubs :
            print(j.show_subject_details())

    def print_all_marks(self) :
        showMrks = self.db_handler.print_all_marks()

        for k in showMrks :
            print(k.show_marks_details())

    def add_new_students(self) :
        self.tk.destroy()

        newStd = new_student.NewStudentForm(Tk(), self.db_handler)
        newStd.form()

    def add_new_subjects(self) :
        self.tk.destroy()

        newSub = new_subject.NewSubjects(Tk(), self.db_handler)
        newSub.new_subjects_form()

    def add_new_marks(self) :
        self.tk.destroy()

        newMrk = add_marks.NewMarksForm(Tk(), self.db_handler)
        newMrk.new_marks_form()

if __name__ == "__main__" :
    myObj = MainForm(Tk())
    myObj.form()
    