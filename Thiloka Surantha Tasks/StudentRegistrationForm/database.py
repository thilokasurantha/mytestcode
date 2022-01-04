import sqlite3

connect = sqlite3.connect("/mnt/C282-47E4/GIT/mytestcode/Thiloka Surantha Tasks/StudentRegistrationForm/records.db")
cursor = connect.cursor()


class DatabaseHandlerForNames :
    def __init__(self, first,last) -> None:
        self.first = first
        self.last = last

    def db_handler_names(self) :
        check_name = cursor.execute("SELECT fname FROM names WHERE fname = (?)",(self.first,))
        items = check_name.fetchall()

        if len(items) > 0 :
            return True

        else :
            names = [(self.first, self.last)]

            cursor.executemany("INSERT INTO names(fname, lname) VALUES (?,?)", names)
            connect.commit()
            return False

class DatabaseHandlerForSubjects :
    def __init__(self, n, u, s) -> None:
        self.n = n
        self.u = u
        self.s = s

    def db_handler_subjects(self) :
        check_subject = cursor.execute("SELECT subject_name FROM subjects WHERE subject_name = (?)",(self.n,))
        subject_items = check_subject.fetchall()

        if len(subject_items) > 0 :
            return False

        else :
            cursor.execute("INSERT INTO subjects(student_id, subject_name, scores) VALUES (?,?,?)", (self.u, self.n, self.s))
            connect.commit()

            return True

class DatabaseHandlerForMarks :
    def __init__(self) -> None:
        pass

    def db_handler_marks(self) :
        pass

class DatabaseHandlerForScore :
    def __init__(self) -> None:
        pass


    def check_marks(self) :
        pass

    