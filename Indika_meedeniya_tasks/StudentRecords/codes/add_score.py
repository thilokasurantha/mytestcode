from tkinter import *
import database as db
from tkinter import messagebox
import main

class AddScore :
    def __init__(self, score):
        self.score = score

    def add_score_window(self):
        self.score.title("Student Score Application")

        name_lbl = Label(self.score, text="name", font=("Source Sans Pro",12,'bold'))
        name_lbl.grid(row=1,column=0,sticky=W)
        self.score_name = Entry(self.score, font=("Source Sans Pro",12,'bold'))
        self.score_name.grid(row=1, column=1,sticky=W)
        check = Button(self.score, text="check", command=self.done_student)
        check.grid(row=1, column=2)
        close = Button(self.score, text="close", command=self.close)
        close.grid(row=1,column=3)

        self.score.mainloop()
    
    def done_student(self) :
        get_name = self.score_name.get()

        myScoreNames = db.DatabaseHandlerScoreName(get_name)
        score = myScoreNames.database_handler_for_score()

        if score :
            messagebox.showinfo("Information", "Succeed!")

            self.score.destroy()
            print("Destroyed")

            SWindow = ScoreWindow(Tk(),get_name)
            SWindow.score_window()
        else :
            messagebox.showerror("Error", "You are not succedd.")

            self.score.destroy()

            StudentRecordWindow = main.MainStudentRecordGUI(Tk())
            StudentRecordWindow.create_window()

    def close(self) :
        self.score.destroy()

        StudentRecordWindow = main.MainStudentRecordGUI(Tk())
        StudentRecordWindow.create_window()

class ScoreWindow :
    def __init__(self, win, name) -> None:
        self.win = win
        self.name = name

    def score_window(self) :
        self.sum = Button(self.win, text="sum" , font=("Source Sans Pro",12,"bold"), width=50,height=5, command = self.get_sum)
        self.sum.pack()
        self.avarage = Button(self.win, text="avarage", font=("Source Sans Pro",12,'bold'), width=50, height=5, command = self.get_avarage)
        self.avarage.pack()

        self.win.mainloop()

    def get_sum(self) :
        get_sum = db.DatabaseHandlerScore(self.name)
        value,length = get_sum.get_values()
        
        self.win.destroy()

        SumWindow = ScoreSum(value,length)
        SumWindow.sum_window()

    def get_avarage(self) :
        get_sum = db.DatabaseHandlerScore(self.name)
        value,length = get_sum.get_values()

        self.win.destroy()

        SumWindow = ScoreSum(value,length)
        SumWindow.avarage_window()       


class ScoreSum :
    def __init__(self, number,get_len) -> None:
        self.num = number
        self.get_len = get_len

    def sum_window(self) :
        sum_press = messagebox.showinfo("Information", f"Your marks all sum value is {self.num}")

        if sum_press :
            StudentRecordWindow = main.MainStudentRecordGUI(Tk())
            StudentRecordWindow.create_window()

    def avarage_window(self) :
        avarage_press = messagebox.showinfo("Information", f"Your subjects avarage is {self.num//self.get_len}")

        if avarage_press :
            StudentRecordWindow = main.MainStudentRecordGUI(Tk())
            StudentRecordWindow.create_window()