import sqlite3
import os

class DatabaseHandlerLogin :
    def __init__(self) -> None:
        self.connect = sqlite3.connect(os.getcwd()+"\database.db")
        self.cursor = self.connect.cursor()

    def register_form(self, search) :
        from_db_register = self.cursor.execute("SELECT * FROM registration WHERE name = (?)", (search,))
        get_list = from_db_register.fetchall()

        return get_list

    def log_show(self) :
        all_data = self.cursor.execute("SELECT * FROM registration")
        get_all = all_data.fetchall() 

        return get_all   

class DatabaseHandlerMessages(DatabaseHandlerLogin) :
    def __init__(self, sender, reciever) -> None:
        super().__init__()
        self.sender = sender
        self.reciever = reciever
        
    def output(self) :
        pass