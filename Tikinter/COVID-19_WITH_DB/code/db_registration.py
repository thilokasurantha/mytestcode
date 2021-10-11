from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error

NAME = r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\registration\user.png"
AGE = r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\registration\age.png"
NIC = r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\registration\nic_card.png"
VACCINE = r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\registration\vaccine.png"
QUANTUTY = r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\registration\poples.png"
ADD =  r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\registration\add.png"
BACK = r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\registration\back.png"
SUBMIT = r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\registration\submit.png"

class RegistrationForm :
    def __init__(self,regi) :
        self.regi = regi
    
    def registration_compare_screen(self) :
        pass

    def registration_import_img(self) :
        self.name = ImageTk.PhotoImage(Image.open(NAME))
        self.age = ImageTk.PhotoImage(Image.open(AGE))
        self.nic_card = ImageTk.PhotoImage(Image.open(NIC))
        self.vaccine = ImageTk.PhotoImage(Image.open(VACCINE))
        self.quantity = ImageTk.PhotoImage(Image.open(QUANTUTY))
        self.back = ImageTk.PhotoImage(Image.open(BACK))
        self.submit = ImageTk.PhotoImage(Image.open(SUBMIT))
        self.add = ImageTk.PhotoImage(Image.open(ADD))

    def registration_make_gui(self) :
        self.name_image_and_label = Label(self.regi, image=self.name, text="Name                                 :", font=("Source Sans Pro", 12, 'bold'), compound=LEFT)
        self.name_image_and_label.grid(row=1, sticky=W)
        self.age_image_and_label = Label(self.regi, image=self.age, text="Age                                    :", font=("Source Sans Pro", 12, 'bold'), compound=LEFT)
        self.age_image_and_label.grid(row=2, sticky=W)
        self.identy_image_and_label = Label(self.regi, image=self.nic_card, text="Identy Card                     :", font=("Source Sans Pro", 12, 'bold'), compound=LEFT)
        self.identy_image_and_label.grid(row=3, sticky=W)
        self.vaccine_image_and_label = Label(self.regi, image=self.vaccine, text="Vaccines                          :", font=("Source Sans Pro", 12, 'bold'), compound=LEFT)
        self.vaccine_image_and_label.grid(row=4, sticky=W)
        self.people = Label(self.regi, image=self.quantity, text="Population Quantity    :", font=("Source Sans Pro", 12, 'bold'), compound=LEFT)
        self.people.grid(row=5, sticky=W)

        self.name_entry = ttk.Entry(self.regi, font=("Source Sans Pro", 12, 'bold'), width=22)
        self.name_entry.grid(row=1, column=1)
        self.age_entry = ttk.Entry(self.regi, font=("Source Sans Pro", 12, 'bold'), width=22)
        self.age_entry.grid(row=2, column=1)
        self.card_entry = ttk.Entry(self.regi, font=("Source Sans Pro", 12, 'bold'), width=22)
        self.card_entry.grid(row=3, column=1)
        self.vaccine_entry = ttk.Combobox(self.regi, values=["Oxford-AstraZeneca", "Johnson & Jhonson's", "Pfizer", "Moderna", "inovio","Sputnik V", "EpiVacCorona", "CoronaVac/SinoVac", "Covaxin", "No Vaccine Getted"], font=("Source Sans Pro", 12, 'bold'))
        self.vaccine_entry.grid(row=4, column=1)
        self.pople_entry = ttk.Entry(self.regi, font=("Source Sans Pro", 12, 'bold'), width=22)
        self.pople_entry.grid(row=5, column=1)

        self.back_button = Button(self.regi, image=self.back, text="go back", font=("Source Sans Pro", 12, 'bold'), compound=LEFT, command=self.back_function, borderwidth=0)
        self.back_button.grid(row=7, sticky=W)
        self.enter_button = Button(self.regi, image=self.submit, text="submit", font=("Source Sans Pro", 12, 'bold'), compound=LEFT, command=self.register_handelling, borderwidth=0)
        self.enter_button.grid(row=7, sticky=E)
        self.add_button = Button(self.regi, image=self.add, text="add form:", font=("Source Sans Pro", 12, 'bold'), borderwidth=0, compound=LEFT, command=self.add_function)
        self.add_button.grid(row=7, column=1, sticky=W)

        self.regi.mainloop()

    def back_function(self) :
        self.regi.destroy()

        import choose_option

        firstPage = choose_option.ChooseOption(Tk())
        firstPage.make_screen()
        firstPage.choosing_option()

    def register_handelling(self) :
        connect = sqlite3.connect("D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\db_files\covid_registration.db")

        cursor = connect.cursor()

        self.name   = self.name_entry.get()
        self.age    = self.age_entry.get()
        self.identy = self.card_entry.get()
        self.vacc   = self.vaccine_entry.get()
        self.people = self.pople_entry.get()

        registration = [
            (self.name, self.age, self.identy, self.vacc, self.people)
        ]
        get_value = cursor.execute("SELECT * FROM covid_registration_form WHERE name = (?)",(self.name,))
        items = cursor.fetchall()

        if (len(items) == 0) :
            cursor.executemany("INSERT INTO covid_registration_form VALUES (?,?,?,?,?)",registration)
            print("Successfully Saved")

            mySaved = SavedAsText(self.name,self.age,self.identy,self.vacc,self.people)
            mySaved.save_as_text_file()
        else :
            messagebox.showerror("Error","You are alredy logged inn.")
            self.name_entry.delete(0, END)
            self.age_entry.delete(0, END)
            self.card_entry.delete(0, END)
            self.vaccine_entry.delete(0, END)
            self.pople_entry.delete(0, END)
        connect.commit()
        connect.close()



    def add_function(self):
        answer = messagebox.askquestion("Add","Do you want to add pacient ?")
        
        if (answer == "yes") :
            self.name_entry.delete(0,END)
            self.age_entry.delete(0,END)
            self.card_entry.delete(0,END)
            self.vaccine_entry.delete(0,END)
            self.pople_entry.delete(0,END)

class SavedAsText :
    def __init__(self,s_name,s_age,s_identy,s_vacc,s_people) :
        self.s_name = s_name
        self.s_age = s_age
        self.s_identy = s_identy
        self.s_vacc = s_vacc
        self.s_people = s_people

    def save_as_text_file(self) :
        open_txt = open("D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\\file\{}_pacient.txt".format(self.s_name), "x")

        create = (
            "Pacient Name                             =>> {} \n"
            "Pacient Age                              =>> {} \n"
            "Pacient Identy card                      =>> {} \n"
            "The pacient vaccine that struck          =>> {} \n"
            "Population Quantity                      =>> {} \n"
        ).format(self.s_name, self.s_age, self.s_identy, self.s_vacc, self.s_people)

        open_txt.write(create)
        open_txt.close()
    

    
