from tkinter import *
import new_student as n_std
import names
import add_score as score

class MainStudentRecordGUI(object) :
    def __init__(self, window):
        self.window = window

    def create_window(self):
        self.window.title("Student Record Application")
        
        self.new_student = Button(self.window, text="Add New Student", font=("Source Sans Pro",12,"bold"), width=50,height=5, command = self.student)
        self.new_student.pack()
        self.add_score = Button(self.window, text="Add New Scores", font=("Source Sans Pro",12,'bold'), width=50, height=5, command = self.score)
        self.add_score.pack()
        self.add_new_subject = Button(self.window, text="Add New Subject", font=("Source Sans Pro",12,'bold'), width=50, height=5, command = self.subject)
        self.add_new_subject.pack()

        self.window.mainloop()

    def student(self) :
        self.window.destroy()
        NewStd = n_std.NewStudent(Tk())
        NewStd.add_new_student_window()

    def score(self):
        self.window.destroy()
        Score = score.AddScore(Tk())
        Score.add_score_window()

    def subject(self) :
        self.window.destroy()

        myOnj = names.Names(Tk())
        myOnj.name_window()

if __name__ == '__main__':
    StudentRecordWindow = MainStudentRecordGUI(Tk())
    StudentRecordWindow.create_window()