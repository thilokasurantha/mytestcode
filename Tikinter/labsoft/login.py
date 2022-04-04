from tkinter import *

from tkinter import messagebox
import os
root = Tk()
def login_function():
    get_login_usernames = login_username_entry.get()
    get_login_passwords = login_password_entry.get()
    print(get_login_usernames)
    get_usernames = open("usernames.txt","r")
    get_passwords = open("passwords.txt","r")

    with get_usernames as f :
        username = get_usernames.readlines()
        for z in username :
            print(z)

    with get_passwords as s :
        password = s.readlines()
        for r in password :
            print(r)

    if (get_login_usernames == z and get_login_passwords == r):
        asking = messagebox.showinfo("Good","Please click Ok button")
        import coose_lab
    elif (get_login_usernames != z and get_login_passwords != r):
            error_label = Label(root,text="Invaliad Username or Password . Please Try again .",font=("Arial Black",10),fg="red")
            error_label.grid(row=3,column=3)
    else :
        while(True):
            ask = messagebox.askquestion("Error Founding", "Now you click yes button")
            if (ask == "yes") :
                import coose_lab


# Username photo

# Enter the username
login_username = Label(root, text="USER NAME :",font=("Arial Black",16),borderwidth=0)
login_username.grid(row=1,column=2,sticky=W)
login_username_entry = Entry(root,width=25,font=("Arial Black",16),borderwidth=0)
login_username_entry.grid(row=1,column=3)
# Password photo

# Enter the password
login_password = Label(root, text="PASSWORD :",font=("Arial Black",16),borderwidth=0)
login_password.grid(row=2,column=2,sticky=E)
login_password_entry = Entry(root,width=25,font=("Arial Black",16),borderwidth=0)
login_password_entry.config(show="X")
login_password_entry.grid(row=2,column=3)
# Submit button
login_registry = Button(root,text="LOGIN",font=("Arial Black",16),borderwidth=0,command=login_function)
login_registry.grid(row=2,column=4,sticky=W)

root.mainloop()
