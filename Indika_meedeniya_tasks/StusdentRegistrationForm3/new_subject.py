from tkinter import *
from tkinter import messagebox

class NewSubjectsForm :
    def __init__(self, tk, db_handler) -> None:
        self.tk = tk
        self.db_handler = db_handler

    def subject_form(self) :
        name_lbl = Label(self.tk, text="Enter your subject : ", font=("SOurce Sans Pro",12,'bold'))
        name_lbl.grid(row=0,column=0)
        self.name = Entry(self.tk, font=("Source Sans Pro",12,'bold'))
        self.name.grid(row=0, column=1)

        btn = Button(self.tk, text="CLICK OK", font=("Source Sans Pro",12,'bold'), command=self.add_subject)
        btn.grid(row=0, column=2)
        cancle = Button(self.tk, text="CLOSE", font=("Source Sans Pro",12,'bold'), command=self.close)
        cancle.grid(row=0, column=3)

        self.tk.mainloop()

    def add_subject(self) :
        sub_name = self.name.get()

        checkSub = self.db_handler.check_subjects(sub_name)

        if checkSub == True :
            self.db_handler.add_subject()

            save_messagebox = messagebox.showinfo("Information", "Successfully saved on a database")

            if save_messagebox == "ok" :
                self.name.delete(0, END)

        else :
            error_message = messagebox.showerror("Error", "Your Subject is already in the database")
            showAlreadyLoggedStudentDetail = self.db_handler.check_subjects(sub_name)

            for i in showAlreadyLoggedStudentDetail :
                print(i.show_subject_details())

            if error_message == "ok" :
                self.name.delete(0, END)

    def close(self) :
        pass

    