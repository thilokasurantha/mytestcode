from tkinter import *
from tkinter import messagebox
import time
from PIL import ImageTk ,Image
import login as th

def find_user():
    with open('usernames.txt', 'r') as f:
        my_usernames = f.readlines()
        for y in my_usernames:
            print(y)

    with open('passwords.txt', 'r') as a:
        my_password = a.readlines()
        for x in my_password :
            print(x)

    ask = messagebox.askquestion("Go To Login","Do you want to login ?")
    if(ask == "yes"):
        import login
    else:
        while(True):
             must_be = messagebox.askquestion("Must","Please click yes ?")
             if (must_be == "yes"):
                 import login


def registoring():
    # Varialbles in function
    get_username = username_entry.get()
    get_password = password_entry.get()


    username_add = open("usernames.txt","w")
    username_add.write(get_username)
    username_add.close()

    password_importing = open("passwords.txt","w")
    password_importing.write("{}".format(get_password))
    password_importing.close()


def find_user():

    


def build_registration_form(resources_path,frame):
    # Username photo
    photo_username = ImageTk.PhotoImage(Image.open(resources_path+"\\icons8-user-90.png"))
    username_images = Label(frame,image=photo_username)
    username_images.grid(row=1,sticky=W)
    # Enter the username
    username = Label(frame, text="USER NAME :",font=("Arial Black",16))
    username.grid(row=1,column=2,sticky=W)
    username_entry = Entry(root,width=25,font=("Arial Black",16),borderwidth=0)
    username_entry.grid(row=1,column=3)
    # Password photo
    photo_password = ImageTk.PhotoImage(Image.open(resources_path+"\icons8-password-96.png"))
    password_images = Label(frame,image=photo_password)
    password_images.grid(row=2,sticky=W)
    # Enter the password
    password = Label(frame, text="PASSWORD :",font=("Arial Black",16))
    password.grid(row=2,column=2,sticky=E)
    password_entry = Entry(frame,width=25,font=("Arial Black",16),borderwidth=0)
    password_entry.config(show="X")
    password_entry.grid(row=2,column=3)
    # Submit button
    photo_registry = ImageTk.PhotoImage(Image.open(resources_path+"\iregistor2.jpg"))
    registry = Button(frame,image=photo_registry,borderwidth=0,command = registoring)
    registry.grid(row=2,column=4,sticky=W)


if __name__ == '__main__':
    root = Tk()

    resources_path = 'd:\\Programing\\GIT\\mytestcode\\Tikinter\\labsoft\\resources'
    root.iconbitmap(resources_path+"\\ifavicon.ico")
    frame = Frame(root)
    frame.grid(row=0, column=0)
    build_registration_form(resources_path,frame)

    root.mainloop()

