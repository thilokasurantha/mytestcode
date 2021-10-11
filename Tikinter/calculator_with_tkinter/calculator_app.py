from tkinter import *
class MakeCalculator :
    def __init__(self,root) :
        self.root = root
    def make_screen(self) :
        self.root.title("Calculator")
        self.resources = "D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
        self.root.iconbitmap(self.resources+"\pythontutorial-1-150x150.ico")

        self.root.resizable(False, False)
        self.application_window_width = 426
        self.application_window_height = 426

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.center_x = (self.screen_width//2 - self.application_window_width//2)
        self.center_y = (self.screen_height//2 -self.application_window_height//2)

        self.root.geometry("{}x{}+{}+{}".format(self.application_window_width,self.application_window_height, self.center_x, self.center_y))

    def make_calculator_app(self) :
        self.frame1 = Frame(self.root)
        self.frame1.pack()
        self.frame2 = Frame(self.root)
        self.frame2.pack()
        self.frame3 = Frame(self.root)
        self.frame3.pack()
        self.frame4 = Frame(self.root)
        self.frame4.pack()

        self.show_entry = Entry(self.frame1, width=43, font=("Segoe UI Black", 0))
        self.show_entry.pack()

        self.button_7 = Button(self.frame1, text="7", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: self.numbers(7))
        self.button_7.pack(side=LEFT)
        self.button_8 = Button(self.frame1, text="8", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: self.numbers(8))
        self.button_8.pack(side=LEFT)
        self.button_9 = Button(self.frame1, text="9", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: self.numbers(9))
        self.button_9.pack(side=LEFT)

        self.button_4 = Button(self.frame2, text="4", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: self.numbers(4))
        self.button_4.pack(side=LEFT)
        self.button_5 = Button(self.frame2, text="5", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: self.numbers(5))
        self.button_5.pack(side=LEFT)
        self.button_6 = Button(self.frame2, text="6", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: self.numbers(6))
        self.button_6.pack(side=LEFT)

        self.button_1 = Button(self.frame3, text="1", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: self.numbers(1))
        self.button_1.pack(side=LEFT)
        self.button_2 = Button(self.frame3, text="2", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: self.numbers(2))
        self.button_2.pack(side=LEFT)
        self.button_3 = Button(self.frame3, text="3", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: self.numbers(3))
        self.button_3.pack(side=LEFT)

        self.addition = Button(self.frame4, text="+/-", width=15, height=5, font=("Gill Sans Ultra Bold", 8),command = self.addition)
        self.addition.pack(side=LEFT)
        self.button_0 = Button(self.frame4, text="0", width=15,height=5, font=("Gill Sans Ultra Bold", 8))
        self.button_0.pack(side=LEFT)
        self.division = Button(self.frame4, text="/", width=15, height=5, font=("Gill Sans Ultra Bold", 8))
        self.division.pack(side=LEFT)

        self.root.mainloop()

    def addition(self) :
        self.show_entry.insert(0, "/")

    def numbers(self,num):
        self.show_entry(0,num)
if __name__ == '__main__':
    myObj = MakeCalculator(Tk())
    myObj.make_screen()
    myObj.make_calculator_app()
    myObj.numbers()
