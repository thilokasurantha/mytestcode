from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import time

class CovidVaccine :
    def __init__(self,root) :
        self.root = root
    def make_screen(self) :
        self.gui_width = 542
        self.gui_height = 210

        self.window_width = self.root.winfo_screenwidth()
        self.window_height = self.root.winfo_screenheight()

        self.center_x = self.window_width//2 - self.gui_width//2
        self.center_y = self.window_height//2 - self.gui_height//2

        self.root.geometry("{}x{}+{}+{}".format(self.gui_width,self.gui_height,self.center_x,self.center_y))
        self.root.resizable(False,False)

        self.root.iconbitmap("D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources\Icons8-Windows-8-Healthcare-Virus.ico")
        self.root.title("Covid - 19 Vaccine Registration")
    def covid_vaccine_registory(self) :

        self.resources = "D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
        
        self.name = ttk.Label(self.root,text="Enter Your Name  :",font=("Arial Black",16,'bold'))
        self.name.grid(row=1,column=0,sticky=E)
        self.name_entry = ttk.Entry(self.root, font=("Arial Black",16,'bold'))
        self.name_entry.grid(row=1,column=1)

        self.age = ttk.Label(self.root, text="Enter Your Age  :",font=("Arial Black", 16, 'bold'))
        self.age.grid(row=2,sticky=E)
        self.age_entry = ttk.Entry(self.root, font=("Arial Black", 16, 'bold'))
        self.age_entry.grid(row=2,column=1)

        self.identy = ttk.Label(self.root, text="Identy Card Number  :",font=("Arial Black", 16, 'bold'))
        self.identy.grid(row=3, sticky=E)
        self.identy_entry = ttk.Entry(self.root, font=("Arial Black", 16, 'bold'),width=20)
        self.identy_entry.grid(row=3, column=1)

        self.vaccine = ttk.Label(self.root, text="Enter Viccine Name  :", font=("Arial Black", 16, 'bold'))
        self.vaccine.grid(row=4, sticky=E)
        self.vaccine_combo = ttk.Combobox(self.root, value=["Oxford-AstraZeneca", "Johnson & Jhonson's", "Pfizer", "Moderna", "inovio", "Sputnik V", "EpiVacCorona", "CoronaVac/SinoVac", "Covaxin","No Vaccine Getted"], font=("Arial Black",15),width=20)
        self.vaccine_combo.grid(row=4,column=1,sticky=W)

        self.submit = ImageTk.PhotoImage(Image.open(self.resources+"\sub.png"))
        self.login_registry = Button(self.root, image=self.submit,borderwidth=0,command=self.when_button_clicked)
        self.login_registry.grid(row=5, column=0, sticky=W)

        self.root.mainloop()
    def when_button_clicked(self) :
        self.get_name = self.name_entry.get()
        self.get_age = self.age_entry.get()
        self.identy_card = self.identy_entry.get()
        self.get_vaccine = self.vaccine_combo.get()

        self.saving_resositories = "D:\Programing\GIT\mytestcode\Classes\covid19_virus_registory"
        self.savong_test_source_path = "D:\Programing\GIT\mytestcode\Classes\covid19_virus_registory\making_derectory"

        self.saving_the_name = open( self.saving_resositories+"\covid_registory_names.txt", "a")
        self.saving_the_name.write("{} \n".format(self.get_name))
        self.saving_the_name.close()
        self.saving_the_vaccines = open(self.saving_resositories+"\covid_registory_vaccines.txt", "a")
        self.saving_the_vaccines.write("{} \n".format(self.get_vaccine))

        self.catogories_name = str(self.get_name.split())

        self.saving_test = open(self.savong_test_source_path+"\{}_pacient.txt".format(self.catogories_name[0]),"x")
        self.aditing = (
            "Pacient Name                    =>> {} \n"
            "Pacient Age                     =>> {} \n"
            "Pacient ID                      =>> {} \n"
            "The pacient vaccine that struck =>> {} \n"
        ).format(self.get_name, self.get_age, self.identy_card, self.get_vaccine)
        self.saving_test.write(self.aditing)
        self.saving_test.close()

        self.all_done = Label(self.root, text="Dear Pacient All Done.", fg="red", font=("Arial Black",10))
        self.all_done.grid(row=6,column=1)

        exit()

if __name__ == '__main__':
    myObj = CovidVaccine(Tk())
    myObj.make_screen()
    myObj.covid_vaccine_registory()
    myObj.when_button_clicked()