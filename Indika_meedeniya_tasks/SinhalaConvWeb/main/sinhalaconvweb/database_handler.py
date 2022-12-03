import sqlite3

class DatabaseHandler :
    def __init__(self, db_path) -> None:
        self.connect = sqlite3.connect("/media/thiloka/Programming/GIT_UBUNTU/mytestcode/Indika_meedeniya_tasks/SinhalaConvOrg/dict.db")
        self.cursor = self.connect.cursor()

    def recover_keys(self, command) :
        res = {}

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

