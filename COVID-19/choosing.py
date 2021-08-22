from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk

class MainGUI :
    def __init__(self,virus) :
        self.virus = virus
    def make_screen(self) :
        pass
    def choosing(self):
        self.resource = "D:\Programing\GIT\mytestcode\Tikinter\COVID-19\covid-19 prevention images"
        self.covid = ImageTk.PhotoImage(Image.open(self.resource+"\\virus.png"))
        self.covid_button = Button(self.virus, image = self.covid,text="Covid Registration",compound=LEFT,font=("Cosolas",20),width=700,justify='left',command=self.covids)
        self.covid_button.pack(anchor=E)

        self.introduction = ImageTk.PhotoImage(Image.open(self.resource+"\\mask-fi.png"))
        self.introduction_button = Button(self.virus, image = self.introduction , text="Covid-19 Healthy Introduction",font=("Consolas",20),compound=LEFT,width=700,command=self.introductions)
        self.introduction_button.pack()

        self.virus.mainloop()
    def covids(self) :
        self.virus.destroy()
        
        myRegistry = Registration()
        myRegistry.make_screen()
        myRegistry.import_images()
        myRegistry.make_gui(Tk())
        myRegistry.registered()

    def introductions(self) :
        self.virus.destroy()

        myObj = Prevention(Tk())
        myObj.make_screen()
        myObj.prevention_or_registration()
        myObj.importing_images_for_programme()
        myObj.reports()
        myObj.frames()
        myObj.make_gui()


class Prevention:
    def __init__(self, root):
        self.root = root

    def make_screen(self):
        self.image = PhotoImage(file="D:\Programing\GIT\mytestcode\Tikinter\COVID-19\covid-19 prevention images\\virus.png")
        self.root.resizable(False, False)
        self.root.iconphoto(0, self.image)
        self.root.title("Covid-19 Healthy Introduction List")
        self.gui_width = 1290
        self.gui_height = 608

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.center_x = self.screen_width//2 - self.gui_width//2
        self.center_y = self.screen_height//2 - self.gui_height//2

        self.root.geometry("{}x{}+{}+{}".format(self.gui_width,self.gui_height, self.center_x, self.center_y))

    def prevention_or_registration(self):
        pass

    def importing_images_for_programme(self):
        self.resource = "D:\Programing\GIT\mytestcode\Tikinter\COVID-19\covid-19 prevention images"

        self.hand_santizer = ImageTk.PhotoImage(Image.open(self.resource+"\\alcohol-fi_wkEKr7k.png"))
        self.wash_hads = ImageTk.PhotoImage(Image.open(self.resource+"\\jabon-fi.png"))
        self.mask = ImageTk.PhotoImage(Image.open(self.resource+"\\mask-fi.png"))
        self.doctor = ImageTk.PhotoImage(Image.open(self.resource+"\\doctor-fi.png"))

    def reports(self):
        self.report_1 = """Handwashing is an easy, cheap, and effective way to prevent the spread of germs and keep kids and adults healthy.\nWhen your family is healthy, you don’t\nhave to worry about missing school, work, or other activities."""
        self.report_2 = """Handwashing is one of the best ways to protect yourself and your family from getting sick.\nLearn when and how you should wash your hands to stay healthy."""
        self.report_3 = """Masks should be used as part of a comprehensive strategy of measures to suppress transmission and save lives; the use of a mask\nalone is not sufficient to provide an adequate level of protection against COVID-19.\n\nIf COVID-19 is spreading in your community, stay safe by taking some simple precautions, such as physical distancing, wearing a\nmask, keeping rooms well ventilated, avoiding crowds, cleaning your hands, and coughing into a bent elbow or tissue. Check local\nadvice where you live and work. Do it all!.\n\nMake wearing a mask a normal part of being around other people. The appropriate use, storage and cleaning or disposal of\nnmasks are essential to make them as effective as possible."""
        self.report_4 = """Immediately if you are infected with covid 19 Must see a doctor.That way you can heal covid 19"""

    def frames(self):
        self.hand_santizer_frame = Frame(self.root)
        self.hand_santizer_frame.grid(row=1, column=1, sticky=W)

        self.hand_wash_frame = Frame(self.root)
        self.hand_wash_frame.grid(row=2, column=1, sticky=W)

        self.mask_frame = Frame(self.root)
        self.mask_frame.grid(row=3, column=1, sticky=W)

        self.doctor_frame = Frame(self.root)
        self.doctor_frame.grid(row=4, column=1, sticky=W)

    def make_gui(self):
        self.hand_santizer_label = Label(self.root, image=self.hand_santizer)
        self.hand_santizer_label.grid(row=1, sticky=W)
        self.hand_santizer_report = Label(self.hand_santizer_frame, text=self.report_1, font=("Consolas", 12), justify="left")
        self.hand_santizer_report.grid(row=1, column=1)

        self.hand_wash_label = Label(self.root, image=self.wash_hads)
        self.hand_wash_label.grid(row=2, sticky=W)
        self.hand_wash_report = Label(self.hand_wash_frame, text=self.report_2, font=("Consolas", 12), justify="left")
        self.hand_wash_report.grid(row=2, column=1)

        self.mask_label = Label(self.root, image=self.mask)
        self.mask_label.grid(row=3, sticky=W)
        self.mask_report = Label(self.root, text=self.report_3, font=("Consolas", 12), justify="left")
        self.mask_report.grid(row=3, column=1, pady=2)

        self.doctor_label = Label(self.root, image=self.doctor)
        self.doctor_label.grid(row=4, sticky=W)
        self.doctor_report = Label(self.doctor_frame, text=self.report_4, font=("Consolas", 12), justify="left")
        self.doctor_report.grid(row=4, column=1, pady=2)
        self.root.mainloop()


class Registration :
    def __init__(self,names,ages,identys,ranges,vaccines) :
        self.names = names
        self.ages = ages
        self.identys = identys
        self.ranges = ranges
        self.vaccines = vaccines

    def make_screen(self) :
        self.paths = "D:\Programing\GIT\mytestcode\Tikinter\COVID-19\covid-19 prevention images\cregistration"
        self.image = PhotoImage(file=self.paths+"\\icons8-virus-58.png")
        self.paper.iconphoto(False,self.image)
        self.paper.title("Covid-19 Registration Form")
    def frames(self):
        pass
    def import_images(self) :
        self.regitry_resource = "D:\Programing\GIT\mytestcode\Tikinter\COVID-19\covid-19 prevention images\cregistration"
        self.name = ImageTk.PhotoImage(Image.open(self.regitry_resource+"\\icons8-user-48.png"))
        self.age = ImageTk.PhotoImage(Image.open(self.regitry_resource+"\\icons8-age-48.png"))
        self.card = ImageTk.PhotoImage(Image.open(self.regitry_resource+"\\icons8-card-48.png"))
        self.vaccine = ImageTk.PhotoImage(Image.open(self.regitry_resource+"\\icons8-syringe-48.png"))
        self.enter = ImageTk.PhotoImage(Image.open(self.regitry_resource+"\\icons8-enter-48.png"))
        self.range = ImageTk.PhotoImage(Image.open(self.regitry_resource+"\\icons8-parenting-48.png"))
    def make_gui(self,paper) :
        self.paper = paper

        self.name_image_and_label = Label(self.paper, image=self.name, text="Name              :", font=("Source Sans Pro", 12,'bold'), compound=LEFT)
        self.name_image_and_label.grid(row=1,sticky=W)
        self.age_image_and_label = Label(self.paper, image=self.age, text="Age                 :", font=("Source Sans Pro",12,'bold'),compound=LEFT)
        self.age_image_and_label.grid(row=2,sticky=W)
        self.identy_image_and_label = Label(self.paper, image=self.card, text="Identy Card   :", font=("Source Sans Pro", 12, 'bold'), compound=LEFT)
        self.identy_image_and_label.grid(row=3,sticky=W)
        self.vaccine_image_and_label = Label(self.paper, image=self.vaccine, text="Vaccines       :", font=("Source Sans Pro", 12, 'bold'), compound=LEFT)
        self.vaccine_image_and_label.grid(row=4, sticky=W)
        self.range_image_and_label = Label(self.paper, image=self.range, text="Ranging        :", font=("Source Sans Pro", 12, 'bold'), compound=LEFT)
        self.range_image_and_label.grid(row=5, sticky=W)
        self.enter_button_image = Button(self.paper, image=self.enter, text="submit", font=("Source Sans Pro", 12, 'bold'), compound=LEFT, command=self.registered,borderwidth=0)
        self.enter_button_image.grid(row=6,column=1,sticky=E)


        self.name_entry = ttk.Entry(self.paper, font=("Source Sans Pro",12,'bold'),width=22)
        self.name_entry.grid(row=1,column=1)
        self.age_entry = ttk.Entry(self.paper, font=("Source Sans Pro", 12, 'bold'),width=22)
        self.age_entry.grid(row=2, column=1)
        self.card_entry = ttk.Entry(self.paper, font=("Source Sans Pro", 12, 'bold'),width=22)
        self.card_entry.grid(row=3, column=1)
        self.vaccine_entry = ttk.Combobox(self.paper, values=["Oxford-AstraZeneca", "Johnson & Jhonson's", "Pfizer", "Moderna", "inovio","Sputnik V", "EpiVacCorona", "CoronaVac/SinoVac", "Covaxin", "No Vaccine Getted"], font=("Source Sans Pro", 12, 'bold'))
        self.vaccine_entry.grid(row=4, column=1)
        self.number_ranges = ttk.Combobox(self.paper, values=["0 - 10","10 - 18","18 - 60","60 - higher"],width=30)
        self.number_ranges.grid(row=5,column=1)
        self.root.mainloop()
    def registered(self) :
        myAdvance = RegistrationFileHandelling(self.name_entry.get(), self.age_entry.get(), self.card_entry.get(), self.number_ranges.get(), self.vaccine_entry.get())
        myAdvance.file_handelling()

class RegistrationFileHandelling(Registration):
    def __init__(self, names, ages, identys, ranges, vaccines) :
        Registration.__init__(self, names, ages, identys, ranges, vaccines)

    def file_handelling(self) :
        print(self.name_entry.get())
if __name__ == '__main__':
    myObj1 = MainGUI(Tk())
    myObj1.make_screen()
    myObj1.choosing()

