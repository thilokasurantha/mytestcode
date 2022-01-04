from tkinter import *
from tkinter import messagebox

class SubjectsGUI :
    def __init__(self,sub) -> None:
        self.sub = sub

    def subjects_window(self) :
        maths_label = Label(self.sub, text="Maths\t", font=("Source Sans Pro",12,'bold'))
        maths_label.grid(row=0, column=0)
        maths = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        maths.grid(row=0, column=1)

        science_label = Label(self.sub, text="Science\t", font=("Source Sans Pro",12,'bold'))
        science_label.grid(row=1,column=0)
        science = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        science.grid(row=1, column=1)

        physics_label = Label(self.sub, text="Physics\t", font=("Source Sans Pro",12,'bold'))
        physics_label.grid(row=2,column=0)
        physics = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        physics.grid(row=2, column=1)

        ict_label = Label(self.sub, text="ICT\t", font=("Source Sans Pro",12,'bold'))
        ict_label.grid(row=3,column=0)
        ict = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        ict.grid(row=3, column=1)

        sinhala_label = Label(self.sub, text="Sinhala\t", font=("Source Sans Pro",12,'bold'))
        sinhala_label.grid(row=4,column=0)
        sinhala = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        sinhala.grid(row=4, column=1)

        english_label = Label(self.sub, text="English\t", font=("Source Sans Pro",12,'bold'))
        english_label.grid(row=5,column=0)
        english = Entry(self.sub, font=("Source Sans Pro",12,'bold'))
        english.grid(row=5, column=1)

        self.sub.mainloop()


if __name__ == "__main__" :
    x = SubjectsGUI(Tk())
    x.subjects_window()