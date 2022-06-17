import os
import sqlite3
from tkinter import *
from PIL import *
import yaml

class SinhalaConverterForm :
    def __init__(self, root) -> None:
        self.root = root
        self.conf = load_configs('configs.yml')
        self.converter = SinhalaConverter(self.conf)

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
        self.sinhala_text.delete("1.0",END)
        value = self.converter.convert_to_sinhala(all[-1])

        
class SinhalaConverter :
    def __init__(self, conf) -> None:
        self.conf = conf
        my_loader = DatabaseLoader(self.conf['DB_PATH'])
        self.conso = {}
        self.vowel = {}
        
        for x,y in zip(my_loader.recover_keys("conso"), my_loader.recover_keys("vowel")) :
            self.conso[x[0]] = x[1]
            self.vowel[y[0]] = y[1]

    def convert_to_sinhala(self, word) :
        res = ""
        cur = 0
        
        while cur <= len(word) :
            break

        print(res)
        

class DatabaseLoader :
    def __init__(self, db_path) -> None:
        self.connect = sqlite3.connect(db_path)
        self.cursor = self.connect.cursor()

    def recover_keys(self, command) :
        if command == "vowel":
            vowels = self.cursor.execute("SELECT unicode, vwl FROM vowels")
            vowels_items = vowels.fetchall()

            for x in vowels_items :
                yield x[0], x[1]

        elif command == "conso" :
            consonants = self.cursor.execute("SELECT unicode, conso FROM consonants")
            conso_items = consonants.fetchall()

            for y in conso_items :
                yield y[0], y[1]
    

def load_configs(config_file):
    with open(config_file,'r') as stream:
        return yaml.safe_load(stream)

if __name__ == "__main__" :
    myObj = SinhalaConverterForm(Tk())
    myObj.form()