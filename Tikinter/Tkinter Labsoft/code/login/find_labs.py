from os import name
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import information as info
import new_test_request as n_text
import test_request as r_text
import report_formats as rp_form

ASGIRIYA = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/choose_img/asgiriya.png"
EMARALD  = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/choose_img/emarald.png"
FAMILY   = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/choose_img/family.png"
HASALAKA = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/choose_img/hasalaka.png"
METHSUWA = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/choose_img/methsuwa.png"


NEW      = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/choose_img/new_test_request.png"
REPORT   = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/choose_img/report.png"
TEST     = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/choose_img/test_request.png" 

class FindLabForm :
    def __init__(self, find) :
        self.find = find
    
    def compare_screen(self) :
        self.find.title("Find Labs")
        
    def import_images(self) :
        self.asgiriya = ImageTk.PhotoImage(Image.open(ASGIRIYA))
        self.emarald  = ImageTk.PhotoImage(Image.open(EMARALD))
        self.family   = ImageTk.PhotoImage(Image.open(FAMILY))
        self.hasalaka = ImageTk.PhotoImage(Image.open(HASALAKA))
        self.methsuwa = ImageTk.PhotoImage(Image.open(METHSUWA))

        self.test     = ImageTk.PhotoImage(Image.open(TEST))
        self.new      = ImageTk.PhotoImage(Image.open(NEW))
        self.report   = ImageTk.PhotoImage(Image.open(REPORT))

    def request_form(self) :
        # Asgiriya Lab
        self.asgiriya_lab_label = Button(self.find,image=self.asgiriya,borderwidth=0,command=lambda:self.details("asgiriya"))
        self.asgiriya_lab_label.grid(row=1)

        self.asgiriya_test_request_label = Button(self.find,image=self.test,borderwidth=0,command=self.test_request)
        self.asgiriya_test_request_label.grid(row=2)
        
        self.asgiriya_new_test_request_label = Button(self.find,image=self.new,borderwidth=0,command=self.new_test_request)
        self.asgiriya_new_test_request_label.grid(row=3)

        self.asgiriya_request_label = Button(self.find,image=self.report,borderwidth=0,command=self.test_check)
        self.asgiriya_request_label.grid(row=4)
        # Hasalaka Lab

        self.hasalaka_lab_label = Button(self.find,image=self.hasalaka,borderwidth=0,command=lambda:self.details("hasalaka"))
        self.hasalaka_lab_label.grid(row=5)

        self.hasalaka_test_request_label = Button(self.find,image=self.test,borderwidth=0,command=self.test_request)
        self.hasalaka_test_request_label.grid(row=6)

        self.hasalaka_new_test_request_label = Button(self.find,image=self.new,borderwidth=0,command=self.new_test_request)
        self.hasalaka_new_test_request_label.grid(row=7)

        self.hasalaka_request_label = Button(self.find,image=self.report,borderwidth=0,command=self.test_check)
        self.hasalaka_request_label.grid(row=8)

        # Methsuwa Lab
        self.methsuwa_lab_label = Button(self.find,image=self.methsuwa,borderwidth=0,command=lambda:self.details("methsuwa"))
        self.methsuwa_lab_label.grid(row=9)

        self.methsuwa_test_request_label = Button(self.find,image=self.test,borderwidth=0,command=self.test_request)
        self.methsuwa_test_request_label.grid(row=10)

        self.methsuwa_new_test_request_label = Button(self.find,image=self.new,borderwidth=0,command=self.new_test_request)
        self.methsuwa_new_test_request_label.grid(row=11)

        self.methsuwa_request_label = Button(self.find,image=self.report,borderwidth=0,command=self.test_check)
        self.methsuwa_request_label.grid(row=12)

        # Family Lab
        self.family_lab_label = Button(self.find,image=self.family,borderwidth=0,command=lambda:self.details("family"))
        self.family_lab_label.grid(row=13)
   
        self.family_test_request_label = Button(self.find,image=self.test,borderwidth=0,command=self.test_request)
        self.family_test_request_label.grid(row=14)

        self.family_new_test_request_label = Button(self.find,image=self.new,borderwidth=0,command=self.new_test_request)
        self.family_new_test_request_label.grid(row=15)

        self.family_request_label = Button(self.find,image=self.report,borderwidth=0,command=self.test_check)
        self.family_request_label.grid(row=16)

        self.find.mainloop()

    def new_test_request(self) :
        pass

    def test_request(self) :
        pass

    def test_check(self) :
        pass

    def details(self,name) :
        self.save_names = name

        self.find.destroy()

        myInformation = info.CheckInformationLab(Tk(),self.save_names)
        myInformation.compare_screen()
        myInformation.import_images()
        myInformation.information_form()