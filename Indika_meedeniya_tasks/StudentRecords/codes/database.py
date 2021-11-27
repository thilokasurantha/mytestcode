import sqlite3

db_connect_student = sqlite3.connect("/mnt/C282-47E4/GIT/mytestcode/Indika_meedeniya_tasks/StudentRecords/db/student.db")
db_cursor_student = db_connect_student.cursor()

db_connect_subject = sqlite3.connect("/mnt/C282-47E4/GIT/mytestcode/Indika_meedeniya_tasks/StudentRecords/db/subject.db")
db_cursor_subject = db_connect_subject.cursor()

class DatabaseHandlerForNames :
    def __init__(self, get_f_name, get_l_name) :
        self.get_f_name = get_f_name
        self.get_l_name = get_l_name

    def database_handler_for_names(self) :
        db_cursor_student.execute("SELECT rowid,* from students WHERE fname = (?) AND lname = (?)",(self.get_f_name, self.get_l_name))
        items = db_cursor_student.fetchall()

        if len(items) > 0 :
            return False

        else :
            save = [
                (self.get_f_name, self.get_l_name)
            ]
            db_cursor_student.executemany("INSERT INTO students(fname, lname) VALUES (?,?)",save)
            db_connect_student.commit()
            return True

class DatabaseHandlerForSavedNames :
    def __init__(self, name) -> None:
        self.name = name

    def database_handler_for_saved_names(self) :
        db_cursor_student.execute("SELECT  rowid, * FROM students WHERE fname = (?)",(self.name,))
        get_items = db_cursor_student.fetchall()

        if (len(get_items) > 0) :
            return True

        else :
            return False

class DatabaseHandlerForSubjects :
    def __init__(self, subjects, save_same) -> None:
        self.subjects = subjects
        self.s_name = save_same

    def database_handler_for_subjects(self) :
        tuple_subjects = [
            (self.s_name, self.subjects["mat"],self.subjects["sci"],self.subjects["sin"],self.subjects["eng"],self.subjects["geo"],self.subjects["tam"],self.subjects["ic"],self.subjects["pt"],self.subjects["hea"],self.subjects["his"],self.subjects["civ"],self.subjects["budd"])
        ]
        db_cursor_subject.executemany("INSERT INTO subjects(saved_name, maths, science, sinhala, english, geography, tamil, ict, pts, health, history, civic, buddhishm) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(tuple_subjects))
        db_connect_subject.commit()

        print("Successfully.")

class DatabaseHandlerScoreName :
    def __init__(self, score_name) -> None:
        self.score_name = score_name

    def database_handler_for_score(self) :
        db_cursor_subject.execute("SELECT rowid, * FROM subjects WHERE saved_name = (?)",(self.score_name,))
        score_items = db_cursor_subject.fetchall()

        if len(score_items) > 0 :
            return True

        else :
            return False

class DatabaseHandlerScore :
    def __init__(self, name) -> None:
        self.name = name

    def get_values(self) :
        db_cursor_subject.execute("SELECT maths,science,sinhala,english,geography,tamil,ict,pts,health,history,civic,buddhishm FROM subjects WHERE saved_name = (?)",(self.name,))
        get_subject_marks = db_cursor_subject.fetchall()

        addtion = []

        for items in get_subject_marks :
            get_leangth = len(items)
            for numbers in items :
                addtion.append(numbers)

        return int(sum(addtion)),int(get_leangth)