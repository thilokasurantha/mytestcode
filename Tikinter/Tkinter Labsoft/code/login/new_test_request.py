from tkinter import * 
from tkinter import ttk
from PIL import ImageTk,Image
import datetime
from tkinter import messagebox

CREATE_REQUEST_DETAILS = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/request_img/create.png"
BACK = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/request_img/back.png"

class NewTestRequest :
    def  __init__(self,new) :
        self.new = new

    def import_images(self) :
        self.create_request_img = ImageTk.PhotoImage(Image.open(CREATE_REQUEST_DETAILS))
        self.back_img = ImageTk.PhotoImage(Image.open(BACK))

    def frmaes(self) :
        self.codes = Frame(self.new)
        self.codes.grid(row=1)
        self.entries = Frame(self.new)
        self.entries.grid(row=2)

        self.pacient_frame = Frame(self.new)
        self.pacient_frame.grid(row=3,sticky=W)

        self.details_lbl = Frame(self.new)
        self.details_lbl.grid(row=4,sticky=W)
        self.detail_entry = Frame(self.new)
        self.detail_entry.grid(row=5,sticky=W)

        self.choose = Frame(self.new)
        self.choose.grid(row=6,sticky=W)

    def compare_screen(self) :
        self.new.title("New Test Request")

    def variables(self) :
        self.import_date = datetime.datetime.now()
        self.year = self.import_date.year
        self.month = self.import_date.month
        self.day = self.import_date.day
        self.maths = 1364

    def new_test_request_form(self) :
        self.center_code = Label(self.codes, text="Centre code  ", font=("Source Sans Pro",12,'bold'),justify="center")
        self.center_code.grid(row=1,column=1)
        self.center_code_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.center_code_entry.grid(row=2,column=1)

        self.report_year = Label(self.codes, text="Report year  ", font=("Source Sans Pro",12,'bold'))
        self.report_year.grid(row=1,column=2)
        self.report_year_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.report_year_entry.insert(0,f"{self.year} / {self.month} / {self.day}")
        self.report_year_entry.grid(row=2,column=2)

        self.seq_no = Label(self.codes, text="Seq no", font=("Source Sans Pro",12,'bold'))
        self.seq_no.grid(row=1,column=3)
        self.seq_no_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.seq_no_entry.grid(row=2,column=3)

        self.seq_no = Label(self.codes, text="Seq no", font=("Source Sans Pro",12,'bold'))
        self.seq_no.grid(row=1,column=3)
        self.seq_no_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.seq_no_entry.grid(row=2,column=3)

        self.year = Label(self.codes, text="Request year", font=("Source Sans Pro",12,'bold'))
        self.year.grid(row=1,column=4)
        self.year_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.year_entry.grid(row=2,column=4)

        self.month = Label(self.codes, text="Request month", font=("Source Sans Pro",12,'bold'))
        self.month.grid(row=1,column=5)
        self.month_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.month_entry.grid(row=2,column=5)

        self.dates = Label(self.codes, text="Request dates", font=("Source Sans Pro",12,'bold'))
        self.dates.grid(row=1,column=6)
        self.dates_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.dates_entry.grid(row=2,column=6)

    def pacient_details(self) :

        self.title = Label(self.codes, text="Title", font=("Source Sans Pro",12,'bold'))
        self.title.grid(row=4,column=1)
        self.title_entry = ttk.Combobox(self.codes,values=["Mr.","Mrs.","Miss.","Ven.","Baby.",""], font=("Source Sans Pro",12,'bold'),justify="center")
        self.title_entry.grid(row=5,column=1)

        self.f_name = Label(self.codes, text="First Name", font=("Source Sans Pro",12,'bold'))
        self.f_name.grid(row=4,column=2)
        self.f_name_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.f_name_entry.grid(row=5,column=2)

        self.l_name = Label(self.codes, text="Last Name", font=("Source Sans Pro",12,'bold'))
        self.l_name.grid(row=4,column=3)
        self.l_name_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.l_name_entry.grid(row=5,column=3)

        self.phone = Label(self.codes, text="Phone Number", font=("Source Sans Pro",12,'bold'))
        self.phone.grid(row=4,column=4)
        self.phone_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.phone_entry.grid(row=5,column=4)

        self.email = Label(self.codes, text="Email", font=("Source Sans Pro",12,'bold'))
        self.email.grid(row=4,column=5)
        self.email_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.email_entry.grid(row=5,column=5)

        self.age = Label(self.codes, text="Age", font=("Source Sans Pro",12,'bold'))
        self.age.grid(row=4,column=6)
        self.age_entry = ttk.Entry(self.codes, font=("Source Sans Pro",12,'bold'),justify="center")
        self.age_entry.grid(row=5,column=6)

        self.design = "-"*177
        self.lable = Label(self.choose, text=f"Choose Text {self.design}",font=("Berlin Sans FB Demi", 12,'bold'))
        self.lable.grid(row=6,sticky=W)

    def choose_test(self) :

        bg = Checkbutton(self.new, text="BG (BLOOD GROUPING AND Rh)", font=("Berlin Sans FB Demi", 13))
        bg.grid(row=7, sticky=W)
        
        egfr = Checkbutton(self.new, text="EGFR (ESTIMATED GLOMARUL FILTRATION (eGFR))", font=("Berlin Sans FB Demi", 13))
        egfr.grid(row=8, sticky=W)
        
        fbs = Checkbutton(self.new, text="FBS (FASTING PLASMA GLUCOSE)",font=("Berlin Sans FB Demi", 13))
        fbs.grid(row=9, sticky=W)
        
        hb = Checkbutton(self.new, text="HB (HEAMOGLOBIN LEVEL)",font=("Berlin Sans FB Demi", 13))
        hb.grid(row=10, sticky=W)
        
        hbaag = Checkbutton(self.new, text="HBaAG (HEPETITIES B SURFACE ANTIGEN (HBSAG)", font=("Berlin Sans FB Demi", 13))
        hbaag.grid(row=11, sticky=W)
        
        lp = Checkbutton(self.new, text="LP (LIPID PROFILE)",font=("Berlin Sans FB Demi", 13))
        lp.grid(row=12, sticky=W)
        
        ogtt1 = Checkbutton(self.new, text="OGTT1 (ORAL GLUCOSE TOLLERANCE TEST (OGTT))", font=("Berlin Sans FB Demi", 13))
        ogtt1.grid(row=13, sticky=W)
        
        pt_inr = Checkbutton(self.new, text="PT_INR (PROTHOMBIN TIME & INR (PT_INR))", font=("Berlin Sans FB Demi", 13))
        pt_inr.grid(row=14, sticky=W)
        
        rft = Checkbutton(self.new, text="RFT (RENAL FUNCTION TEST)",font=("Berlin Sans FB Demi", 13))
        rft.grid(row=15, sticky=W)
        
        scal = Checkbutton(self.new, text="SCAL (SERUM CALCIUM (S-CAL))",font=("Berlin Sans FB Demi", 13))
        scal.grid(row=16, sticky=W)
        
        ual = Checkbutton(self.new, text="UAL (URINE ALBUMIN)",font=("Berlin Sans FB Demi", 13))
        ual.grid(row=17, sticky=W)
        
        uric_acid = Checkbutton(self.new, text="URIC ACID (SERUM URIC ACID)", font=("Berlin Sans FB Demi", 13))
        uric_acid.grid(row=23, sticky=W)
        # PART 5
        
        asot = Checkbutton(self.new, text="ASOT (ASOT)",font=("Berlin Sans FB Demi", 13))
        asot.grid(row=18, sticky=W)
        
        cpk = Checkbutton(self.new, text="CPK (CREATININE PHOSPHOKINASE (CPK)", font=("Berlin Sans FB Demi", 13))
        cpk.grid(row=19, sticky=W)
        
        esr = Checkbutton(self.new, text="ESR (ERYTHROCYTES SEDIMENTATION RATE) ", font=("Berlin Sans FB Demi", 13))
        esr.grid(row=20, sticky=W)
        
        fbs_ppbs = Checkbutton(self.new, text="FBS_PPBS (FASTING PLASMA GLUCOSE (FBS) and POST PREANDIAL PLASMA GLUCOSE (PPBS))", font=("Berlin Sans FB Demi", 13))
        fbs_ppbs.grid(row=21, sticky=W)
        
        hsabp = Checkbutton(self.new, text="HB&BP (HB % & BLOOD PICTURE)",font=("Berlin Sans FB Demi", 13))
        hsabp.grid(row=22,sticky=W)
        
        hepe = Checkbutton(self.new, text="HEP.algMab (HEPETITIES 'A' lg M ANTIBODY)", font=("Berlin Sans FB Demi", 13))
        hepe.grid(row=23,  sticky=W)
        
        lpt = Checkbutton(self.new, text="LPT (LIVET PROFILE TEST)",font=("Berlin Sans FB Demi", 13))
        lpt.grid(row=24, sticky=W)
        
        otpt = Checkbutton(self.new, text="OTPT (SGOT/SGPT)",font=("Berlin Sans FB Demi", 13))
        otpt.grid(row=25, sticky=W)
        
        rbs = Checkbutton(self.new, text="RBS (RANDOM BLOOD GLUCOSE (RBS))", font=("Berlin Sans FB Demi", 13))
        rbs.grid(row=26, sticky=W)
        
        sat = Checkbutton(self.new, text="SAT (WIDAL STANDARD AGGLUTINATION (S.A.T) TEST)", font=("Berlin Sans FB Demi", 13))
        sat.grid(row=27, sticky=W)
        
        se = Checkbutton(self.new, text="SE (SERIUM ELECTROLYTES (SE))",font=("Berlin Sans FB Demi", 13))
        se.grid(row=28,  sticky=W)
        
        ufr = Checkbutton(self.new, text="UFR (URINE FULL REPORT)",font=("Berlin Sans FB Demi", 13))
        ufr.grid(row=29, sticky=W)
        
        vdrl = Checkbutton(self.new, text="VDRL (VDRL TEST)",font=("Berlin Sans FB Demi", 13))
        vdrl.grid(row=30,sticky=W)
        
        vdrl = Checkbutton(self.new, text="VDRL (VDRL TEST)",font=("Berlin Sans FB Demi", 13))
        vdrl.grid(row=31,  sticky=W)
        self.new.mainloop()

if __name__ == '__main__':
    myObj = NewTestRequest(Tk())
    myObj.import_images()
    myObj.frmaes()
    myObj.compare_screen()
    myObj.variables()
    myObj.new_test_request_form()
    myObj.pacient_details()
    myObj.choose_test()
    myObj.create_request_details()
