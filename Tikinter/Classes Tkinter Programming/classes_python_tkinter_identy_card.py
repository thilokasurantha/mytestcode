# Importing Items Need t othis Programme
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
# Create a 'class'
class CreateTkinterIdentyCard :
    # Making a Variable
    def __init__(self,root) :
        self.root = root
    # Screen Comparing
    def compare_screen(self) :
        self.path_of_icons = r"D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
        self.root.resizable(False,False)
        self.root.title("Identy Card Entering Python Programme")
        self.root.iconbitmap(self.path_of_icons+"\Alecive-Flatwoken-Apps-Computer-Login.ico")
        self.root.config(bg="#ffffff")
        self.gui_width = 675
        self.gui_height = 200

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()


        self.center_x = (self.screen_width//2 - self.gui_width//2)
        self.center_y = (self.screen_height//2 - self.gui_height//2)


        self.root.geometry("{}x{}+{}+{}".format(self.gui_width,self.gui_height,self.center_x,self.center_y))

    # Making Graphical User Interface
    def making_gui(self) :
        self.resource = r"D:\\DDDDD\\LABLK_SOFTWARE_MAKING\\part_2.py"
        self.identy_label = Label(self.root, text="Enter your Identy Card Number :", font=("Trebuchet MS", 14, 'bold'), bg="#ffffff")
        self.identy_label.grid(row=1,column=1)
        self.identy_entry = ttk.Entry(self.root, font=("Trebuchet MS",14,'bold'))
        self.identy_entry.grid(row=1,column=2)
        self.submit = Button(self.root,text="login",font=("Trebuchet MS", 14, 'bold'),command = self.get_month_and_date,borderwidth=0,width=12)
        self.submit.grid(row=1,column=3)
        self.root.mainloop() 

    # Get Month And Date
    def get_month_and_date(self) :
        if (len(self.identy_entry.get()) < 10) :
            self.errormessage = messagebox.showerror("Entering Error","You identy card must be length of 10 digits. Please try again")
            if (self.errormessage == "ok") :
                self.identy_entry.delete(0,END)
        elif (len(self.identy_entry.get()) == 10) :
            self.entering_autocomplete_programme()

    # Entering And autocompleting programme
    def entering_autocomplete_programme (self):
        self.getting_identy = self.identy_entry.get()
        self.year = self.getting_identy[0:2]
        self.month_dates = int(self.getting_identy[2:5])

        self.output_year = Label(self.root, text="Your Birth year is :",font=("Trebuchet MS", 14, 'bold'),bg="#ffffff")
        self.output_year.grid(sticky=W , row=2,column=1)
        self.printing_output = Label(self.root, text="19"+self.year, font=("Trebuchet MS", 14, 'bold'),bg="#ffffff")
        self.printing_output.grid(sticky=W, row=2,column=2)

        if (int(self.month_dates) < 500) :
            self.male = Label(self.root, text="Your Gender :",font=("Trebuchet MS", 14, 'bold'), bg="#ffffff")
            self.male.grid(sticky=W, row=3, column=1)
            self.male_show = Label(self.root, text="Male", font=("Trebuchet MS", 14, 'bold'), bg="#ffffff")
            self.male_show.grid(sticky=W, row=3, column=2)
            self.genarationg_identy()
        else :
            self.male = Label(self.root, text="Your Gender :", font=("Trebuchet MS", 14, 'bold'), bg="#ffffff")
            self.male.grid(sticky=W, row=4, column=1)
            self.male_show = Label(self.root, text="Female", font=( "Trebuchet MS", 14, 'bold'), bg="#ffffff")
            self.male.grid(sticky=W, row=4, column=2)

    def genarationg_identy(self) :
            self.months = [31,28,31,30,31,30,31,31,30,31,30,31]
            self.month = 0
            self.dates = 1
            while (self.month_dates > self.months[self.month] + self.dates) :
                self.month += 1
                self.dates += self.months[self.month]

            self.calculation = self.month + 1
            self.mines = self.month_dates - self.dates

            self.month = Label(self.root, text="Your Month :", font=("Trebuchet MS", 14, 'bold'), bg="#ffffff")
            self.month.grid(sticky=W, row=5, column=1)
            self.month_show = Label(self.root, text=self.calculation, font=("Trebuchet MS", 14, 'bold'), bg="#ffffff")
            self.month_show.grid(sticky=W, row=5, column=2)
            self.date = Label(self.root, text="Your Date :", font=( "Trebuchet MS", 14, 'bold'), bg="#ffffff")
            self.date.grid(sticky=W, row=6, column=1)
            self.date_show = Label(self.root, text=self.mines, font=( "Trebuchet MS", 14, 'bold'), bg="#ffffff")
            self.date_show.grid(sticky=W, row=6, column=2)

            self.close  = Button(self.root , text="close",font=("Trebuchet MS", 14, 'bold'),command = self.close_function,borderwidth=0,width=12)
            self.close.grid(sticky=W,row=7,column=1)

    def close_function(self) :
        exit()


if __name__ == '__main__':
    myObj = CreateTkinterIdentyCard(Tk()) 
    myObj.compare_screen()
    myObj.making_gui()

