from tabnanny import check
from tkinter import *
from tkinter import messagebox
import main_form

class NewSubjects :
    def __init__(self, tk, db_handler) -> None:
        self.tk = tk
        self.db_handler = db_handler

    def new_subjects_form(self) : 
        name_lbl = Label(self.tk, text="Enter your subject : ", font=("SOurce Sans Pro",12,'bold'))
        name_lbl.grid(row=0,column=0)
        self.name = Entry(self.tk, font=("Source Sans Pro",12,'bold'))
        self.name.grid(row=0, column=1)

        btn = Button(self.tk, text="CLICK OK", font=("Source Sans Pro",12,'bold'), command=self.add_subjects)
        btn.grid(row=0, column=2)
        cancle = Button(self.tk, text="CLOSE", font=("Source Sans Pro",12,'bold'), command=self.close)
        cancle.grid(row=0, column=3)

        self.tk.mainloop()

    def add_subjects(self) :
        get_subject_name = self.name.get()

        checkSub = self.db_handler.check_subjects(get_subject_name)

        if checkSub == True :
            self.db_handler.add_new_subjects(get_subject_name)

            btn = messagebox.showinfo("Information", "Successfully saved on a database.")

            if btn == "ok" : 
                self.name.delete(0, END)

        else :
            error = messagebox.showwarning("Warning", "This subject is already in the database.")

            if error == "ok" :
                self.name.delete(0, END) 

    def close(self) :
        self.tk.destroy()
        
        myObj = main_form.MainForm(Tk())
        myObj.form()