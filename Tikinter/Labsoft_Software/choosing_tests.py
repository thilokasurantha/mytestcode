from tkinter import *
from PIL import ImageTk,Image
def one_clicked() :
    root.destroy()
    import saving_test
root = Tk()
resources = "D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
root.iconbitmap(resources + "\pythontutorial-1-150x150.ico")
root.title("Enter the Reports")

window_width = 1227
window_height = 630

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = (screen_width // 2 - window_width // 2)
center_y = (screen_height // 2 - window_height // 2)

root.geometry("{}x{}+{}+{}".format(window_width, window_height, center_x, center_y))

root.iconbitmap("D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources\ifavicon.ico")
ap = Checkbutton(root, text="AP (SERUM ALKALINE PHOSPHATSE)",font=("Berlin Sans FB Demi", 13))
ap.grid(row=11, sticky=W)

bg = Checkbutton(root, text="BG (BLOOD GROUPING AND Rh)", font=("Berlin Sans FB Demi", 13))
bg.grid(row=12, sticky=W)

egfr = Checkbutton(root, text="EGFR (ESTIMATED GLOMARUL FILTRATION (eGFR))", font=("Berlin Sans FB Demi", 13))
egfr.grid(row=13, sticky=W)

fbs = Checkbutton(root, text="FBS (FASTING PLASMA GLUCOSE)",font=("Berlin Sans FB Demi", 13))
fbs.grid(row=14, sticky=W)

hb = Checkbutton(root, text="HB (HEAMOGLOBIN LEVEL)",font=("Berlin Sans FB Demi", 13))
hb.grid(row=15, sticky=W)

hbaag = Checkbutton(root, text="HBaAG (HEPETITIES B SURFACE ANTIGEN (HBSAG)", font=("Berlin Sans FB Demi", 13))
hbaag.grid(row=16, sticky=W)

lp = Checkbutton(root, text="LP (LIPID PROFILE)",font=("Berlin Sans FB Demi", 13))
lp.grid(row=17, sticky=W)

ogtt1 = Checkbutton(root, text="OGTT1 (ORAL GLUCOSE TOLLERANCE TEST (OGTT))", font=("Berlin Sans FB Demi", 13))
ogtt1.grid(row=18, sticky=W)

pt_inr = Checkbutton(root, text="PT_INR (PROTHOMBIN TIME & INR (PT_INR))", font=("Berlin Sans FB Demi", 13))
pt_inr.grid(row=19, sticky=W)

rft = Checkbutton(root, text="RFT (RENAL FUNCTION TEST)",font=("Berlin Sans FB Demi", 13))
rft.grid(row=20, sticky=W)

scal = Checkbutton(root, text="SCAL (SERUM CALCIUM (S-CAL))",font=("Berlin Sans FB Demi", 13))
scal.grid(row=21, sticky=W)

ual = Checkbutton(root, text="UAL (URINE ALBUMIN)",font=("Berlin Sans FB Demi", 13))
ual.grid(row=22, sticky=W)

uric_acid = Checkbutton(root, text="URIC ACID (SERUM URIC ACID)", font=("Berlin Sans FB Demi", 13))
uric_acid.grid(row=21,column=1 ,sticky=W)
# PART 5

asot = Checkbutton(root, text="ASOT (ASOT)",font=("Berlin Sans FB Demi", 13))
asot.grid(row=22,column=1 , sticky=W)

cpk = Checkbutton(root, text="CPK (CREATININE PHOSPHOKINASE (CPK)", font=("Berlin Sans FB Demi", 13))
cpk.grid(row=23,column=1, sticky=W)

esr = Checkbutton(root, text="ESR (ERYTHROCYTES SEDIMENTATION RATE) ", font=("Berlin Sans FB Demi", 13))
esr.grid(row=23, sticky=W)

fbs_ppbs = Checkbutton(root, text="FBS_PPBS (FASTING PLASMA GLUCOSE (FBS) and POST PREANDIAL PLASMA GLUCOSE (PPBS))", font=("Berlin Sans FB Demi", 13))
fbs_ppbs.grid(row=24,column=1 , sticky=W)

hsabp = Checkbutton(root, text="HB&BP (HB % & BLOOD PICTURE)",font=("Berlin Sans FB Demi", 13))
hsabp.grid(row=24, column=0,sticky=W)

hepe = Checkbutton(root, text="HEP.algMab (HEPETITIES 'A' lg M ANTIBODY)", font=("Berlin Sans FB Demi", 13))
hepe.grid(row=25, column=0, sticky=W)

lpt = Checkbutton(root, text="LPT (LIVET PROFILE TEST)",font=("Berlin Sans FB Demi", 13))
lpt.grid(row=25, column=1,sticky=W)

otpt = Checkbutton(root, text="OTPT (SGOT/SGPT)",font=("Berlin Sans FB Demi", 13))
otpt.grid(row=27, column=0,sticky=W)

rbs = Checkbutton(root, text="RBS (RANDOM BLOOD GLUCOSE (RBS))", font=("Berlin Sans FB Demi", 13))
rbs.grid(row=27, column=1,sticky=W)

sat = Checkbutton(root, text="SAT (WIDAL STANDARD AGGLUTINATION (S.A.T) TEST)", font=("Berlin Sans FB Demi", 13))
sat.grid(row=29, column=0,sticky=W)

se = Checkbutton(root, text="SE (SERIUM ELECTROLYTES (SE))",font=("Berlin Sans FB Demi", 13))
se.grid(row=29, column=1, sticky=W)

ufr = Checkbutton(root, text="UFR (URINE FULL REPORT)",font=("Berlin Sans FB Demi", 13))
ufr.grid(row=31, column=0,sticky=W)

vdrl = Checkbutton(root, text="VDRL (VDRL TEST)",font=("Berlin Sans FB Demi", 13))
vdrl.grid(row=31, column=1,sticky=W)

bcf = Checkbutton(root, text="BCF (BIOCHEMISTRY FULL REPORT)",font=("Berlin Sans FB Demi", 13))
bcf.grid(row=33, column=0,sticky=W)

dengue = Checkbutton(root, text="DENGUE (DENGUE ANTIGEN (NSI))",font=("Berlin Sans FB Demi", 13))
dengue.grid(row=33, column=1,sticky=W)

ggt = Checkbutton(root, text="GGT (SERUM GAMMA GLUTAMYL TRANSERANCE (GGT))",font=("Berlin Sans FB Demi", 13))
ggt.grid(row=11, column=1,sticky=W)
#
hba1c = Checkbutton(root, text="HBA1C (HBA1C)",font=("Berlin Sans FB Demi", 13))
hba1c.grid(row=12, column=1,sticky=W)
#
HIV = Checkbutton(root, text="HIV (HIV I & II)",font=("Berlin Sans FB Demi", 13))
HIV.grid(row=13, column=1,sticky=W)
#
ogct = Checkbutton(root, text="OGCT (ORAL GLUCOSE CHALLENGE TEST (OGCT) - ( AFTER 50g OF GLUCOSE ))",font=("Berlin Sans FB Demi", 13))
ogct.grid(row=14, column=1,sticky=W)
#
ogct = Checkbutton(root, text="OGCT (ORAL GLUCOSE CHALLENGE TEST (OGCT) - ( AFTER 50g OF GLUCOSE ))",font=("Berlin Sans FB Demi", 13))
ogct.grid(row=15, column=1,sticky=W)
#
ppbs = Checkbutton(root, text="PPBS (POST PRANDIAL PLASMA GLUCOSE (PPBS))",font=("Berlin Sans FB Demi", 13))
ppbs.grid(row=16, column=1,sticky=W)
#
rf = Checkbutton(root, text="RF (RHEUMATOID FACTOR./ C.R.P. / E.S.R.)",font=("Berlin Sans FB Demi", 13))
rf.grid(row=17, column=1,sticky=W)

#
sc = Checkbutton(root, text="SC (SERUM CREATININE)",font=("Berlin Sans FB Demi", 13))
sc.grid(row=18, column=1,sticky=W)

#
trop = Checkbutton(root, text="TROP.I (SERUM CARDIAC TROPONIN I (CTNI))",font=("Berlin Sans FB Demi", 13))
trop.grid(row=19, column=1,sticky=W)
#
uma = Checkbutton(root, text="UMA(URINE MICROALBUMIN CREATININE RATIO)",font=("Berlin Sans FB Demi", 13))
uma.grid(row=20, column=1,sticky=W)

submit = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK_SOFTWARE_MAKING\part_2.py\ICREATE_REQUEST_DETAILS.png"))
submit_button = Button(root,image=submit,borderwidth=0,command=one_clicked)
submit_button.grid(row=34,column=0,sticky=W)
root.mainloop()
