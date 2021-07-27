import datetime
from tkinter import *
from PIL import ImageTk,Image
import random
from tkinter import ttk

root = Tk()
root.iconbitmap("D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources\ifavicon.ico")
root.title("New Test Request")
resources = "D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
root.iconbitmap(resources + "\pythontutorial-1-150x150.ico")


window_width = 1466
window_height = 380

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = (screen_width // 2 - window_width // 2)
center_y = (screen_height // 2 - window_height // 2)

root.geometry("{}x{}+{}+{}".format(window_width, window_height, center_x, center_y))

def one_clicked() :
    root.destroy()
    import choosing_tests

frame01 = Frame(root)
frame01.grid(row=0,column=0)

centre_code = Label(frame01, text="Centre code", font=("Berlin Sans FB Demi", 18))
centre_code.grid(row=1,sticky=W)
centre_code_combox = ttk.Combobox(frame01, values=[  "Asgiriya", "Hasalaka", "Emereld", "Methsuwa", "Family"], font=("Berlin Sans FB Demi", 18), width=20)
centre_code_combox.current(0)
centre_code_combox.grid(row=2)


mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=1,column=2,sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=2,column=2,sticky=W)


report_year = Label(frame01, text="Report Year", font=("Berlin Sans FB Demi", 18))
report_year.grid(row=1,column=3, sticky=W)
report_year_entry = ttk.Entry(frame01,  width=20,font=("Berlin Sans FB Demi", 18),justify="center")
x = datetime.datetime.now()
report_year_entry.insert(END,x.year)
report_year_entry.grid(row=2,column=3)

mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=1, column=4, sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=2, column=4, sticky=W)

seq_no = Label(frame01, text="Seq Number", font=("Berlin Sans FB Demi", 18))
seq_no.grid(row=1,column=5, sticky=W)
seq_no_entry = ttk.Entry(frame01, width=20,font=("Berlin Sans FB Demi", 18),justify="center")
get_random = random.randrange(0,101)
seq_no_entry.insert(END,get_random)
seq_no_entry.grid(row=2,column=5)

mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=1, column=6, sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=2, column=6, sticky=W)

requast_date = Label(frame01, text="Reuest Date", font=("Berlin Sans FB Demi", 18))
requast_date.grid(row=1, column=7, sticky=W)

year = []
for x in range(1998,2030):
    year.append(x)

year_listers = ttk.Combobox(frame01, values=year, font=("Berlin Sans FB Demi", 18), width=9,justify="center")
year_listers.current(0)
year_listers.grid(row=2,column=7)

month_listers = ttk.Combobox(frame01, values=["January", "February", "March", "April", "May", "June", "July","Auguest", "September", "october", "november", "December"], font=("Berlin Sans FB Demi", 18), width=9,justify="center")
month_listers.current(0)
month_listers.grid(row=2, column=8)


dates = []
for x in range(1,31):
    dates.append(x)

dates_listers = ttk.Combobox(frame01, values=dates, font=("Berlin Sans FB Demi", 18),width=9,justify="center")
dates_listers.current(0)
dates_listers.grid(row=2, column=9)


# PART 2

pacient_details = ttk.Label(frame01, text="Pacient Details", font=("Berlin Sans FB Demi", 18))
pacient_details.grid(row=3,sticky=W)

title2 = ttk.Label(frame01, text="Title",font=("Berlin Sans FB Demi", 18))
title2.grid(row=4, sticky=W)
title = ttk.Combobox(frame01, values=["Mr","Mrs","Miss"], font=("Berlin Sans FB Demi", 18), width=20, justify="center")
title.grid(row=5)

mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=4, column=2, sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=5, column=2, sticky=W)


first_name = ttk.Label(frame01, text="First Name", font=("Berlin Sans FB Demi", 18))
first_name.grid(row=4,column=3, sticky=W)
first_name_entry = ttk.Entry(frame01,width=20, font=("Berlin Sans FB Demi", 18))
first_name_entry.grid(row=5, column=3, sticky=W)

mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=4, column=4, sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=5, column=4, sticky=W)

last_name = ttk.Label(frame01, text="Last Name",font=("Berlin Sans FB Demi", 18))
last_name.grid(row=4, column=5, sticky=W)
last_name_entry = ttk.Entry(frame01, width=20, font=("Berlin Sans FB Demi", 18))
last_name_entry.grid(row=5, column=5, sticky=W)

mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=4, column=6, sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=5, column=6, sticky=W)

phone = ttk.Label(frame01, text="Phone Number", font=("Berlin Sans FB Demi", 18))
phone.grid(row=6, sticky=W)
phone_entry = ttk.Entry(frame01, width=21, font=("Berlin Sans FB Demi", 18))
phone_entry.grid(row=7, sticky=W)

mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=6, column=2, sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=7, column=2, sticky=W)

email = ttk.Label(frame01, text="Phone Number", font=("Berlin Sans FB Demi", 18))
email.grid(row=6,column=3, sticky=W)
email_entry = ttk.Entry(frame01, width=20, font=("Berlin Sans FB Demi", 18))
email_entry.grid(row=7,column=3, sticky=W)

mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=6, column=4, sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=7, column=4, sticky=W)

age = ttk.Label(frame01, text="Age(derive DOB)", font=("Berlin Sans FB Demi", 18))
age.grid(row=6, column=5, sticky=W)
age_entry = ttk.Entry(frame01, width=20, font=("Berlin Sans FB Demi", 18))
age_entry.grid(row=7, column=5, sticky=W)

mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=6, column=6, sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=7, column=6, sticky=W)

year = []
for x in range(1998, 2030):
    year.append(x)

year_listers = ttk.Combobox(frame01, values=year, font=("Berlin Sans FB Demi", 18), width=9, justify="center")
year_listers.current(0)
year_listers.grid(row=7, column=7,sticky=W)

month_listers = ttk.Combobox(frame01, values=["January", "February", "March", "April", "May", "June", "July", "Auguest", "September", "october", "november", "December"], font=("Berlin Sans FB Demi", 18), width=9, justify="center")
month_listers.current(0)
month_listers.grid(row=7, column=8)

dates = []
for x in range(1, 31):
    dates.append(x)

dates_listers = ttk.Combobox(frame01, values=dates, font=("Berlin Sans FB Demi", 18), width=9, justify="center")
dates_listers.current(0)
dates_listers.grid(row=7, column=9)

refferd_by = Label(frame01, text="Refferd By",font=("Berlin Sans FB Demi", 18))
refferd_by.grid(row=8, sticky=W)

doctor = Label(frame01, text="Doctor", font=("Berlin Sans FB Demi", 18))
doctor.grid(row=9, sticky=W)
doctor_name_entry = ttk.Entry(frame01, width=21, font=("Berlin Sans FB Demi", 18))
doctor_name_entry.grid(row=10, sticky=W)

mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=9, column=2, sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=10, column=2, sticky=W)

address = Label(frame01, text="Address", font=("Berlin Sans FB Demi", 18))
address.grid(row=9, column=3, sticky=W)
address_name_entry = ttk.Entry(frame01, width=21, font=("Berlin Sans FB Demi", 18))
address_name_entry.grid(row=10, column=3,  sticky=W)

mark = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark.grid(row=9, column=4, sticky=W)
mark2 = Label(frame01, text="|", font=("Berlin Sans FB Demi", 18))
mark2.grid(row=10, column=4, sticky=W)

submit = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK_SOFTWARE_MAKING\part_2.py\ICREATE_REQUEST_DETAILS.png"))
submit_button = Button(frame01,image=submit,borderwidth=0,command=one_clicked)
submit_button.grid(row=10,column=5,sticky=W)
root.mainloop()

