from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox

def login_function():
    get_username = open("username.txt" , 'r')
    get_password = open("password.txt",'r')

    with get_username as user :
        user_n = user.readline()

    with get_password as passwor :
        pass_w = passwor.readline()

    username = login_username_entry.get()
    password = login_password_entry.get()

    choose_the_lab(user_n,pass_w,username,password)

def choose_the_lab(user_n,pass_w,username,password) :
    if ((username == user_n) and (password == pass_w)) :
        login.destroy()
        import coose_lab
    else :
        warninig = messagebox.showwarning("Warning","Your Username or Passowrd incorrect .")
        if (warninig == "ok") :
            ask = messagebox.askquestion("Wanting","Do you want to show prassword and username.")
            if (ask == "yes") :
                show_username = open("username.txt","r")
                show_password = open("password.txt","r")
                print(show_username.read())
                print(show_password.read())
                login_username_entry.delete(0,END)
                login_password_entry.delete(0,END)

login = Tk()
resources = "D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
login.iconbitmap(resources + "\pythontutorial-1-150x150.ico")
login.title("Registring Form")

window_width = 645
window_height = 95

screen_width = login.winfo_screenwidth()
screen_height = login.winfo_screenheight()

center_x = (screen_width // 2 - window_width // 2)
center_y = (screen_height // 2 - window_height // 2)

login.geometry("{}x{}+{}+{}".format(window_width, window_height, center_x, center_y))
# Username photo
login_photo_username = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK_SOFTWARE_MAKING\photos\icons8-user-90.png"))
login_username_images = Label(image=login_photo_username)
login_username_images.grid(row=1, sticky=W)
# Enter the username
login_username = Label(login, text="USER NAME :", font=("Arial Black", 16), borderwidth=0)
login_username.grid(row=1, column=2, sticky=W)
login_username_entry = ttk.Entry(login, width=25, font=("Arial Black", 16))
login_username_entry.grid(row=1, column=3)
# Password photo
login_photo_password = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK_SOFTWARE_MAKING\photos\icons8-password-96.png"))
login_password_images = Label(image=login_photo_password)
login_password_images.grid(row=2, sticky=W)
# Enter the password
login_password = Label(login, text="PASSWORD :", font=("Arial Black", 16), borderwidth=0)
login_password.grid(row=2, column=2, sticky=E)
login_password_entry = ttk.Entry(login, width=25, font=("Arial Black", 16))
login_password_entry.config(show="X")
login_password_entry.grid(row=2, column=3)
# Submit button
frame_button = Frame(login, bg="black")
frame_button.grid(row=2, column=4)
submit = ImageTk.PhotoImage(Image.open(resources+"\sub.png"))
login_registry = Button(frame_button , image = submit , borderwidth=0,command=login_function)
login_registry.grid(row=2, column=4, sticky=W)
login.mainloop()
