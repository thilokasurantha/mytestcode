from tkinter import *
from tkinter import messagebox
import main_form

class NewStudentsForm :
    def __init__(self, tk, db_handler) -> None:
        self.tk = tk
        self.db_handler = db_handler

    def students_form(self) :
        fname_lbl = Label(self.tk, text="First Name", font=("Soerce Sans Pro",12,'bold'))
        fname_lbl.grid(row=0, column=0)
        self.fname = Entry(self.tk, font=("Source Sans Pro",12,'bold'))
        self.fname.grid(row=0, column=1)

        lname_lbl = Label(self.tk, text="Last Name", font=("Source San Pro",12,'bold'))
        lname_lbl.grid(row=1,column=0)
        self.lname = Entry(self.tk, font=("Source Sans Pro",12,'bold'))
        self.lname.grid(row=1,column=1)

        submit_btn = Button(self.tk, text="SUBMIT", font=("Source Sans Pro",12,'bold'), command=self.submit)
        submit_btn.grid(row=2, column=0)
        cancle = Button(self.tk, text="CLOSE", font=("Source Sans Pro",12,'bold'), command=self.close)
        cancle.grid(row=2, column=1)
        
        self.tk.mainloop()

    def submit(self) :
        get_fname = self.fname.get()
        get_lname = self.lname.get()

        get_return_value = self.db_handler.get_student(get_fname, get_lname)

        if get_return_value == True :
            self.db_handler.add_student(get_fname, get_lname)

        else :
            messagebox.showerror("Error", "You are already logged in.")
            for j in get_return_value :
                print(j.show_student_details())

    def close(self) :
        self.tk.destroy()

        myMainForm = main_form.MainForm(Tk())
        myMainForm.main_form()
