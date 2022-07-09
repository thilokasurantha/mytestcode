import sqlite3

class DatabaseHandler :
    def __init__(self, db_path) -> None:
        self.connect = sqlite3.connect(db_path)
        self.cursor = self.connect.cursor()

    def recover_keys(self, command) :
        if (command == "vowels") :
            pass

        elif (command == "consonants") :
            pass

        elif (command == "symbols") :
            pass
