# Import Libraries
from tkinter import *
from tkinter import messagebox
# Import Files
import registration as regi
import score as scr
import edit as e
import edit
# Code 
class StudentOptionGUI :
    def __init__(self, option) -> None:
        self.reg = option

    def registration_form(self) :
        registration = Button(self.reg, text="Student Name Registration", font=("Source Sans Pro",12,"bold"), width=50,height=5, command=self.student_registration)
        registration.pack()

        sub_marks = Button(self.reg, text="Create Subject and Marks", font=("Source Sans Pro",12,"bold"), width=50,height=5, command=self.subjects)
        sub_marks.pack()

        scores = Button(self.reg, text="Check Score", font=("Source Sans Pro",12,"bold"), width=50,height=5, command=self.check_score)
        scores.pack()
        
        self.reg.mainloop()

    def student_registration(self) :
        self.reg.destroy()

        register = regi.RegistrationForm(Tk())
        register.registration_form()

    def subjects(self) :
        self.reg.destroy()
        
        subject = edit.EditAndAddSubjects(Tk())
        subject.window()

    def check_score(self) :
        pass


if __name__ == "__main__":
    StudentReg = StudentOptionGUI(Tk())
    StudentReg.registration_form()

