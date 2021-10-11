from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk

INTRO_FORM_LOGO = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/choosing_images/virus.png"
HAND_WASH = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/choosing_images/jabon-fi.png"
HAND_SANITIZER = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/choosing_images/alcohol-fi_wkEKr7k.png"
MASK = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/choosing_images/mask-fi.png"
DOCTOR = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/choosing_images/doctor-fi.png"
BACK = r"/home/thiloka/Documents/100 Python Projects/covid_regostration/choosing_images/icons8-go-back-48.png"

class RescueForm :
    def __init__(self,rescue) :
        self.rescue = rescue

    def rescue_screen_resolution(self) :

        intro_image = PhotoImage(file=INTRO_FORM_LOGO)
        self.rescue.iconphoto(False, intro_image)
        self.rescue.title("Introduction Menu")
        self.rescue.resizable(False,False)

        screen_width = 1564
        screen_height = 660

        window_width = self.rescue.winfo_screenwidth()
        window_height = self.rescue.winfo_screenheight()

        center_x = window_width//2 - screen_width//2
        center_y = window_height//2 - screen_height//2

        self.rescue.geometry("{}x{}+{}+{}".format(screen_width,screen_height,center_x,center_y))

    def reoprts(self) :
        self.report_1 = """Handwashing is an easy, cheap, and effective way to prevent the spread of germs and keep kids and adults healthy.\nWhen your family is healthy, you don’t\nhave to worry about missing school, work, or other activities."""
        self.report_2 = """Handwashing is one of the best ways to protect yourself and your family from getting sick.\nLearn when and how you should wash your hands to stay healthy."""
        self.report_3 = """Masks should be used as part of a comprehensive strategy of measures to suppress transmission and save lives; the use of a mask\nalone is not sufficient to provide an adequate level of protection against COVID-19.\n\nIf COVID-19 is spreading in your community, stay safe by taking some simple precautions, such as physical distancing, wearing a\nmask, keeping rooms well ventilated, avoiding crowds, cleaning your hands, and coughing into a bent elbow or tissue. Check local\nadvice where you live and work. Do it all!.\n\nMake wearing a mask a normal part of being around other people. The appropriate use, storage and cleaning or disposal of\nnmasks are essential to make them as effective as possible."""
        self.report_4 = """Immediately if you are infected with covid 19 Must see a doctor.That way you can heal covid 19"""

    def rescue_form_make_images(self) :
        self.sanitizer = ImageTk.PhotoImage(Image.open(HAND_SANITIZER))
        self.hand_washer = ImageTk.PhotoImage(Image.open(HAND_WASH))
        self.mask = ImageTk.PhotoImage(Image.open(MASK))
        self.doctor = ImageTk.PhotoImage(Image.open(DOCTOR))
        self.back = ImageTk.PhotoImage(Image.open(BACK))

    def frames(self) :
        self.hand_santizer_frame = Frame(self.rescue)
        self.hand_santizer_frame.grid(row=1, column=1, sticky=W)

        self.hand_wash_frame = Frame(self.rescue)
        self.hand_wash_frame.grid(row=2, column=1, sticky=W)

        self.mask_frame = Frame(self.rescue)
        self.mask_frame.grid(row=3, column=1, sticky=W)

        self.doctor_frame = Frame(self.rescue)
        self.doctor_frame.grid(row=4, column=1, sticky=W)

        self.back_button = Frame(self.rescue)
        self.back_button.grid(row=5,column=2,sticky=W)

    def make_rescue_form(self) :
        self.hand_santizer_report = Label(self.hand_santizer_frame, image=self.sanitizer, text=self.report_1, font=("Consolas", 12), compound=LEFT, justify="left")
        self.hand_santizer_report.grid(row=1, column=1)

        self.hand_wash_report = Label(self.hand_wash_frame, image=self.hand_washer, text=self.report_2, font=("Consolas", 12), compound=LEFT, justify="left")
        self.hand_wash_report.grid(row=2, column=1)

        self.mask_report = Label(self.mask_frame, image=self.mask, text=self.report_3, font=("Consolas", 12), compound=LEFT, justify="left")
        self.mask_report.grid(row=3, column=1, pady=2)

        self.doctor_report = Label(self.doctor_frame, image=self.doctor, text=self.report_4, font=("Consolas", 12), compound=LEFT, justify="left")
        self.doctor_report.grid(row=4, column=1, pady=2)

        self.go_back = Button(self.back_button, image=self.back , text="go back",font=("Source Sans Pro",12,'bold'),compound=LEFT,command=self.back_function,borderwidth=0)
        self.go_back.grid(row=5,column=1,sticky=E)

        self.rescue.mainloop()

    def back_function(self) :
        self.rescue.destroy()
        
        import choose as c

        myBack = c.ChooseForm(Tk())
        myBack.choose_screen_resolution()
        myBack.make_images()
        myBack.make_choosing_form()
        myBack.registration()
        myBack.introduction_form()
