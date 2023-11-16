from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import find_labs as lab
from tkinter import messagebox


class LoginForm :
    def  __init__(self, log) :
        self.log = log
    
    def compare_screen(self) :
        self.log.title("Login")
        self.log.resizable(False,False)


    def login_form(self) :
        
        self.login_username_label = Label(self.log, image=self.username, text="username    :", font=("Source Sans Pro",12,'bold'),compound=LEFT)
        self.login_username_label.grid(row=1,sticky=W)
        self.login_password_lable = Label(self.log, image=self.password, text="password     :", font=("Source Sans Pro",12,'bold'),compound=LEFT)
        self.login_password_lable.grid(row=2,sticky=W)

        self.login_username_entry = Entry(self.log, font=("Source Sans Pro",12,'bold'))
        self.login_username_entry.grid(row=1,column=1,sticky=W)
        self.login_password_entry = Entry(self.log, font=("Source Sans Pro",12,'bold'),show="*")
        self.login_password_entry.grid(row=2,column=1,sticky=W)

        self.login_login_button = Button(self.log, image=self.login, text="login", font=("Source Sans Pro",12,'bold'), compound=LEFT,borderwidth=0 , command=self.login_function)
        self.login_login_button.grid(sticky=E, row=3,column=1)

        self.log.mainloop()

    def login_function(self) :
        name = self.login_username_entry.get()
        password = self.login_password_entry.get()


        if (name == "thiloka" and password == "thiloka123") :

            self.log.destroy()

            myLab = lab.FindLabForm(Tk())
            myLab.compare_screen()
            myLab.import_images()
            myLab.request_form()
            myLab.details()
            myLab.new_test_request()
            myLab.test_request()
            myLab.test_check()
        
        else :
            error = messagebox.showerror("Error","Invaliad Username or Password")

            if (error == "ok") :
                self.login_username_entry.delete(0,END)
                self.login_password_entry.delete(0,END)


if __name__ == '__main__':
    myLog = LoginForm(Tk())
    myLog.compare_screen()

    myLog.login_form()
    myLog.login_function()