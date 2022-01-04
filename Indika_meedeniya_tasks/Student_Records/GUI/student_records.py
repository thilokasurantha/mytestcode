from os import name
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import sutudent_marks as marks

class StudentRecordGui :
    def __init__(self, window):
        self.window = window

    def student_record_design(self):
        self.window.title("Student Window GUI")

        self.f_name = ttk.Label(self.window, text="First Name\t",font=("Source Sans Pro",12,'bold'))
        self.f_name.grid(row=1,column=0,sticky=W)
        self.f_name_entry = Entry(self.window, font=("Source Sans Pro",12,'bold'))
        self.f_name_entry.grid(row=1,column=1,sticky=W)

        self.l_name = ttk.Label(self.window, text="Last_Name\t",font=("Source Sans Pro",12,'bold'))
        self.l_name.grid(row=2,column=0,sticky=W)
        self.l_name_entry = Entry(self.window, font=("Source Sans Pro",12,'bold'))
        self.l_name_entry.grid(row=2,column=1,sticky=W)

        self.add_marks = ttk.Button(self.window, text="Marks List",command=self.class_call)
        self.add_marks.grid(row=4,column=0,sticky=W)

        self.window.mainloop()

    def delete_items(self):
        self.f_name_entry.delete(0,END)
        self.l_name_entry.delete(0,END)

    def quit_window(self) :
        self.window.destroy()

    def class_call(self) :
        myObj = SaveData(self.f_name_entry.get(), self.l_name_entry.get())
        myObj.classes_calling()

class StudentUIHelper :
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def classes_calling(self) :
        re = db_hander.carate_new_student('Thiloka','Surantha')
        if (re):
            msgbox "new student created!"
        else:
            msgbox "Student already exists!"
            
        myData = Database(self.fname, self.lname)
        myData.checking_database()

class Database :
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

    def checking_database(self) :
        db_connect = sqlite3.connect("/home/thiloka/Documents/Student_Records/databases/student.db")
        db_cursor = db_connect.cursor()

        db_cursor.execute("SELECT rowid,fname, lname FROM student WHERE fname = (?)",(self.first,))
        items = db_cursor.fetchall()

        if len(items) > 0 :
            error = messagebox.showerror("Error","You are already logged in.")

            if error == "ok" :
                StudentRecordWindow.delete_items()
        else :
            names = [
                (self.first, self.last)
            ]
            db_cursor.executemany("INSERT INTO student(fname, lname) VALUES (?,?)", names)
            db_connect.commit()
            information = messagebox.showinfo("Information", "You Name is saved")

            if information == "ok" :
                StudentRecordWindow.quit_window()


if __name__ == '__main__':
    StudentRecordWindow = StudentRecordGui(Tk())
    StudentRecordWindow.student_record_design()