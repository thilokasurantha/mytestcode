from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

DISPLAY_ICON = r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\introduction\intro_virus.png"
VIRUS = r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\introduction\intro_virus.png"
MASK = r"D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\img\introduction\wearing_mask.png"

class ChooseOption :
    def __init__(self,choose) :
        self.choose = choose

    def make_screen(self) :
        image = PhotoImage(file=DISPLAY_ICON)
        self.choose.iconphoto(False,image)
        self.choose.resizable(False,False)
        self.choose.title("Covid-19 Choosing GUI(Graphical User Interface)")

        gui_width = 707
        gui_height = 267

        screen_width = self.choose.winfo_screenwidth()
        screen_height = self.choose.winfo_screenheight()

        center_x = screen_width//2 - gui_width//2
        center_y = screen_height//2 - gui_height//2

        self.choose.geometry("{}x{}+{}+{}".format(gui_width,gui_height,center_x,center_y))


    def choosing_option(self) :
        covid = ImageTk.PhotoImage(Image.open(VIRUS))
        covid_button = Button(self.choose, image = covid,text="Covid Registration",compound=LEFT,font=("Cosolas",20),width=700,justify='left',command=self.registration)
        covid_button.pack(anchor=E)

        introduction = ImageTk.PhotoImage(Image.open(MASK))
        introduction_button = Button(self.choose, image = introduction , text="Covid-19 Healthy Introduction",font=("Consolas",20),compound=LEFT,width=700,command=self.introduction)
        introduction_button.pack()

        self.choose.mainloop()

    def registration(self) :
        self.choose.destroy()

        import db_registration

        myRegistry = db_registration.RegistrationForm(Tk())
        myRegistry.registration_compare_screen()
        myRegistry.registration_import_img()
        myRegistry.registration_make_gui() 

    def introduction(self) :
        pass
    

if __name__ == '__main__':
    myObj = ChooseOption(Tk())
    myObj.make_screen()
    myObj.choosing_option()

