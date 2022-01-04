from tkinter import *
import database
import student
import items
import scores

class Subject :
    def __init__(self, subject, firstname, lastname) -> None:
        self.subject = subject
        self.firstname = firstname
        self.lastname = lastname

    def add_new_subjects(self) :

        word = "Subject"

        self.maths_lbl = Label(self.subject, text=f"{word} Maths\t", font=("Source Sans Pro",12,'bold'))
        self.maths_lbl.grid(row=1)
        self.maths = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.maths.grid(row=1, column=1)

        self.science_lbl = Label(self.subject, text=f"{word} Science\t", font=("Source Sans Pro",12,'bold'))
        self.science_lbl.grid(row=2)
        self.science = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.science.grid(row=2, column=1)

        self.sinhala_lbl = Label(self.subject, text=f"{word} Sinhala\t", font=("Source Sans Pro",12,'bold'))
        self.sinhala_lbl.grid(row=3)
        self.sinhala = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.sinhala.grid(row=3, column=1)

        self.english_lbl = Label(self.subject, text=f"{word} English\t", font=("Source Sans Pro",12,'bold'))
        self.english_lbl.grid(row=4)
        self.english = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.english.grid(row=4, column=1)

        self.geography_lbl = Label(self.subject, text=f"{word} Geography\t", font=("Source Sans Pro",12,'bold'))
        self.geography_lbl.grid(row=5)
        self.geography = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.geography.grid(row=5, column=1)

        self.tamil_lbl = Label(self.subject, text=f"{word} Tamil\t", font=("Source Sans Pro",12,'bold'))
        self.tamil_lbl.grid(row=6)
        self.tamil = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.tamil.grid(row=6, column=1)

        self.ict_lbl = Label(self.subject, text=f"{word} ICT\t", font=("Source Sans Pro",12,'bold'))
        self.ict_lbl.grid(row=7)
        self.ict = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.ict.grid(row=7, column=1)

        self.pts_lbl = Label(self.subject, text=f"{word} P.T.S\t", font=("Source Sans Pro",12,'bold'))
        self.pts_lbl.grid(row=8)
        self.pts = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.pts.grid(row=8, column=1)

        self.health_lbl = Label(self.subject, text=f"{word} Health\t", font=("Source Sans Pro",12,'bold'))
        self.health_lbl.grid(row=9)
        self.health = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.health.grid(row=9, column=1)

        self.history_lbl = Label(self.subject, text=f"{word} History\t", font=("Source Sans Pro",12,'bold'))
        self.history_lbl.grid(row=10)
        self.history = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.history.grid(row=10, column=1)

        self.civic_lbl = Label(self.subject, text=f"{word} Civic\t", font=("Source Sans Pro",12,'bold'))
        self.civic_lbl.grid(row=11)
        self.civic = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.civic.grid(row=11, column=1)

        self.buddhishm_lbl = Label(self.subject, text=f"{word} Buddhishm\t", font=("Source Sans Pro",12,'bold'))
        self.buddhishm_lbl.grid(row=12)
        self.buddhishm = Entry(self.subject, font=("Source Sans Pro",12,'bold'))
        self.buddhishm.grid(row=12, column=1)

        self.close = Button(self.subject, text="Close", font=("Source Sans Pro",12,'bold'), command=self.close)
        self.close.grid(row=13, sticky=W)
        self.genarate = Button(self.subject, text="Genarate", font=("Source Sans Pro",12,'bold'), command=self.genarate_subject)
        self.genarate.grid(row=13, column=1, sticky=W)

        self.subject.mainloop()

    def genarate_subject(self) :
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
        subject_data  = database.DatabaseHandlerForSubjects(subject_values, self.firstname, self.lastname)
        subject_data.database_for_subject()
    def close(self) :
        self.subject.destroy()

        StudentRecordWindow = items.ChooseItems(Tk())
        StudentRecordWindow.create_window()
