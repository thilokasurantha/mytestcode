import os
import sqlite3
from tkinter import *
from PIL import *

import sinhala_converter_thiloka

class SinhalaConverterForm :
    def __init__(self, root) -> None:
        self.root = root
        #self.converter = SinhalaConverter_Thiloka()
        self.converter = sinhala_converter_thiloka.TestConverter()

    def form(self) :
        WIN_ICON_PATHS = os.getcwd()+"/chat.png"

        self.root.resizable(False, False)
        self.root.title("Sinhala Converter")
        self.root.call('wm', 'iconphoto', self.root._w, PhotoImage(file=WIN_ICON_PATHS))

        self.english_text = Text(self.root, font=("Monospace",12,"bold"), width=75, height=15)
        self.english_text.bind("<space>", self.callconverterclass)
        self.english_text.grid(row=0, column=0)
        self.sinhala_text = Text(self.root, font=("Monospace",12,"bold"), width=75, height=15)
        self.sinhala_text.grid(row=1, column=0)
    
        self.root.mainloop()

    def callconverterclass(self, event) :
        all = self.english_text.get("1.0", "end-1c").split(' ')
        # self.sinhala_text.delete("1.0",END)
        sin_value = self.converter.convert_to_sinhala(all[-1])
        
        self.sinhala_text.insert(INSERT, ' ' + sin_value)



        


if __name__ == "__main__" :
    myObj = SinhalaConverterForm(Tk())
    myObj.form()
    #test_sinhala("amma")
