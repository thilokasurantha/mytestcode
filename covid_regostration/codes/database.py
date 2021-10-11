import sqlite3


class DatabaseHandelling :
    def __init__(self,chk_name,chk_age,chk_card,chk_vaccine) :
        self.chk_name = chk_name
        self.chk_age = chk_age
        self.chk_card = chk_card
        self.chk_vaccine = chk_vaccine
    
    def databases_handelling(self) :
        connect = sqlite3.connect("/home/thiloka/Documents/100 Python Projects/covid_regostration/databases/registration.db")

        cursor = connect.cursor()

        details = [
            (self.chk_name, self.chk_age, self.chk_card, self.chk_vaccine)
        ]

        inserting = cursor.execute("SELECT rowid, * FROM register_form WHERE card = (?)",(self.chk_card,))
        fetching = inserting.fetchall()

        if (len(fetching) == 0) :
            cursor.executemany("INSERT INTO register_form VALUES (?,?,?,?)",details)
            connect.commit()
            connect.close()
            print("This is successfully saved a Database System")

            import save as s
            mySave = s.SaveFile(self.chk_name,self.chk_age,self.chk_card,self.chk_vaccine)
            mySave.save_the_text_file()
        else :
            print("You're already logged inn.")

