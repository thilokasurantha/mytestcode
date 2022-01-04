from tkinter import *
import add_new_subject as sub
import database as subject
from tkinter import messagebox
import main

class Names :
    def __init__(self, root) -> None:
        self.root = root

    def name_window(self) :
        self.root.title("Named Window")

        name_lbl = Label(self.root, text="name", font=("Source Sans Pro",12,'bold'))
        name_lbl.grid(row=1,column=0,sticky=W)
        self.name_entry = Entry(self.root, font=("Source Sans Pro",12,'bold'))
        self.name_entry.grid(row=1, column=1,sticky=W)
        name = Button(self.root, text="save", command=self.next_page)
        name.grid(row=1, column=2)
        close = Button(self.root, text="close",command=self.close)
        close.grid(row=1, column=3)

        self.root.mainloop()

    def next_page(self) :
        mySubjectDb = subject.DatabaseHandlerForSavedNames(self.name_entry.get())
        asnwer = mySubjectDb.database_handler_for_saved_names()

        if asnwer :
            messagebox.showinfo("Information","You are successfully saved a database.")

            self.name_value = self.name_entry.get()

            self.root.destroy()

            Sub = sub.AddNewSubjects(Tk(), self.name_value)
            Sub.add_new_subject_window()

        else :
            messagebox.showwarning("Warnning", "You are not registered a database.")

            self.root.destroy()

            StudentRecordWindow = main.MainStudentRecordGUI(Tk())
            StudentRecordWindow.create_window()

    def close(self) :
        self.root.destroy()
        
        StudentRecordWindow = main.MainStudentRecordGUI(Tk())
        StudentRecordWindow.create_window()