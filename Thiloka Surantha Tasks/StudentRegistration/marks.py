from tkinter import *
from tkinter import messagebox
import database

class InsertMarks :
    def __init__(self, mrk, std_name) -> None:
        self.mrk = mrk
        self.std_name = std_name

    def form(self) :
        self.lbl_1 = Label(self.mrk, text="Maths\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_1.grid(row=0, column=0, sticky=W)
        self.maths = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.maths.grid(row=0, column=1)

        self.lbl_2 = Label(self.mrk, text="I.C.T\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_2.grid(row=1, column=0, sticky=W)
        self.ict = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.ict.grid(row=1, column=1)

        self.lbl_3 = Label(self.mrk, text="Sinhala\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_3.grid(row=2, column=0, sticky=W)
        self.sinhala = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.sinhala.grid(row=2, column=1)

        self.lbl_4 = Label(self.mrk, text="Geography\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_4.grid(row=3, column=0, sticky=W)
        self.geography = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.geography.grid(row=3, column=1)

        self.lbl_5 = Label(self.mrk, text="History\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_5.grid(row=4, column=0, sticky=W)
        self.history = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.history.grid(row=4, column=1)

        self.lbl_6 = Label(self.mrk, text="Tamil\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_6.grid(row=5, column=0, sticky=W)
        self.tamil = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.tamil.grid(row=5, column=1)

        self.lbl_7 = Label(self.mrk, text="Science\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_7.grid(row=6, column=0, sticky=W)
        self.science = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.science.grid(row=6, column=1)

        self.lbl_8 = Label(self.mrk, text="Buddhishm\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_8.grid(row=7, column=0, sticky=W)
        self.budd = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.budd.grid(row=7, column=1)

        self.lbl_9 = Label(self.mrk, text="ART\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_9.grid(row=8, column=0, sticky=W)
        self.art = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.art.grid(row=8, column=1)

        self.lbl_10 = Label(self.mrk, text="P.T.S\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_10.grid(row=9, column=0, sticky=W)
        self.pts = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.pts.grid(row=9, column=1)

        self.lbl_11 = Label(self.mrk, text="P.T\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_11.grid(row=10, column=0, sticky=W)
        self.pt = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.pt.grid(row=10, column=1)

        self.lbl_12 = Label(self.mrk, text="English\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_12.grid(row=11, column=0, sticky=W)
        self.eng = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.eng.grid(row=11, column=1)

        self.lbl_13 = Label(self.mrk, text="Civics\t", font=("Source Sans Pro",12,'bold'))
        self.lbl_13.grid(row=12, column=0, sticky=W)
        self.civ = Entry(self.mrk, font=("Source Sans Pro",12,'bold'))
        self.civ.grid(row=12, column=1)

        self.save = Button(self.mrk, text="SAVE", font=("Source Sans Pro",12,'bold'), command=self.save_mark)
        self.save.grid(row=13,column=0, sticky=W)
        self.close = Button(self.mrk, text="CLOSE", font=("Source Sans Pro",12,'bold'), command=self.end)
        self.close.grid(row=13,column=0, sticky=E)

        self.mrk.mainloop()

    def save_mark(self) :
        dict_marks = {
            "maths" : self.maths.get(),
            "i.c.t" : self.ict.get(),
            "sinhala" : self.sinhala.get(),
            "geography" : self.geography.get(),
            "history" : self.history.get(),
            "tamil" : self.tamil.get(),
            "science" : self.science.get(),
            "buddhishm" : self.budd.get(),
            "art" : self.art.get(),
            "p.t.s" :self.pts.get(),
            "p.t" : self.pt.get(),
            "english" : self.eng.get(),
            "civcs" : self.civ.get()
        }

        add = database.DatabaseHandlerForMarks(self.std_name, dict_marks)
        add.db_handler_marks()

    def end(self) :
        exit()
