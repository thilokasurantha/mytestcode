from tkinter import *
import main as main
import database as db
from tkinter import messagebox

class AddNewSubjects :
    def __init__(self, sub, chk_name):
        self.sub = sub
        self.chk_name = chk_name

    def add_new_subject_window(self):
        self.sub.title("Fill The Subjects")
        
        word = "Subject"

        maths_lbl = Label(self.sub, text=f"{word} Maths\t", font=("Source Sans Pro",12,'bold'))
        maths_lbl.grid(row=1)
        self.maths = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.maths.grid(row=1, column=1)

        science_lbl = Label(self.sub, text=f"{word} Science\t", font=("Source Sans Pro",12,'bold'))
        science_lbl.grid(row=2)
        self.science = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.science.grid(row=2, column=1)

        sinhala_lbl = Label(self.sub, text=f"{word} Sinhala\t", font=("Source Sans Pro",12,'bold'))
        sinhala_lbl.grid(row=3)
        self.sinhala = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.sinhala.grid(row=3, column=1)

        english_lbl = Label(self.sub, text=f"{word} English\t", font=("Source Sans Pro",12,'bold'))
        english_lbl.grid(row=4)
        self.english = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.english.grid(row=4, column=1)

        geography_lbl = Label(self.sub, text=f"{word} Geography\t", font=("Source Sans Pro",12,'bold'))
        geography_lbl.grid(row=5)
        self.geography = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.geography.grid(row=5, column=1)

        tamil_lbl = Label(self.sub, text=f"{word} Tamil\t", font=("Source Sans Pro",12,'bold'))
        tamil_lbl.grid(row=6)
        self.tamil = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.tamil.grid(row=6, column=1)

        ict_lbl = Label(self.sub, text=f"{word} ICT\t", font=("Source Sans Pro",12,'bold'))
        ict_lbl.grid(row=7)
        self.ict = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.ict.grid(row=7, column=1)

        pts_lbl = Label(self.sub, text=f"{word} P.T.S\t", font=("Source Sans Pro",12,'bold'))
        pts_lbl.grid(row=8)
        self.pts = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.pts.grid(row=8, column=1)

        health_lbl = Label(self.sub, text=f"{word} Health\t", font=("Source Sans Pro",12,'bold'))
        health_lbl.grid(row=9)
        self.health = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.health.grid(row=9, column=1)

        history_lbl = Label(self.sub, text=f"{word} History\t", font=("Source Sans Pro",12,'bold'))
        history_lbl.grid(row=10)
        self.history = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.history.grid(row=10, column=1)

        civic_lbl = Label(self.sub, text=f"{word} Civic\t", font=("Source Sans Pro",12,'bold'))
        civic_lbl.grid(row=11)
        self.civic = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.civic.grid(row=11, column=1)

        buddhishm_lbl = Label(self.sub, text=f"{word} Buddhishm\t", font=("Source Sans Pro",12,'bold'))
        buddhishm_lbl.grid(row=12)
        self.buddhishm = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        self.buddhishm.grid(row=12, column=1)

        close = Button(self.sub, text="Close", font=("Source Sans Pro",12,'bold'), command=self.subject_close)
        close.grid(row=13, sticky=W)
        genarate = Button(self.sub, text="Genarate", font=("Source Sans Pro",12,'bold'), command=self.genarate_subjects)
        genarate.grid(row=13, column=1, sticky=W)

    def genarate_subjects(self) :
        subject_values = {
            "mat" : self.maths.get(),
            "sci" : self.science.get(),
            "sin" : self.sinhala.get(),
            "eng" :self.english.get(),
            "geo" : self.geography.get(),
            "tam" : self.tamil.get(),
            "ic" : self.ict.get(),
            "pt" : self.pts.get(),
            "hea" : self.health.get(),
            "his" : self.history.get(),
            "civ" : self.civic.get(),
            "budd" : self.buddhishm.get(),
        }

        Subjects = db.DatabaseHandlerForSubjects(subject_values, self.chk_name)
        Subjects.database_handler_for_subjects()
        information = messagebox.showinfo("Information", "Successfully Genarated.")

        if information :
            self.sub.destroy()
            StudentRecordWindow = main.MainStudentRecordGUI(Tk())
            StudentRecordWindow.create_window()
            
    def subject_close(self) :
        self.sub.destroy()
        StudentRecordWindow = main.MainStudentRecordGUI(Tk())
        StudentRecordWindow.create_window()
