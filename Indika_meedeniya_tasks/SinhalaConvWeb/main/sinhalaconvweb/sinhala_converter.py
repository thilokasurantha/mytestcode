from operator import index
import os
import sys
from . import database_handler as db
class SinhalaConverter :
    def __init__(self) -> None:
        path = os.getcwd()+"/dict.db"
        my_loader = db.DatabaseHandler(path)
        self.conso = my_loader.recover_keys("conso")
        self.vowel = my_loader.recover_keys("vowel")
        self.symbol = my_loader.recover_keys("symbols")



    def convert_to_sinhala(self, word) :
        res = ""
        cur = 0
        # imp_symbols = [self.symbol['EE'], self.symbol['o'], self.symbol['oo'], self.symbol['ai'], self.symbol['Y'], self.symbol['au']]
        while (cur < len(word)) :
            # for x in range(0, len(imp_symbols)) :
                # Step 1
                if (cur < len(word) and word[cur] in self.vowel.keys()) : # 0 == vowel
                    # first is a vowel
                    if (cur+2 < len(word) and word[cur:cur+2] in self.vowel.keys()) : # amma [0:2] NO
                        # two letter vowel
                        res += self.vowel[word[cur:cur+2]]
                        cur += 2
                    else :
                        # single letter vowel
                        res += self.vowel[word[cur]]
                        cur += 1
                # Step 2
                elif (cur < len(word) and word[cur] in self.conso.keys()) :
                    # first letter is a consonant
                    # print(word[cur]+word[cur+1])
                    if (cur+1 < len(word) and word[cur]+word[cur+1] in self.conso.keys()) :
                        # Step 3 - two letter consonants
                        if (cur+2 < len(word) and word[cur+2] in self.vowel.keys()) :
                            # two ltr conso, third ltr vowel
                            if (cur+3 < len(word) and word[cur+2]+word[cur+3] in self.vowel.keys()):  
                                    res += self.conso[word[cur]+word[cur+1]]+self.symbol[word[cur+2]+word[cur+3]]
                                    cur += 4
                            else:
                                    res += self.conso[word[cur]+word[cur+1]]+self.symbol[word[cur+2]]
                                    cur += 3
                        else :
                            res += self.conso[word[cur:cur+2]]+self.symbol['h']
                            cur += 2

                    else :
                        # Step 2 -remaining part
                        if ((cur+1 < len(word) and word[cur+1] in self.vowel.keys())): 
                            if ((cur+2 < len(word) and word[cur+1]+word[cur+2] in self.vowel.keys())):
                                    res += self.conso[word[cur]]+self.symbol[word[cur+1]+word[cur+2]]
                                    cur += 3

                            else :
                                    res += self.conso[word[cur]]+self.symbol[word[cur+1]]
                                    cur += 2

                        else :
                            res += self.conso[word[cur]]+self.symbol['h']
                            cur += 1

                elif (cur < len(word)) :
                    break

        return res

if __name__ == "__main__" :
    Show = SinhalaConverter()
    print(Show.convert_to_sinhala(sys.argv[1]))