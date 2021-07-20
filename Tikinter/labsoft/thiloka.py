from tkinter import *
root = Tk()
root.title("Enter the Reports")
root.iconbitmap("D:\Programing\GIT\mytestcode\ifavicon.ico")
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
uric_acid.grid(row=23, sticky=W)
# PART 5

asot = Checkbutton(root, text="ASOT (ASOT)",font=("Berlin Sans FB Demi", 13))
asot.grid(row=25, sticky=W)

cpk = Checkbutton(root, text="CPK (CREATININE PHOSPHOKINASE (CPK)", font=("Berlin Sans FB Demi", 13))
cpk.grid(row=26, sticky=W)

esr = Checkbutton(root, text="ESR (ERYTHROCYTES SEDIMENTATION RATE) ", font=("Berlin Sans FB Demi", 13))
esr.grid(row=27, sticky=W)

fbs_ppbs = Checkbutton(root, text="FBS_PPBS (FASTING PLASMA GLUCOSE (FBS) and POST PREANDIAL PLASMA GLUCOSE (PPBS))", font=("Berlin Sans FB Demi", 13))
fbs_ppbs.grid(row=28, sticky=W)

hsabp = Checkbutton(root, text="HB&BP (HB % & BLOOD PICTURE)",font=("Berlin Sans FB Demi", 13))
hsabp.grid(row=11, column=1,sticky=W)

hepe = Checkbutton(root, text="HEP.algMab (HEPETITIES 'A' lg M ANTIBODY)", font=("Berlin Sans FB Demi", 13))
hepe.grid(row=12, column=1, sticky=W)

lpt = Checkbutton(root, text="LPT (LIVET PROFILE TEST)",font=("Berlin Sans FB Demi", 13))
lpt.grid(row=13, column=1,sticky=W)

otpt = Checkbutton(root, text="OTPT (SGOT/SGPT)",font=("Berlin Sans FB Demi", 13))
otpt.grid(row=14, column=1,sticky=W)

rbs = Checkbutton(root, text="RBS (RANDOM BLOOD GLUCOSE (RBS))", font=("Berlin Sans FB Demi", 13))
rbs.grid(row=15, column=1,sticky=W)

sat = Checkbutton(root, text="SAT (WIDAL STANDARD AGGLUTINATION (S.A.T) TEST)", font=("Berlin Sans FB Demi", 13))
sat.grid(row=16, column=1,sticky=W)

se = Checkbutton(root, text="SE (SERIUM ELECTROLYTES (SE))",font=("Berlin Sans FB Demi", 13))
se.grid(row=17, column=1, sticky=W)

ufr = Checkbutton(root, text="UFR (URINE FULL REPORT)",font=("Berlin Sans FB Demi", 13))
ufr.grid(row=18, column=1,sticky=W)

vdrl = Checkbutton(root, text="VDRL (VDRL TEST)",font=("Berlin Sans FB Demi", 13))
vdrl.grid(row=19, column=1,sticky=W)

root.mainloop()
