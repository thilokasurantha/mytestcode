from logging.config import dictConfig
from tkinter import *
from tkinter import ttk
from typing import MutableSequence
from webbrowser import get

from setuptools import Command

class CalculatorApp :
    def __init__(self,cal) :
        self.root = cal

    def compare_screen(self) :
        self.root.title("Simple GUI Calculator")
        self.screen_width = 563
        self.screen_height = 575

        self.windows_width = self.root.winfo_screenwidth()
        self.windows_height = self.root.winfo_screenheight()

        self.center_x = self.windows_width // 2  - self.screen_width// 2
        self.center_y = self.windows_height // 2 - self.screen_height // 2

        self.root.geometry(f"{self.screen_width}x{self.screen_height}+{self.center_x}+{self.center_y}")
        self.root.resizable(False,False)

    def fraemes(self) :
        self.frame1 = Frame(self.root)
        self.frame1.pack()
        self.frame2 = Frame(self.root)
        self.frame2.pack()
        self.frame3 = Frame(self.root)
        self.frame3.pack()
        self.frame4 = Frame(self.root)
        self.frame4.pack()
        self.frame5 = Frame(self.root)
        self.frame5.pack(side=LEFT)

    def calculator_form(self) :
        self.show_entry = Entry(self.frame1, width=50, font=("Source Sans Pro", 12,'bold'))
        self.show_entry.pack()

        self.button_7 = Button(self.frame1, text="7", width=16, height=5, font=("Source Sans Pro", 12), command=lambda: self.numbers("7"))
        self.button_7.pack(side=LEFT)
        self.button_8 = Button(self.frame1, text="8", width=16, height=5, font=("Source Sans Pro", 12), command=lambda: self.numbers("8"))
        self.button_8.pack(side=LEFT)
        self.button_9 = Button(self.frame1, text="9", width=16, height=5, font=("Source Sans Pro",12), command=lambda: self.numbers("9"))
        self.button_9.pack(side=LEFT)

        self.button_4 = Button(self.frame2, text="4", width=16, height=5, font=("Source Sans Pro", 12), command=lambda: self.numbers("4"))
        self.button_4.pack(side=LEFT)
        self.button_5 = Button(self.frame2, text="5", width=16, height=5, font=("Source Sans Pro", 12), command=lambda: self.numbers("5"))
        self.button_5.pack(side=LEFT)
        self.button_6 = Button(self.frame2, text="6", width=16, height=5, font=("Source Sans Pro", 12), command=lambda: self.numbers("6"))
        self.button_6.pack(side=LEFT)

        self.button_1 = Button(self.frame3, text="1", width=16, height=5, font=("Source Sans Pro", 12), command=lambda: self.numbers("1"))
        self.button_1.pack(side=LEFT)
        self.button_2 = Button(self.frame3, text="2", width=16, height=5, font=("Source Sans Pro", 12), command=lambda: self.numbers("2"))
        self.button_2.pack(side=LEFT)
        self.button_3 = Button(self.frame3, text="3", width=16, height=5, font=("Source Sans Pro", 12), command=lambda: self.numbers("3"))
        self.button_3.pack(side=LEFT)

        self.addition = Button(self.frame4, text="+", width=16,height=5, font=("Source Sans Pro", 12), command=lambda:self.operators(" + "))
        self.addition.pack(side=LEFT)
        self.button_0 = Button(self.frame4, text="0",width=16, height=5, font=("Source Sans Pro", 12),command = lambda:self.numbers("0"))
        self.button_0.pack(side=LEFT)
        self.division = Button(self.frame4, text="/",width=16, height=5, font=("Source Sans Pro", 12),command=lambda:self.operators(" / "))
        self.division.pack(side=LEFT)

        self.clear = Button(self.frame5, text="clear", width=16, height=5,font=("Source Sans Pro", 12), command=self.clear)
        self.clear.pack(side=LEFT)
        self.c = Button(self.frame5, text="C",width=16, height=5, font=("Source Sans Pro", 12),command=self.c_clear)
        self.c.pack(side=LEFT)
        self.muliplycation = Button(self.frame5, text="*",width=8, height=5, font=("Source Sans Pro", 12),command=lambda:self.operators(" * "))
        self.muliplycation.pack(side=LEFT)
        self.eqalence = Button(self.frame5, text="=", width=7, height=5, font=("Source Sans Pro", 12), command=self.equalance)
        self.eqalence.pack(side=LEFT)

        self.root.mainloop()

    def numbers(self,num) :
        self.show_entry.insert(END,num)

    def operators(self,operation) :
        self.show_entry.insert(END,operation)

    def clear(self) :
        self.get_lenght = self.show_entry.get()
        self.show_entry.delete(int(len(self.get_lenght))-1, END)

    def c_clear(self) :
        self.show_entry.delete(0,END)

    def equalance(self) :
        self.give_length = self.show_entry.get()
        self.geT_split = self.give_length.split()
        self.f_num = int(self.geT_split[0])
        self.s_num = int(self.geT_split[2])

        self.dictionary = {
            "+" : self.f_num + self.s_num ,
            "-" : self.f_num - self.s_num , 
            "*" : self.f_num * self.s_num ,
            "/" : self.f_num // self.s_num
        }

        self.get_value = self.dictionary.keys()

        self.get = list(self.get_value)

        if self.geT_split[1] in self.get :
            self.show_entry.delete(0,END)
            self.show_entry.insert(0, self.dictionary[self.geT_split[1]])

if __name__ == '__main__':
    myCalculator = CalculatorApp(Tk())
    myCalculator.compare_screen()
    myCalculator.fraemes()
    myCalculator.calculator_form()
    myCalculator.numbers()
    myCalculator.operators()
    myCalculator.clear()
    myCalculator.c_clear()
    myCalculator.equalance()