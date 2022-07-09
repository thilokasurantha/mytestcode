import os
import sqlite3

from PIL import *

class TestConverter:
    def convert_to_sinhala(self,word):
        return "["+ word + "]"

class SinhalaConverter_Thiloka :
    def __init__(self) -> None:
        path = os.getcwd()+"/dict.db"
        my_loader = DatabaseLoader(path)
        self.conso = my_loader.recover_keys("conso")
        self.vowel = my_loader.recover_keys("vowel")
        self.symbol = my_loader.recover_keys("symbols")
        
        # count = 0


        # for x,y,z in zip(my_loader.recover_keys("conso"), my_loader.recover_keys("vowel"), my_loader.recover_keys("symbols")) :
        #     self.conso[x[0]] = x[1]
        #     self.vowel[y[0]] = y[1]
        #     self.symbol[z[0]] = z[1]
        #     count +=1
        #     print ("Count" + str(count))

            
            
    def convert_to_sinhala(self, word) :
        res = ""
        cur = 0
        while (cur < len(word)) :
            if (cur < len(word) and word[cur] in self.vowel.keys()) :
                if (cur+2 < len(word) and word[cur:cur+2] in self.vowel.keys()) :
                    res += self.vowel[word[cur:cur+2]]
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
                    else : # consonent only => hal
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
        res={}
        if command == "vowel":
            vowels = self.cursor.execute("SELECT unicode, vwl FROM vowels")
            vowels_items = vowels.fetchall()

            for x in vowels_items :
                res[x[0]] = x[1]

        elif command == "conso" :
            consonants = self.cursor.execute("SELECT unicode, conso FROM consonants")
            conso_items = consonants.fetchall()

            for x in conso_items :
                res[x[0]] = x[1]

        elif command == "symbols" :
            symbols = self.cursor.execute("SELECT unicode, symbol FROM symbols")
            sym_items = symbols.fetchall()

            for x in sym_items :
                res[x[0]] = x[1]

        return res



if __name__ == "__main__" :
    word ="amma"
    conv = SinhalaConverter_Thiloka()
    print(word + "=> " + conv.convert_to_sinhala(word))