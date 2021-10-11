from os import name
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import time
import sqlite3

REGISTRATION_LOGO = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/register_images/icons8-virus-58.png"
NAME = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/register_images/icons8-user-48.png"
AGE = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/register_images/icons8-age-48.png"
CARD = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/register_images/icons8-card-48.png"
VACCINE = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/register_images/icons8-syringe-48.png"
BACK = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/register_images/icons8-go-back-48.png"
SUBMIT = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/register_images/icons8-enter-48.png"
ADD_PACIE = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/register_images/icons8-add-tag-48.png"

class RegistrationForm :
    def __init__(self,log) :
        self.log = log
    def registration_comapare_screen(self) :

        regi_img = PhotoImage(file=REGISTRATION_LOGO)
        self.log.iconphoto(False, regi_img)
        self.log.title("Registration")
        self.log.resizable(False,False)


        screen_width = 560
        screen_height = 280

        windows_width = self.log.winfo_screenwidth()
        windows_height = self.log.winfo_screenheight()

        center_x = windows_width//2 - screen_width//2
        center_y = windows_height//2 - screen_height//2

        self.log.geometry("{}x{}+{}+{}".format(screen_width,screen_height,center_x,center_y))
    def registration_add_images(self) :
        self.regi_name = ImageTk.PhotoImage(Image.open(NAME))
        self.regi_age = ImageTk.PhotoImage(Image.open(AGE))
        self.regi_card = ImageTk.PhotoImage(Image.open(CARD))
        self.regi_vaccine = ImageTk.PhotoImage(Image.open(VACCINE))
        self.regi_back = ImageTk.PhotoImage(Image.open(BACK))
        self.regi_submit = ImageTk.PhotoImage(Image.open(SUBMIT))
        self.regi_pacient = ImageTk.PhotoImage(Image.open(ADD_PACIE))
    def registration_form(self) :
        self.name_label = Label(self.log, image=self.regi_name, text="Name                                 :", font=("Source Sans Pro", 12,'bold'), compound=LEFT)
        self.name_label.grid(row=1,sticky=W)
        self.age_lable = Label(self.log, image=self.regi_age, text="Age                                    :", font=("Source Sans Pro",12,'bold'),compound=LEFT)
        self.age_lable.grid(row=2,sticky=W)
        self.identy_lable = Label(self.log, image=self.regi_card, text="Identy Card                        :", font=("Source Sans Pro", 12, 'bold'), compound=LEFT)
        self.identy_lable.grid(row=3,sticky=W)
        self.vaccine_lable = Label(self.log, image=self.regi_vaccine, text="Vaccines                            :", font=("Source Sans Pro", 12, 'bold'), compound=LEFT)
        self.vaccine_lable.grid(row=4, sticky=W)

    


        self.name = ttk.Entry(self.log, font=("Source Sans Pro",12,'bold'),width=22)
        self.name.grid(row=1,column=1)
        self.age = ttk.Entry(self.log, font=("Source Sans Pro", 12, 'bold'),width=22)
        self.age.grid(row=2, column=1)
        self.card = ttk.Entry(self.log, font=("Source Sans Pro", 12, 'bold'),width=22)
        self.card.grid(row=3, column=1)
        self.vaccine = ttk.Combobox(self.log, values=["Oxford-AstraZeneca", "Johnson & Jhonson's", "Pfizer", "Moderna", "inovio","Sputnik V", "EpiVacCorona", "CoronaVac/SinoVac", "Covaxin", "No Vaccine Getted"], font=("Source Sans Pro", 12, 'bold'),width=21)
        self.vaccine.grid(row=4, column=1)

        self.submit_button = Button(self.log, image=self.regi_submit, text="submit", font=("Source Sans Pro", 12, 'bold'), compound=LEFT, command=self.submit_function,borderwidth=0)
        self.submit_button.grid(row=5,sticky=E)
        self.back_button = Button(self.log, image=self.regi_back, text="go back", font=("Source Sans Pro", 12, 'bold'), compound=LEFT, command=self.back_function, borderwidth=0)
        self.back_button.grid(row=5, sticky=W)
        self.add_pacient = Button(self.log, image=self.regi_pacient, text="add form:", font=("Source Sans Pro", 12, 'bold'),borderwidth=0, compound=LEFT, command=self.add_pacient_function)
        self.add_pacient.grid(row=5,column=1,sticky=W)

        self.log.mainloop()

    def submit_function(self) :
        get_name     = self.name.get()
        get_age      = self.age.get()
        get_card     = self.card.get()
        get_vaccine  = self.vaccine.get()

        import database as db

        myDatabase = db.DatabaseHandelling(get_name,get_age,get_card,get_vaccine)
        myDatabase.databases_handelling()
    def back_function(self) :

        self.log.destroy()
        
        import choose as c

        myBack = c.ChooseForm(Tk())
        myBack.choose_screen_resolution()
        myBack.make_images()
        myBack.make_choosing_form()
        myBack.registration()
        myBack.introduction_form()

    def add_pacient_function(self) :

        self.name.delete(0,END)
        self.age.delete(0,END)
        self.card.delete(0,END)
        self.vaccine.delete(0,END)