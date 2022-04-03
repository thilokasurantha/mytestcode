# Import Libraries, Files
import sqlite3
from tkinter import *
from tkinter import messagebox
import database
import new_student
import new_subject
import new_mark

# Call To The Database, Class Database
db_connect = sqlite3.connect("details.db")
db_cursor = db_connect.cursor()

# Tkinter Main Form
class MainForm :
    def __init__(self, tk) -> None:
        self.tk = tk
        self.db_handler = database.DatabaseHandler(db_connect, db_cursor)

    def main_form(self) :
        self.tk.title("Main Form")
        self.tk.resizable(False, False)

        new_student = Button(self.tk, text="Add New Student", font=("Source Sans Pro",12,'bold'), command=self.add_students, width=20, height=5)
        new_student.grid(row=0, column=0)

        new_subject = Button(self.tk, text="Add New Subject", font=("Source Sans Pro",12,'bold'), command=self.add_subjects, width=20, height=5)
        new_subject.grid(row=1, column=0)

        new_marks = Button(self.tk, text="Add New Marks", font=("Source Sans Pro",12,'bold'), command=self.add_marks, width=20, height=5)
        new_marks.grid(row=2, column=0)

        print_student = Button(self.tk, text="Print All Student", font=("Source Sans Pro",12,'bold'), command=self.print_all_students, width=20, height=5)
        print_student.grid(row=0, column=1)

        print_subject = Button(self.tk, text="Print All Subject", font=("Source Sans Pro",12,'bold'), command=self.print_all_subjects, width=20, height=5)
        print_subject.grid(row=1, column=1)

        print_marks = Button(self.tk, text="Print All Marks", font=("Source Sans Pro",12,'bold'), command=self.print_all_marks , width=20, height=5)
        print_marks.grid(row=2, column=1)

        self.tk.mainloop()

    def add_students(self) :
        self.tk.destroy()

        myNewStudent = new_student.NewStudentsForm(Tk(), self.db_handler)
        myNewStudent.students_form()

    def add_subjects(self) :
        self.tk.destroy()

        myNewSubject = new_subject.NewSubjectsForm(Tk(), self.db_handler)
        myNewSubject.subject_form()

    def add_marks(self) :
        self.tk.destroy()

        myNewScores = new_mark.NewMarksForm(Tk(), self.db_handler)
        myNewScores.marks_form()

    def print_all_students(self) :
        get_students = self.db_handler.get_all_students()

        for i in get_students :
            print(i.show_student_details())

    def print_all_subjects(self) :
        get_subjects = self.db_handler.get_all_subjects()

        for j in get_subjects :
            print(j.show_subject_details())

    def print_all_marks(self) :
        self.std_id = []
        self.sub_id = []
        self.std_name = []
        self.sub_name = []

        get_students = self.db_handler.get_all_students()
        get_subjects = self.db_handler.get_all_subjects()

        for i in get_students :
            self.std_id.append(i.student_id)
            self.std_name.append(i.first_name + " " + i.last_name)

        for j in get_subjects :
            self.sub_name.append(j.subject_name)
            self.sub_id.append(j.subject_id)
        get_marks = self.db_handler.get_all_marks()

        for j in get_marks :
            std = self.std_name[j.student_id-1]
            sub = self.sub_name[j.subject_id-1]
            scr = j.score

            print("Student Name : {}, Subject Name : {}, Score : {}".format(std, sub, scr))
            
if __name__ == "__main__" :
    myMainForm = MainForm(Tk())
    myMainForm.main_form()
