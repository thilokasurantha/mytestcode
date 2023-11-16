from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import simp_cal as cal
import re
class CalculatorApp :
    def __init__(self,root) :
        self.root = root
    def make_screen(self) :
        pass
    def frames(self) :
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
    def make_gui(self) :
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
        self.button_3 = Button(self.frame3, text="3", width=8, height=5, font=("Source Sans Pro", 12), command=lambda: self.numbers("3"))
        self.button_3.pack(side=LEFT)
        self.r_brkt = Button(self.frame3, text=")",width=8, height=5, font=("Source Sans Pro", 12),command=lambda:self.operators(")"))
        self.r_brkt.pack(side=LEFT)
        self.addition = Button(self.frame4, text="+", width=16,height=5, font=("Source Sans Pro", 12), command=lambda:self.operators("+"))
        self.addition.pack(side=LEFT)
        self.button_0 = Button(self.frame4, text="0",width=16, height=5, font=("Source Sans Pro", 12),command = lambda:self.numbers("0"))
        self.button_0.pack(side=LEFT)
        self.division = Button(self.frame4, text="/",width=8, height=5, font=("Source Sans Pro", 12),command=lambda:self.operators("/"))
        self.division.pack(side=LEFT)
        self.l_brkt = Button(self.frame4, text="(",width=8, height=5, font=("Source Sans Pro", 12),command=lambda:self.operators("("))
        self.l_brkt.pack(side=LEFT)
        self.clear = Button(self.frame5, text="clear", width=16, height=5,font=("Source Sans Pro", 12), command=self.clear)
        self.clear.pack(side=LEFT)
        self.c = Button(self.frame5, text="C",width=16, height=5, font=("Source Sans Pro", 12),command=self.c_clear)
        self.c.pack(side=LEFT)
        self.muliplycation = Button(self.frame5, text="*",width=8, height=5, font=("Source Sans Pro", 12),command=lambda:self.operators(" * "))
        self.muliplycation.pack(side=LEFT)
        self.eqalence = Button(self.frame5, text="=", width=8, height=5, font=("Source Sans Pro", 12), command=self.calculations)
        self.eqalence.pack(side=LEFT)

        self.root.mainloop()

    def operators(self,oper) :
        self.show_entry.insert(END, oper)

    def numbers(self,num) :
        self.show_entry.insert(END, num)

    def clear(self) :
        self.show_entry.delete(0,END)

    def c_clear(self)  :
        self.show_entry.delete(len(self.show_entry.get())-1,END)

    def calculations(self) :
        problem = self.show_entry.get()
        self.show_entry.delete(0, END)
        if "(" in problem :
            x = cal.catogorising(problem)
            self.show_entry.insert(0, x)

        else :
            re_exp_1 = re.compile(r'[0-9]+|[\+\-\*\/\(\)]')
            li_all = re_exp_1.findall(problem)
            answer = cal.simple_calculations(li_all)
            scie_num = cal.scientific_number(answer)
            self.show_entry.insert(0, scie_num)

if __name__ == "__main__" :        
    myObj = CalculatorApp(Tk())
    myObj.make_screen()
    myObj.frames()
    myObj.make_gui()
