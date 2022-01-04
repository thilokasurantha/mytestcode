from tkinter import *
from tkinter import messagebox
import database

class CheckAndAddScore :
    def __init__(self, score) -> None:
        self.score = score

    def form(self) :
        add_score = database.DatabaseHandlerForMarks("thiloka")
        items = add_score.db_handler_marks()

        for i in items :
            for j in i :
                self.marks = Entry(self.score)
                self.marks.pack(anchor=N)
                self.marks.insert(0, j)
                
                send = Button(self.score, text="send",width=18, command=self.add_marks)
                send.pack()

        self.score.mainloop()

    def add_marks(self) :
        print(self.marks.get())

if __name__ == "__main__" :
    x = CheckAndAddScore(Tk())
    x.form()