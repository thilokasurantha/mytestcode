from tkinter import *
from PIL import ImageTk,Image
import find_labs as find

TEST_REQUEST = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/request_img/test_request.png"
NEW_TEXT_REQUEST = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/request_img/mew_test_request.png"
REPORT_FORMATS = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/request_img/report_formats.png"
BACK = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/python projects/request_img/back.png"

class CheckInformationLab :
	def __init__(self, info,lab) :
		self.info = info
		self.lab = lab

	def compare_screen(self) :
		self.info.config(bg="white")
		self.info.title("Lab Information")
		self.info.resizable(False, False)

	def import_images(self) :
		self.test_request = ImageTk.PhotoImage(Image.open(TEST_REQUEST))
		self.new_test_request = ImageTk.PhotoImage(Image.open(NEW_TEXT_REQUEST))
		self.report_formats = ImageTk.PhotoImage(Image.open(REPORT_FORMATS))
		self.return_programme = ImageTk.PhotoImage(Image.open(BACK))

	def information_form(self) :

		frame = Frame(self.info)
		frame.grid(row=1)
		lable_frame = LabelFrame(self.info,fg="black",bg="white")
		lable_frame.grid(row=2,column=0,sticky=W)	
		
		calculation = int(len(self.lab))//2
		editing = (self.lab[0]+self.lab[calculation]).upper()

		self.test_button = Button(frame, image=self.test_request,bg="white")
		self.test_button.grid(row=1,column=0,sticky=W)
		self.new_test_button = Button(frame, image=self.new_test_request, bg="white",borderwidth=0)
		self.new_test_button.grid(row=1,column=1,sticky=W)
		self.reported_formats = Button(frame, image=self.report_formats, bg="white",borderwidth=0)
		self.reported_formats.grid(row=1,column=2,sticky=W)
		self.back_button = Button(self.info, image=self.return_programme,bg="white",borderwidth=0,command=self.back_function)
		self.back_button.grid(row=5,column=0,sticky=W)

		self.name = Label(lable_frame, text=f"Center Name        : {self.lab}", font=("Source Sans Pro",12,'bold'),bg="white")
		self.name.grid(row=2,column=0,sticky=W)
		self.codes =Label(lable_frame, text=f"Center Code         : {editing}", font=("Source Sans Pro",12,'bold'),bg="white")
		self.codes.grid(row=3,column=0,sticky=W)
		self.address = Label(lable_frame,   text=f"Address                : {self.lab},kandy", font=("Source Sans Pro",12,'bold'),bg="white")
		self.address.grid(row=4,column=0,sticky=W)

		self.info.mainloop()

	def back_function(self):
    		
		self.info.destroy()
    	
		back = find.FindLabForm(Tk())
		back.compare_screen()
		back.import_images()
		back.request_form()
		back.details()
		back.new_test_request()
		back.test_request()
		back.test_check()