from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image


def asgiriya_coosing_lab():
    new_test_request_label.config(state="active")

def hasalaka_coosing_lab():
    new_test2_request_label.config(state="active")

def methsuwa_coosing_lab():
    new_test3_request_label.config(state="active")

def family_coosing_lab():
    new_test4_request_label.config(state="active")

def test1():
    pass

def new_test1():
    root.destroy()
    import user_asking

def requast():
    pass

root = Tk()
resources = "D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
root.iconbitmap(resources + "\pythontutorial-1-150x150.ico")
root.title("Choose a Lab")

window_width = 1100
window_height = 680

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = (screen_width // 2 - window_width // 2)
center_y = (screen_height // 2 - window_height // 2)

root.geometry("{}x{}+{}+{}".format(window_width, window_height, center_x, center_y))

root.configure(bg="#FFFFFF")
# Asgiriya Lab
asgiriya_lab = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\isgiriya.png"))
asgiriya_lab_label = Button(image=asgiriya_lab,borderwidth=0,command=asgiriya_coosing_lab)
asgiriya_lab_label.grid(row=1)


test_request = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\itest_request.png"))
test_request_label = Button(image=test_request,borderwidth=0,command=test1)
test_request_label.config(state="disabled")
test_request_label.grid(row=2)

new_test_request = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\inew_test.png"))
new_test_request_label = Button(image=new_test_request,borderwidth=0,command=new_test1)
new_test_request_label.config(state="disabled")
new_test_request_label.grid(row=3)


request = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\ireport.png"))
request_label = Button(image=request,borderwidth=0,command=requast)
request_label.config(state="disabled")
request_label.grid(row=4)

# Hasalaka Lab
hasalaka_lab = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\iasalaka.png"))
hasalaka_lab_label = Button(image=hasalaka_lab,borderwidth=0,command=hasalaka_coosing_lab)
hasalaka_lab_label.grid(row=5)

test_request2 = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\itest_request.png"))
test_request2_label = Button(image=test_request,borderwidth=0,command=test1)
test_request2_label.config(state="disabled")
test_request2_label.grid(row=6)


new_test2_request = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\inew_test.png"))
new_test2_request_label = Button(image=new_test_request,borderwidth=0,command=new_test1)
new_test2_request_label.config(state="disabled")
new_test2_request_label.grid(row=7)


request2 = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\ireport.png"))
request2_label = Button(image=request,borderwidth=0,command=requast)
request2_label.config(state="disabled")
request2_label.grid(row=8)

# Methsuwa Lab
methsuwa_lab = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\iethsuwa.png"))
methsuwa_lab_label = Button(image=methsuwa_lab,borderwidth=0,command=methsuwa_coosing_lab)
methsuwa_lab_label.grid(row=9)


test_request3 = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\itest_request.png"))
test_request3_label = Button(image=test_request,borderwidth=0,command=test1)
test_request3_label.config(state="disabled")
test_request3_label.grid(row=10)


new_test3_request = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\inew_test.png"))
new_test3_request_label = Button(image=new_test_request,borderwidth=0,command=new_test1)
new_test3_request_label.config(state="disabled")
new_test3_request_label.grid(row=11)


request3 = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\ireport.png"))
request3_label = Button(image=request,borderwidth=0,command=requast)
request3_label.config(state="disabled")
request3_label.grid(row=12)

# Family Lab
family_lab = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\iamily.png"))
family_lab_label = Button(image=family_lab,borderwidth=0,command=family_coosing_lab)
family_lab_label.grid(row=13)


test_request4 = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\itest_request.png"))
test_request4_label = Button(image=test_request,borderwidth=0,command=test1)
test_request4_label.config(state="disabled")
test_request4_label.grid(row=14)


new_test4_request = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\inew_test.png"))
new_test4_request_label = Button(image=new_test_request,borderwidth=0,command=new_test1)
new_test4_request_label.config(state="disabled")
new_test4_request_label.grid(row=15)


request4 = ImageTk.PhotoImage(Image.open("D:\DDDDD\LABLK.HEROKUAPP.COM\LABLK_SOFTWARE_MAKING\PREVIOUS_lab_icons\ireport.png"))
request4_label = Button(image=request,borderwidth=0,command=requast)
request4_label.config(state="disabled")
request4_label.grid(row=16)


root.mainloop()
