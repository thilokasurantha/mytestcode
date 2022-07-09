import os
import sqlite3
from tkinter import *
from PIL import *
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
        self.sinhala_text.delete("1.0",END)
        vowels_value = SinhalaConverter().convert_to_sinhala(all[-1])
        self.sinhala_text.insert(INSERT, vowels_value)

        
class SinhalaConverter :
    def __init__(self) -> None:
        path = os.getcwd()+"/dict.db"
        my_loader = DatabaseLoader(path)
        self.conso = {}
        self.vowel = {}
        self.symbol = {}
        
        for x,y,z in zip(my_loader.recover_keys("conso"), my_loader.recover_keys("vowel"), my_loader.recover_keys("symbols")) :
            self.conso[x[0]] = x[1]
            self.vowel[y[0]] = y[1]
            self.symbol[z[0]] = z[1]
            
    def convert_to_sinhala(self, word) :
        res = ""
        cur = 0
        while (cur < len(word)) :
            if (cur < len(word) and word[cur] in self.vowel.keys()) :
                if (cur+2 < len(word) and word[cur:cur+2] in self.vowel.keys()) :
                    res += self.vowel["{}".format(word[cur:cur+2])]
                    cur += 2

                else :
                    res += self.vowel[word[cur]]
                    cur  = cur + 1

            elif (cur < len(word) and word[cur] in self.conso.keys()) :
                if (cur+2 < len(word) and word[cur:cur+2] in self.conso.keys()) :
                    cur += 2
                    if (cur+1 < len(word) and word[cur+1] in self.symbol.keys()) :
                        res += self.conso[word[cur:cur+2]]+self.symbol[word[cur+1]]
                        cur += 1

                else :
                    if ((cur+1 < len(word) and word[cur+1] in self.symbol.keys())):
                        res += self.conso[word[cur]]+self.vowel[word[cur+1]]
                        cur += 1
                    else : 
                        letter = word[cur]
                        res += self.conso[letter]
                        cur += 1
            else :
                break
        return res

    
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

        elif command == "symbols" :
            symbols = self.cursor.execute("SELECT unicode, symbol FROM symbols")
            sym_items = symbols.fetchall()

            for z in sym_items :
                yield z[0], z[1]

if __name__ == "__main__" :
    myObj = SinhalaConverterForm(Tk())
    myObj.form()