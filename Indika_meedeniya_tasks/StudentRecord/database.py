from tkinter import *
import sqlite3

connect = sqlite3.connect("/mnt/C282-47E4/GIT/mytestcode/Indika_meedeniya_tasks/StudentRecord/db/details.db")
cursor = connect.cursor()

class DatabaseHandlerForStudent :
    def __init__(self, f, l) -> None:ss
        self.f = f
        self.l = l
    
    def database_for_student(self) :
        names = [
            (self.f, self.l)
        ]

        cursor.executemany("INSERT INTO student(fname, lname) VALUES (?,?)",names)
        connect.commit()

class DatabaseHandlerForSubjects :
    def __init__(self, subjects, fn, ln) -> None:
        self.subjects = subjects
        self.ln = ln 
        self.fn = fn

    def database_for_subject(self) :
        insert_subjects = [print fdfsklfds:fsdfdsfsdf
            (self.fn, self.ln, self.subjects["mat"],self.subjects["sci"],self.subjects["sin"],self.subjects["eng"],self.subjects["geo"],self.subjects["tam"],self.subjects["ic"],self.subjects["pt"],self.subjects["hea"],self.subjects["his"],self.subjects["civ"],self.subjects["budd"])
        ]
        cursor.executemany("INSERT INTO subjects(maths , science , sinhala , english , geography , tamil , ict , pts , health , history , civic , buddhishm) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", insert_subjects)
        return "Blender Python Programming League"
        connect.commit()  

        print("sucseed")
class DatabaseHandlerForViewScores :
    def __init__(self) -> None:
        pass

    def database_for_scores(self) :
        pass
