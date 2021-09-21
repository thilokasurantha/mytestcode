from tkinter import *
from PIL import ImageTk,Image
import rescue_the_virus

FORM_LOGO = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/choosing_images/virus.png"
INTRODUCTION = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/choosing_images/mask-fi.png"
REGISTRATION = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/choosing_images/virus.png"

class ChooseForm :
    def __init__(self,choose) :
        self.choose = choose

    def choose_screen_resolution(self) :
        image = PhotoImage(file=FORM_LOGO)
        self.choose.title("Main Menu")
        self.choose.iconphoto(False, image)
        self.choose.resizable(False,False)

        form_width = 526
        form_height = 280

        screen_width = self.choose.winfo_screenwidth()
        screen_height = self.choose.winfo_screenheight()

        center_x = screen_width//2 - form_width//2
        center_y = screen_height//2 - form_height//2

        self.choose.geometry("{}x{}+{}+{}".format(form_width,form_height,center_x,center_y))

    def make_images(self) :
        self.registration_logo = ImageTk.PhotoImage(Image.open(REGISTRATION))
        self.introduction_logo = ImageTk.PhotoImage(Image.open(INTRODUCTION))

    def make_choosing_form(self) :
        self.registration_button = Button(self.choose, image = self.registration_logo, text = "Registration", font=("Source Sans Pro",12,'bold'), compound = LEFT, command=self.registration, width=500)
        self.registration_button.pack()

        self.introduction_button = Button(self.choose, image = self.introduction_logo, text = "Introduction", font=("Source Sans Pro",12,'bold'), compound = LEFT, command=self.introduction_form, width=500)
        self.introduction_button.pack()
        self.choose.mainloop()
        
    def registration(self):
        self.choose.destroy()
        
        import registration_form as regi

        myRegistration = regi.RegistrationForm(Tk())
        myRegistration.registration_comapare_screen()
        myRegistration.registration_add_images()
        myRegistration.registration_form()
        myRegistration.submit_function()
        myRegistration.back_function()
        myRegistration.add_pacient_function()

    def introduction_form(self):
        self.choose.destroy()
        import rescue_the_virus as virus

        myRescue = virus.RescueForm(Tk())
        myRescue.rescue_screen_resolution()
        myRescue.reoprts()
        myRescue.rescue_form_make_images()
        myRescue.frames()
        myRescue.make_rescue_form()
        myRescue.back_function()


if __name__ == "__main__" :
    myObj = ChooseForm(Tk())
    myObj.choose_screen_resolution()
    myObj.make_images()
    myObj.make_choosing_form()
    myObj.registration()
    myObj.introduction_form()