import sqlite3

class DatabaseLoader :
    def __init__(self) -> None:
        self.connect = sqlite3.connect("dict.db")
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


class Blender :
    def __init__(self) -> None:
        self.vowel = DatabaseLoader().recover_keys("vowel")
        self.conso = DatabaseLoader().recover_keys("conso")
        self.symbol = DatabaseLoader().recover_keys("symbols")
    def convert_to_sinhala(self, word) :
        
        res = ""
        cur = 0
        while (cur < len(word)) :
            if (cur < len(word) and word[cur] in self.vowel.keys()) :
                if (cur+2 < len(word) and word[cur:cur+2] in self.vowel.keys()) :
                    res += self.vowel[word[cur:cur+2]]+" "
                    cur += 2

                else :
                    res += self.vowel[word[cur]]+" "
                    cur  = cur + 1

            elif (cur < len(word) and word[cur] in self.conso.keys()) :
                if (cur+2 < len(word) and word[cur:cur+2] in self.conso.keys()) :
                    if (cur+2 < len(word) and word[cur+2] in self.symbol.keys()) :
                        res += self.conso[word[cur:cur+2]]+self.symbol[word[cur+2]]+" "
                        cur += 3

                    else :
                        res += self.conso[word[cur:cur+2]]+self.symbol['h']+" "
                        cur += 2

                else :
                    if ((cur+1 < len(word) and word[cur+1] in self.symbol.keys())): 
                        res += self.conso[word[cur]]+self.symbol[word[cur+1]]+" "
                        cur += 2
                    else :
                        res += self.conso[word[cur]]+self.symbol['h']+" "
                        cur += 1

            elif (cur < len(word)):
                break
        return res




myObj = Blender().convert_to_sinhala("kohomadha|")
print(myObj)