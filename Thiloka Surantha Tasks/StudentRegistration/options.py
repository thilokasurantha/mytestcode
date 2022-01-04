from tkinter import *
from tkinter import messagebox
import registration as regi

class StudentOptionGUI :
    def __init__(self, option) -> None:
        self.reg = option

    def registration_form(self) :
        registration = Button(self.reg, text="Student Registration", font=("Source Sans Pro",12,"bold"), width=50,height=5, command=self.student_registration)
        registration.pack()

        sub_marks = Button(self.reg, text="View Subjects", font=("Source Sans Pro",12,"bold"), width=50,height=5, command=self.marks)
        sub_marks.pack()

        scores = Button(self.reg, text="Check Score", font=("Source Sans Pro",12,"bold"), width=50,height=5, command=self.view_score)
        scores.pack()
        
        self.reg.mainloop()

    def student_registration(self) :
        self.reg.destroy()

        register = regi.RegistrationForm(Tk())
        register.registration_form()

    def marks(self) :
        pass

    def view_score(self) :
        pass


if __name__ == "__main__":
    StudentReg = StudentOptionGUI(Tk())
    StudentReg.registration_form()

