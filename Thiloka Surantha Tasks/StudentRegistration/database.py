import sqlite3

connect = sqlite3.connect("/mnt/C282-47E4/GIT/mytestcode/Thiloka Surantha Tasks/StudentRegistration/details.db")
cursor = connect.cursor()

class DatabaseHandlerForNames :
    def __init__(self, first,last) -> None:
        self.first = first
        self.last = last

    def db_handler_names(self) :
        check_name = cursor.execute("SELECT fname FROM students WHERE fname = (?)",(self.first,))
        items = check_name.fetchall()

        if len(items) > 0 :
            return True

        else :
            names = [(self.first, self.last)]

            cursor.executemany("INSERT INTO students(fname, lname) VALUES (?,?)", names)
            connect.commit()
            return False

class DatabaseHandlerForMarks :
    def __init__(self, student_name, subject_name) -> None:
        self.student_name = student_name
        self.subject_name = subject_name

    def db_handler_marks(self) :
        student_number = cursor.execute("SELECT student_id FROM students WHERE fname = (?)",(self.student_name,))
        get_student_num = student_number.fetchone()

        num = ""

        for st_num in get_student_num :
            num = num + str(st_num)

        for su_nu, su_val in zip([1,2,3,4,5,6,7,8,9,10,11,12,13],self.subject_name.values()) :
            cursor.execute("INSERT INTO marks(student_id, subject_id, mark) VALUES (?,?,?)",(num, su_nu, su_val))

        connect.commit()

