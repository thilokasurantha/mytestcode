from tkinter import *
import student
import subjects
import scores

class ChooseItems(object) :
    def __init__(self, window):
        self.window = window

    def create_window(self):
        self.window.title("Student Record Application")
        
        self.new_student = Button(self.window, text="Add New Student", font=("Source Sans Pro",12,"bold"), width=50,height=5, command = self.student)
        self.new_student.pack()
        self.add_score = Button(self.window, text="Add New Scores", font=("Source Sans Pro",12,'bold'), width=50, height=5, command = self.score)
        self.add_score.pack()

        self.window.mainloop()

    def student(self) :
        self.window.destroy()

        NewStd = student.NewStudent(Tk())
        NewStd.add_new_students()

    def score(self):
        self.window.destroy()

        Score = scores.AddScore(Tk())
        Score.check_scores()

if __name__ == '__main__':
    StudentRecordWindow = ChooseItems(Tk())
    StudentRecordWindow.create_window()