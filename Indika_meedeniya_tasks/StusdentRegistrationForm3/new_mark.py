from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class NewMarksForm :
    def __init__(self, tk, db_handler) -> None:
        self.tk = tk
        self.db_handler = db_handler

    def marks_form(self) :
        self.std_id = []
        self.sub_id = []
        self.std_name = []
        self.sub_name = []

        get_students = self.db_handler.get_all_students()
        get_subjects = self.db_handler.get_all_subjects()

        for i in get_students :
            self.std_id.append(i.student_id)
            self.std_name.append(i.first_name + " " + i.last_name)

        for j in get_subjects :
            self.sub_name.append(j.subject_name)
            self.sub_id.append(j.subject_id)

        print(self.std_name, self.sub_name)

        stds_name = Label(self.tk, text="Enter the student name : ", font=("Source Sans Pro",12,'bold'))
        stds_name.grid(row=0, column=0)
        self.std_combo = ttk.Combobox(self.tk, values=self.std_name , font=("Source Sans Pro",12,'bold'))
        self.std_combo.grid(row=0, column=1)

        self.std_combo.bind("<<ComboboxSelected>>",self.on_student_select)

        subs_name = Label(self.tk, text="Enter the subject name : ", font=("Source Sans Pro",12,'bold'))
        subs_name.grid(row=1, column=0)
        self.sub_combo = ttk.Combobox(self.tk, values=self.sub_name, font=("Source Sans Pro",12,'bold'))
        self.sub_combo.grid(row=1, column=1)

        self.score_lbl = Label(self.tk, text="Enter the  score            : ", font=("Source Sans Pro",12,'bold'))
        self.score_lbl.grid(row=2, column=0)
        self.score_combo = Entry(self.tk, font=("Source Sans Pro",12,'bold'), width=21)
        self.score_combo.grid(row=2, column=1)


        submit_btn = Button(self.tk, text="submit", font=("Source Sans Pro",12,'bold'), command=self.submit, width=21, height=1)
        submit_btn.grid(row=0, column=2)
        close_btn = Button(self.tk, text='close', font=("Source Sans Pro",12,'bold'), command=self.close, width=21)
        close_btn.grid(row=1, column=2)

        self.tk.mainloop()

    def submit(self) :
        self.cur_std_id = self.std_id[self.std_combo.current()]
        cur_sub_id = self.sub_id[self.sub_combo.current()]
        score = self.score_combo.get()

        checkMarks = self.db_handler.check_marks(self.cur_std_id, cur_sub_id, score)

        if checkMarks == True :
            print("Name : {}, Subject : {}, Score : {} :::::::: Succesfully Saved it.".format(self.std_combo.get(), self.sub_combo.get(), self.score_combo.get()))

            self.db_handler.add_marks()

        else :
            error = messagebox.showerror("Error", "Your data is already in the database.")

            if error == "ok" :
                self.std_combo.delete(0, END)
                self.sub_combo.delete(0, END)
                self.score_combo.delete(0, END)
                
            for i in checkMarks :
                std = self.std_name[i.student_id-1]
                sub = self.sub_name[i.subject_id-1]
                scr = i.score

                print("Student Name : {}, Subject Name : {}, Score : {}".format(std, sub, scr))

    def on_student_select(self, event) :
        getStdMrkDtls = self.db_handler.get_student_marks_details(self.std_id[self.std_combo.current()])

        for j in getStdMrkDtls :
            std = self.std_name[j.student_id-1]
            sub = self.sub_name[j.subject_id-1]
            scr = j.score

            print("Student Name : {}, Subject Name : {}, Score : {}".format(std, sub, scr))

    def close(self) :
        pass

    def show_details(self) :
        pass