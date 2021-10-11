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

class RegisterForm :
    def __init__(self,root) :
        self.root = root
    def registry_make_screen(self) :
        self.image = PhotoImage(file=SCREEN_ICONS)
        self.root.iconphoto(False, self.image)
        self.root.title("Registerd")
    def registry_importing_photos(self) :
        self.username = ImageTk.PhotoImage(Image.open(USERNAME_ICONS))
        self.passwords = ImageTk.PhotoImage(Image.open(PASSWORD_ICONS))
        self.submit = ImageTk.PhotoImage(Image.open(SUBMIT_ICONS))
    def registring_form(self):
        self.username_label = Label(self.root, image=self.username, text="username  :",compound=LEFT,font=("Source Sans Pro",12,'bold'))
        self.username_label.grid(row=1)
        self.username_entry = ttk.Entry(self.root, font=("Source Sans Pro",12,'bold'))
        self.username_entry.grid(row=1,column=1)

        self.passwords_label = Label(self.root, image=self.passwords, text="password  :",compound=LEFT, font=("Source Sans Pro", 12, 'bold'))
        self.passwords_label.grid(row=2)
        self.passwords_entry = ttk.Entry(self.root, font=("Source Sans Pro",12,'bold'),show="*")
        self.passwords_entry.grid(row=2,column=1)

        self.submit_button = Button(self.root, borderwidth=0, image=self.submit, text="registerd", font=("Source Sans Pro",12,'bold'), command=self.register,compound=LEFT,bg="#ffffff",activebackground="#ffffff")
        self.submit_button.grid(row=3,column=1,sticky=E)
    
        self.root.mainloop()

    def register(self) :
        myRegistry = RegistringFileHandelling(self.username_entry.get(),self.passwords_entry.get())
        myRegistry.registring_file_handelling()

        self.root.destroy()
        
        myLogin = LoginForm(Tk())
        myLogin.login_make_screen()
        myLogin.login_importing_images()
        myLogin.login_form()

class RegistringFileHandelling :
    def __init__(self,name,password) :
        self.name = name
        self.password = password
    def registring_file_handelling(self) :
        self.file_username = open(FILE_PATH+"\\username.txt","w")
        self.file_username.write("{}".format(self.name))
        self.file_username.close()

        self.file_pasword = open(FILE_PATH+"\\password.txt","w")
        self.file_pasword.write("{}".format(self.password))
        self.file_pasword.close()


class LoginForm:
    def __init__(self, login):
        self.login = login

    def login_make_screen(self):
        self.image = PhotoImage(file=SCREEN_ICONS)
        self.login.iconphoto(False, self.image)
        self.login.title("Loging")

    def login_importing_images(self):
        self.login_username = ImageTk.PhotoImage(Image.open(USERNAME_ICONS))
        self.login_passwords = ImageTk.PhotoImage(Image.open(PASSWORD_ICONS))
        self.login_submit = ImageTk.PhotoImage(Image.open(SUBMIT_ICONS))

    def login_form(self):
        self.login_username_label = Label(self.login, image=self.login_username, text="username  :",compound=LEFT, font=("Source Sans Pro", 12, 'bold'))
        self.login_username_label.grid(row=1)
        self.login_username_entry = ttk.Entry(self.login, font=("Source Sans Pro", 12, 'bold'))
        self.login_username_entry.grid(row=1, column=1)

        self.login_passwords_label = Label(self.login, image=self.login_passwords,text="password  :", compound=LEFT, font=("Source Sans Pro", 12, 'bold'))
        self.login_passwords_label.grid(row=2)
        self.login_passwords_entry = ttk.Entry(self.login, font=("Source Sans Pro", 12, 'bold'), show="*")
        self.login_passwords_entry.grid(row=2, column=1)

        self.login_submit_button = Button(self.login, borderwidth=0, image=self.login_submit, text="login", font=("Source Sans Pro", 12, 'bold'), command=self.login_function, compound=LEFT, bg="#ffffff", activebackground="#ffffff")
        self.login_submit_button.grid(row=3, column=1, sticky=E)

        self.login.mainloop()

    def login_function(self):
        myLog = LoginFileHandelling(self.login,self.login_username_entry.get(),self.login_passwords_entry.get(),self.login_username_entry,self.login_passwords_entry)
        myLog.login_file_handelling()

class LoginFileHandelling :
    def __init__(self,form,login_name,login_password,get_username_entry,get_password_entry) :
        self.get_user_entry = get_username_entry
        self.get_pass = get_password_entry
        self.form = form
        self.login_name = login_name
        self.login_password = login_password
    def login_file_handelling(self) :
        self.open_username = open(FILE_PATH+"\\username.txt")
        self.read_username = self.open_username.read()
        self.open_username.close()

        self.open_password = open(FILE_PATH+"\\password.txt","r")
        self.read_password = self.open_password.read()
        self.open_password.close()

        self.dictonary_username = {
            "username" : self.read_username
        }
        print(self.dictonary_username["username"])
        self.dictonary_password = {
            "password" : self.read_password
        }
        print(self.dictonary_password["password"])
        if ((self.dictonary_username["username"] == self.login_name) and (self.dictonary_password["password"] == self.login_password)) :
            self.form.destroy()
            myChooseLab = ChosingLabForm(Tk())
            myChooseLab.choose_compare_screen()
            myChooseLab.choose_lab_form()
        else :
            self.answer = messagebox.showerror("Error","Invaliad Username or Password.")
            if (self.answer == "ok") :
                self.get_user_entry.delete(0,END)
                self.get_pass.delete(0,END)

class ChosingLabForm :
    def __init__(self,choose) :
        self.choose = choose
    def choose_compare_screen(self) :
        pass
    def choose_lab_form(self) :
        # Asgiriya Lab
        self.asgiriya_lab = ImageTk.PhotoImage(Image.open(ASGIRIYA))
        self.asgiriya_lab_label = Button(image=self.asgiriya_lab, borderwidth=0)
        self.asgiriya_lab_label.grid(row=1)

        self.test_request_asgiriya = ImageTk.PhotoImage(Image.open(TEST_REQUEST))
        self.test_request_asgiriya_label = Button(image=self.test_request_asgiriya, borderwidth=0, command=self.test_request)
        self.test_request_asgiriya_label.grid(row=2)

        self.new_test_request_asgiriya = ImageTk.PhotoImage(Image.open(NEW_TEST_REQUEST))
        self.new_test_request_asgiriya_label = Button(image=self.new_test_request_asgiriya, borderwidth=0, command=self.new_test_request)
        self.new_test_request_asgiriya_label.grid(row=3)

        self.request_asgiriya = ImageTk.PhotoImage(Image.open(REQUEST))
        self.request_label_asgiriya = Button(image=self.request_asgiriya, borderwidth=0, command=self.request_details)
        self.request_label_asgiriya.grid(row=4)

        # Hasalaka Lab
        self.hasalaka_lab = ImageTk.PhotoImage(Image.open(HASALAKA))
        self.hasalaka_lab_label = Button(image=self.hasalaka_lab, borderwidth=0)
        self.hasalaka_lab_label.grid(row=5)

        self.test_request_hasalaka = ImageTk.PhotoImage(Image.open(TEST_REQUEST))
        self.test_request_hasalaka_label = Button(image=self.test_request_hasalaka, borderwidth=0, command=self.test_request)
        self.test_request_hasalaka_label.grid(row=6)

        self.new_test_request_hasalaka = ImageTk.PhotoImage(Image.open(NEW_TEST_REQUEST))
        self.new_test_request_hasalaka_label = Button(image=self.new_test_request_hasalaka, borderwidth=0, command=self.new_test_request)
        self.new_test_request_hasalaka_label.grid(row=7)

        self.request_hasalaka = ImageTk.PhotoImage(Image.open(REQUEST))
        self.request_label_hasalaka = Button(image=self.request_hasalaka, borderwidth=0, command=self.request_details)
        self.request_label_hasalaka.grid(row=8)

        # Methsuwa Lab
        self.methsuwa_lab = ImageTk.PhotoImage(Image.open(METHSUWA))
        self.methsuwa_lab_label = Button(image=self.methsuwa_lab, borderwidth=0)
        self.methsuwa_lab_label.grid(row=9)

        self.test_request_methsuwa = ImageTk.PhotoImage(Image.open(TEST_REQUEST))
        self.test_request_methsuwa_label = Button(image=self.test_request_methsuwa, borderwidth=0, command=self.test_request)
        self.test_request_methsuwa_label.grid(row=10)

        self.new_test_request_methsuwa = ImageTk.PhotoImage(Image.open(NEW_TEST_REQUEST))
        self.new_test_request_methsuwa_label = Button(image=self.new_test_request_methsuwa, borderwidth=0, command=self.new_test_request)
        self.new_test_request_methsuwa_label.grid(row=11)

        self.request_methsuwa = ImageTk.PhotoImage(Image.open(REQUEST))
        self.request_label_methsuwa = Button(image=self.request_methsuwa, borderwidth=0, command=self.request_details)
        self.request_label_methsuwa.grid(row=12)

        # Family Lab
        self.family_lab = ImageTk.PhotoImage(Image.open(FAMILY))
        self.family_lab_label = Button(image=self.family_lab, borderwidth=0)
        self.family_lab_label.grid(row=13)

        self.test_request_family = ImageTk.PhotoImage(Image.open(TEST_REQUEST))
        self.test_request_family_label = Button(image=self.test_request_family, borderwidth=0, command=self.test_request)
        self.test_request_family_label.grid(row=14)

        self.new_test_request_family = ImageTk.PhotoImage(Image.open(NEW_TEST_REQUEST))
        self.new_test_request_family_label = Button(image=self.new_test_request_family, borderwidth=0, command=self.new_test_request)
        self.new_test_request_family_label.grid(row=15)

        self.request_family = ImageTk.PhotoImage(Image.open(REQUEST))
        self.request_label_family = Button(image=self.request_family, borderwidth=0, command=self.request_details)
        self.request_label_family.grid(row=16)

        self.choose.mainloop()  
    def test_request(self):
        pass
    
    def new_test_request(self):
        self.choose.destroy()
        import new_test_request

        self.importing_new_test = new_test_request.NewTestRequestForm(Tk())
        self.importing_new_test.new_test_request_compare_screen()
    
    def request_details(self):
        pass


if __name__ == '__main__':
    myForm = RegisterForm(Tk())
    myForm.registry_importing_photos()
    myForm.registry_make_screen()
    myForm.registring_form()
