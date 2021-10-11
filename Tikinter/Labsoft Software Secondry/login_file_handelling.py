import login
class LoginFileHandelling:
    def __init__(self, form, login_name, login_password, get_username_entry, get_password_entry):
        self.get_user_entry = get_username_entry
        self.get_pass = get_password_entry
        self.form = form
        self.login_name = login_name
        self.login_password = login_password

    def login_file_handelling(self):
        self.open_username = open(FILE_PATH+"\\username.txt")
        self.read_username = self.open_username.read()
        self.open_username.close()

        self.open_password = open(FILE_PATH+"\\password.txt", "r")
        self.read_password = self.open_password.read()
        self.open_password.close()

        self.dictonary_username = {
            "username": self.read_username
        }
        print(self.dictonary_username["username"])
        self.dictonary_password = {
            "password": self.read_password
        }
        print(self.dictonary_password["password"])
        if ((self.dictonary_username["username"] == self.login_name) and (self.dictonary_password["password"] == self.login_password)):
            self.form.destroy()
            import choosing

            self.myChooseLab = choosing.ChosingLabForm(Tk())
            self.myChooseLab.choosing.choose_compare_screen()
            self.myChooseLab.choosing.choose_lab_form()
        else:
            self.answer = messagebox.showerror(
                "Error", "Invaliad Username or Password.")
            if (self.answer == "ok"):
                self.get_user_entry.delete(0, END)
                self.get_pass.delete(0, END)
get = login.LoginForm(Tk())
x = get.loged_form()


