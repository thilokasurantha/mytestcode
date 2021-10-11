from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

ICONS_PATH = r"D:\Programing\GIT\mytestcode\Tikinter\Labsoft Software Secondry\images"
FILE_PATH = r"D:\Programing\GIT\mytestcode\Tikinter\Labsoft Software Secondry\Text_Folders"
USERNAME_ICONS = ICONS_PATH+"\icons8-name-48.png"
PASSWORD_ICONS = ICONS_PATH+"\icons8-forgot-password-48.png"
SCREEN_ICONS = ICONS_PATH+"\icons8-licence-48.png"
SUBMIT_ICONS = ICONS_PATH+"\icons8-enter-48.png"
CHOOSE_LAB_PATH = r"D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons"
ASGIRIYA = CHOOSE_LAB_PATH+"\isgiriya.png"
HASALAKA = CHOOSE_LAB_PATH+"\iasalaka.png"
METHSUWA = CHOOSE_LAB_PATH+"\iethsuwa.png"
FAMILY = CHOOSE_LAB_PATH+"\iamily.png"
TEST_REQUEST = CHOOSE_LAB_PATH+"\itest_request.png"
NEW_TEST_REQUEST = CHOOSE_LAB_PATH+"\inew_test.png"
REQUEST = CHOOSE_LAB_PATH+"\ireport.png"

class LoginForm:
    def __init__(self, login):
        self.login = login

    def loged_make_screen(self):
        self.image = PhotoImage(file=SCREEN_ICONS)
        self.login.iconphoto(False, self.image)
        self.login.title("Loging")

    def loged_importing_images(self):
        self.login_username = ImageTk.PhotoImage(Image.open(USERNAME_ICONS))
        self.login_passwords = ImageTk.PhotoImage(Image.open(PASSWORD_ICONS))
        self.login_submit = ImageTk.PhotoImage(Image.open(SUBMIT_ICONS))

    def loged_form(self):
        self.login_username_label = Label(self.login, image=self.login_username,text="username  :", compound=LEFT, font=("Source Sans Pro", 12, 'bold'))
        self.login_username_label.grid(row=1)
        self.login_username_entry = ttk.Entry(self.login, font=("Source Sans Pro", 12, 'bold'))
        self.login_username_entry.grid(row=1, column=1)

        self.login_passwords_label = Label(self.login, image=self.login_passwords,text="password  :", compound=LEFT, font=("Source Sans Pro", 12, 'bold'))
        self.login_passwords_label.grid(row=2)
        self.login_passwords_entry = ttk.Entry(self.login, font=("Source Sans Pro", 12, 'bold'), show="*")
        self.login_passwords_entry.grid(row=2, column=1)

        self.login_submit_button = Button(self.login, borderwidth=0, image=self.login_submit, text="login", font=("Source Sans Pro", 12, 'bold'), command=self.loged_function, compound=LEFT, bg="#ffffff", activebackground="#ffffff")
        self.login_submit_button.grid(row=3, column=1, sticky=E)

        self.login.mainloop()

    def loged_function(self):
        import login_file_handelling

        self.file = login_file_handelling.LoginFileHandelling(self.login, self.login_username_entry.get(), self.login_passwords_entry.get(), self.login_username_entry, self.login_passwords_entry)
        self.file.login_file_handelling()
        # myLog = LoginFileHandelling(self.login, self.login_username_entry.get(), self.login_passwords_entry.get(), self.login_username_entry, self.login_passwords_entry)
        # myLog.login_file_handelling()


# class LoginFileHandelling:
#     def __init__(self, form, login_name, login_password, get_username_entry, get_password_entry):
#         self.get_user_entry = get_username_entry
#         self.get_pass = get_password_entry
#         self.form = form
#         self.login_name = login_name
#         self.login_password = login_password

#     def login_file_handelling(self):
#         self.open_username = open(FILE_PATH+"\\username.txt")
#         self.read_username = self.open_username.read()
#         self.open_username.close()

#         self.open_password = open(FILE_PATH+"\\password.txt", "r")
#         self.read_password = self.open_password.read()
#         self.open_password.close()

#         self.dictonary_username = {
#             "username": self.read_username
#         }
#         print(self.dictonary_username["username"])
#         self.dictonary_password = {
#             "password": self.read_password
#         }
#         print(self.dictonary_password["password"])
#         if ((self.dictonary_username["username"] == self.login_name) and (self.dictonary_password["password"] == self.login_password)):
#             self.form.destroy()
#             import choosing

#             self.myChooseLab = choosing.ChosingLabForm(Tk())
#             self.myChooseLab.choosing.choose_compare_screen()
#             self.myChooseLab.choosing.choose_lab_form()
#         else:
#             self.answer = messagebox.showerror(
#                 "Error", "Invaliad Username or Password.")
#             if (self.answer == "ok"):
#                 self.get_user_entry.delete(0, END)
#                 self.get_pass.delete(0, END)
                

log = LoginForm(Tk())
log.loged_make_screen()
log.loged_importing_images()
log.loged_form()
log.loged_function()
