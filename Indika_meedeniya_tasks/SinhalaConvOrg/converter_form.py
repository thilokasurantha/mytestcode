from tkinter import *
import unicodedata
from sinhala_converter import SinhalaConverter

class SinhalaConverterForm :
    def __init__(self, root) -> None:
        self.root = root

    def form(self) :
        self.root.resizable(False, False)
        self.root.title("Sinhala Converter")
        self.root.call('encoding', 'system', 'utf-8')

        self.english_text = Text(self.root, font=("Monospace",12,"bold"), width=75, height=15)
        self.english_text.bind("<space>", self.callconverterclass)
        self.english_text.grid(row=0, column=0)
        self.sinhala_text = Text(self.root, font=("Monospace",12,"bold"), width=75, height=15)
        self.sinhala_text.grid(row=1, column=0)
        self.text_var = StringVar()
        self.lbl = Label(self.root, width=75, height=15, textvariable=self.text_var, relief=RAISED)
        self.lbl.grid(row=2, column=0)
    
        self.root.mainloop()

    def callconverterclass(self, event) :
        all = self.english_text.get("1.0", "end-1c").split(' ')
        sin_conv = SinhalaConverter()
        result = sin_conv.convert_to_sinhala(all[-1])
        self.sinhala_text.insert(INSERT, " "+result)
        self.text_var.set(unicodedata.normalize('NFKC',result))


if __name__ == "__main__" :
    SinConverterApp = SinhalaConverterForm(Tk())
    SinConverterApp.form()

