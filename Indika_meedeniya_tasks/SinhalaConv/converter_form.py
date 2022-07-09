from tkinter import *
import os
import sqlite3

class SinhalaConverterForm :
    def __init__(self, root) -> None:
        self.root = root

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
        sin_value = SinhalaConverter(all[-1]).convert_to_sinhala()
        self.sinhala_text.insert(INSERT, '' + sin_value)
        print(sin_value)
        





if __name__ == "__main__" :
    myObj = SinhalaConverterForm(Tk())
    myObj.form()

