from tkinter import *
from tkinter import messagebox
import random
import db_handler as data
import sqlite3
import chat_form
import os

class Option :
    def __init__(self, root) -> None:
        self.root = root
        self.db = data.DatabaseHandlerLogin()
        self.connect = sqlite3.connect(os.getcwd()+"\database.db")
        self.cursor = self.connect.cursor()

    def random_numbers(self) :
        random_number = random.randrange(1000, 9999)
        return random_number

    def form(self) :
        self.name_label = Label(self.root, text="Full Name : ", font=("Source Sans Pro",12,"bold"))
        self.name_label.grid(row=1, column=0)
        self.name_entry = Entry(self.root, font=("Source Sans Pro",12,"bold"))
        self.name_entry.grid(row=1, column=1)

        self.password_label = Label(self.root, text="Password : ", font=("Source Sans Pro",12,"bold"))
        self.password_label.grid(row=2, column=0)
        self.password_entry = Entry(self.root, font=("Source Sans Pro",12,"bold"), show="*")
        self.password_entry.grid(row=2, column=1)
        

        self.key_label = Label(self.root, text="Unique Key : ", font=("Source Sans Pro",12,"bold"))
        self.key_label.grid(row=3, column=0)
        self.key_entry = Entry(self.root, font=("Source Sans Pro",12,"bold"))
        self.key_entry.insert(0, self.random_numbers())
        self.key_entry.grid(row=3, column=1)

        self.generate = Button(self.root, text="Generate", font=("Source Sans Pro",12,"bold"), command=self.loginsystem)
        self.generate.grid(row=4,column=0)

        self.root.mainloop()

    def loginsystem(self) :
        if(len(self.name_entry.get())>0 and len(self.password_entry.get())>0) :
            search = self.db.register_form(self.name_entry.get())
            if search :
                self.name_entry.delete(0,END)
                self.key_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.name_entry.insert(0, search[0][1])
                self.key_entry.insert(0, search[0][2])
                self.password_entry.insert(0, search[0][3])
                
                name = self.name_entry.get()
                key = self.key_entry.get()

                messagebox.showwarning("Error", "You are already logged into this software")
                self.root.destroy()
                myObj = chat_form.ChatForm(Tk())
                myObj.form(name, key)

            else :
                ins_db_register = self.cursor.execute("INSERT INTO registration(name, key, password) VALUES (?,?,?)", (self.name_entry.get(), self.key_entry.get(), self.password_entry.get()))
                self.connect.commit()
                messagebox.showinfo("Information", "You are a now memeber to our software.")
                self.root.destroy()

                name_new = self.name_entry.get()
                key_new = self.key_entry.get()

                myObj = chat_form.ChatForm(Tk())
                myObj.form(name_new, key_new)


        else :
            messagebox.showwarning("Error", "Please Fill The Blanks Correctry")
            self.name_entry.delete(0, END)
            self.password_entry.delete(0, END)
if __name__ == "__main__" :
    myObj = Option(Tk())
    myObj.form()