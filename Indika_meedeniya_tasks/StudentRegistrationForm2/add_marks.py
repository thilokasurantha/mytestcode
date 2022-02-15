from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import main_form

class NewMarksForm :
    def __init__(self, tk, db_handler) -> None:
        self.tk = tk
        self.db_handler = db_handler

    def show_details(self) :
        pass

    def new_marks_form(self) :

        stds = self.db_handler.get_all_stduetnts()


        get_names, get_subjects = self.db_handler.give_details_for_add_marks()

        stds = []
        subs = []

        for j in get_names :
            stds.append(j)
        for i in get_subjects :
            subs.append(i[0])

        std_name = Label(self.tk, text="Enter the student name : ", font=("Source Sans Pro",12,'bold'))
        std_name.grid(row=0, column=0)
        self.std_combo = ttk.Combobox(self.tk, values=stds, font=("Source Sans Pro",12,'bold'))
        self.std_combo.grid(row=0, column=1)

        self.std_combo.bind("<<ComboboxSelected>>",self.on_student_select)

        sub_name = Label(self.tk, text="Enter the subject name : ", font=("Source Sans Pro",12,'bold'))
        sub_name.grid(row=1, column=0)
        self.sub_combo = ttk.Combobox(self.tk, values=subs, font=("Source Sans Pro",12,'bold'))
        self.sub_combo.grid(row=1, column=1)

        self.score_lbl = Label(self.tk, text="Enter the  score            : ", font=("Source Sans Pro",12,'bold'))
        self.score_lbl.grid(row=2, column=0)
        self.score_combo = Entry(self.tk, font=("Source Sans Pro",12,'bold'), width=21)
        self.score_combo.grid(row=2, column=1)


        submit_btn = Button(self.tk, text="submit", font=("Source Sans Pro",12,'bold'), command=self.submit, width=21)
        submit_btn.grid(row=0, column=2)
        close_btn = Button(self.tk, text='close', font=("Source Sans Pro",12,'bold'), command=self.close, width=21)
        close_btn.grid(row=1, column=2)
        details = Button(self.tk, text="details", font=("Source Sans Pro",12,'bold'), command=self.show_details, width=21)
        details.grid(row=2, column=2)

        self.tk.mainloop()


    def on_student_select(self, event):
        print ("IM HERER" + self.std_combo.get())

    def submit(self) :
        get_name = self.std_combo.get()
        get_subject = self.sub_combo.get()
        get_score = self.score_combo.get()

        checkScore = self.db_handler.check_details(get_name, get_subject, get_score)

        if checkScore == True :
            self.db_handler.add_scores(get_score)

            answer = messagebox.showinfo("Information", "Successfully save on your marks in database.")

            if answer == "ok" :
                self.clear_entries()

        else :
            error = messagebox.showwarning("Warning", "Your marks are already added in a database.")

            if error == "ok" :
                self.clear_entries()

    def clear_entries(self) :
        self.std_combo.delete(0, END)
        self.sub_combo.delete(0, END)
        self.score_combo.delete(0, END)

    def close(self) :
        self.tk.destroy()
        
        myObj = main_form.MainForm(Tk())
        myObj.form()