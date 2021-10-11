from tkinter import *
from PIL import ImageTk , Image
from tkinter import ttk
def registoring() :
    registry_username = username_entry.get()
    registry_password = password_entry.get()

    write_username = open("username.txt","w")
    write_username.write("{} \n".format(registry_username))
    write_username.close()

    write_password = open("password.txt","w")
    write_password.write("{} \n".format(registry_password))
    write_password.close()

    print("Successfully Saved :(")

    loging_form_gui(root,ttk)

def loging_form_gui(root,ttk) :
    
    root = Tk()
    # Username photo
    login_photo_username = ImageTk.PhotoImage(Image.open("D:\LABLK_SOFTWARE_MAKING\photos\icons8-user-90.png"))
    login_username_images = Label(image=login_photo_username)
    login_username_images.grid(row=1, sticky=W)
    # Enter the username
    login_username = Label(root, text="USER NAME :", font=("Arial Black", 16), borderwidth=0)
    login_username.grid(row=1, column=2, sticky=W)
    login_username_entry = ttk.Entry( root, width=25, font=("Arial Black", 16))
    login_username_entry.grid(row=1, column=3)
    # Password photo
    login_photo_password = ImageTk.PhotoImage(Image.open("D:\LABLK_SOFTWARE_MAKING\photos\icons8-password-96.png"))
    login_password_images = Label(image=login_photo_password)
    login_password_images.grid(row=2, sticky=W)
    # Enter the password
    login_password = Label(root, text="PASSWORD :", font=("Arial Black", 16), borderwidth=0)
    login_password.grid(row=2, column=2, sticky=E)
    login_password_entry = ttk.Entry( root, width=25, font=("Arial Black", 16))
    login_password_entry.config(show="X")
    login_password_entry.grid(row=2, column=3)
    # Submit button
    frame_button = Frame(root,bg="black")
    frame_button.grid(row=2,column=4)
    login_registry = Button(frame_button, text="LOGIN", font=("Arial Black", 16), borderwidth=0, command=login_function)
    login_registry.grid(row=2, column=4, sticky=W)

    login_function(login_username_entry, login_password_entry)

    root.mainloop()


def login_function(login_username_entry, login_password_entry):
    get_username = open("username.txt",'r')
    get_password = open("password.txt",'r')

    username = login_username_entry.get()
    password = login_password_entry.get()

    if (username == get_username) :
        print("successfull connected")
    else :
        print("bye")


if __name__ == '__main__':
    root = Tk()
    resources = "D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
    root.iconbitmap(resources+"\pythontutorial-1-150x150.ico")
    root.title("Registring Form")

    window_width = 645
    window_height = 95

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = (screen_width//2 - window_width//2)
    center_y = (screen_height//2 - window_height//2)

    root.geometry("{}x{}+{}+{}".format(window_width,window_height,center_x,center_y))

    # Username photo
    photo_username = ImageTk.PhotoImage(Image.open("D:\LABLK_SOFTWARE_MAKING\photos\icons8-user-90.png"))
    username_images = Label(image=photo_username)
    username_images.grid(row=1, sticky=W)
    # Enter the username
    username = Label(root, text="USER NAME :", font=("Arial Black", 16))
    username.grid(row=1, column=2, sticky=E)
    username_entry = ttk.Entry(root, width=25, font=("Arial Black", 16))
    username_entry.grid(row=1, column=3)
    # Password photo
    photo_password = ImageTk.PhotoImage(Image.open("D:\LABLK_SOFTWARE_MAKING\photos\icons8-password-96.png"))
    password_images = Label(image=photo_password)
    password_images.grid(row=2, sticky=W)
    # Enter the password
    password = Label(root, text="PASSWORD :", font=("Arial Black", 16))
    password.grid(row=2, column=2, sticky=E)
    password_entry = ttk.Entry(root, width=25, font=("Arial Black", 16))
    password_entry.config(show="X")
    password_entry.grid(row=2, column=3)
    # Submit button
    photo_registry = ImageTk.PhotoImage(Image.open("D:\LABLK_SOFTWARE_MAKING\photos\iregistor2.jpg"))
    registry = Button(image=photo_registry, borderwidth=0, command=registoring)
    registry.grid(row=2, column=4, sticky=W)

    registoring()

    root.mainloop()
