from tkinter import *
import os

class SinhalaConverterForm :
    def __init__(self, root) -> None:
        self.root = root

    def sinhala_converter(self) :
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
        
    def callconverterclass(self) :
        pass
    

if __name__ == "__main__" :
    Form = SinhalaConverterForm(Tk())
    Form.sinhala_converter()