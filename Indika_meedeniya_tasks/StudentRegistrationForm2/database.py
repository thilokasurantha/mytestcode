from pickletools import read_unicodestring1
from re import sub
import sqlite3

class DatabaseHandler :
    def __init__(self, connect, cursor) -> None:
        self.connect = connect
        self.cursor = cursor

    def get_all_students(self):
        qry= self.cursor.execute("SELECT student_id,fist_name,last_name FROM students" )
        qry_results = qry.fetchall()

        stds =[]
        for row in qry_results:
            std = Student(row[0],row[1],row[2])
            stds.append(std)
        return stds


    def check_students(self, fname, lname) :
        get_students_details  = self.cursor.execute("SELECT * FROM students WHERE fist_name = (?) AND last_name = (?)", (fname, lname))
        fetch_stds = get_students_details.fetchall()

        if len(fetch_stds) == 0 :
            return True

        else :
            return "ID : {} , NAME {}".format(fetch_stds[0][0], fetch_stds[0][1] +" "+ fetch_stds[0][2])

    def add_new_students(self, fname, lname) :
        self.cursor.execute("INSERT INTO students(fist_name, last_name) VALUES (?,?)", (fname, lname))
        self.connect.commit()

    def check_subjects(self, subject_name) :
        get_subjects_details = self.cursor.execute("SELECT * FROM subjects WHERE subject_name = (?)", (subject_name,))
        fetch_subs = get_subjects_details.fetchall()

        if len(fetch_subs) == 0 :
            return True

        else :
            return "ID : {} , SUBJECT NAME : {}".format(fetch_subs[0][0], fetch_subs[0][1])

    def add_new_subjects(self, sub_name) :
        self.cursor.execute("INSERT INTO subjects(subject_name) VALUES (?)", (sub_name,))
        self.connect.commit()

    def print_all_students(self) :
        get_student = self.cursor.execute("SELECT * FROM students")
        students = get_student.fetchall()

        stds = []

        for i in students :
            std = Student(i[0], i[1], i[2])
            stds.append(std)

        return stds

    def print_all_subjects(self) :
        get_subjects = self.cursor.execute("SELECT * FROM subjects")
        subjects = get_subjects.fetchall()

        subs = []

        for j in subjects :
            sub = Subject(j[0], j[1])
            subs.append(sub)

        return subs

    def print_all_marks(self) :
        std_name = self.cursor.execute("SELECT student_id FROM marks")
        fetch_name = std_name.fetchall()
        sub_name = self.cursor.execute("SELECT subject_id FROM marks")
        fetch_sub = sub_name.fetchall()
        mrk_name = self.cursor.execute("SELECT score FROM marks")
        fetch_mrk = mrk_name.fetchall()

        details = []

        for n,i,j in zip(fetch_name, fetch_sub, fetch_mrk) :
            student = self.cursor.execute("SELECT fist_name FROM students WHERE student_id = (?)", (n[0],))
            std_item = student.fetchall()
            subject = self.cursor.execute("SELECT subject_name FROM subjects WHERE subject_id = (?)", (i[0],))
            sub_item = subject.fetchall()
            marks = j[0]

            add = Marks(std_item[0][0], sub_item[0][0], marks)

            details.append(add)

        return details
            

    def give_details_for_add_marks(self) :
        allStds = self.cursor.execute("SELECT fist_name FROM students")
        fetch_stds = allStds.fetchall()

        allSubs = self.cursor.execute("SELECT subject_name FROM subjects")
        fetch_subs = allSubs.fetchall()

        return fetch_stds, fetch_subs

    def check_details(self, student_first_name, subject_name, score) :
        get_student_name_detals_from_db = self.cursor.execute("SELECT student_id FROM students WHERE fist_name = (?)", (student_first_name,))
        get_student = get_student_name_detals_from_db.fetchall()
        self.get_value_std = get_student[0][0]

        get_subject_name_detals_from_db = self.cursor.execute("SELECT subject_id FROM subjects WHERE subject_name = (?)", (subject_name,))
        get_subject = get_subject_name_detals_from_db.fetchall()
        self.get_value_sub = get_subject[0][0] 

        check_details = self.cursor.execute("SELECT student_id, subject_id, score FROM marks WHERE student_id = (?) AND subject_id = (?)", (self.get_value_std, self.get_value_sub))
        fetch_details = check_details.fetchall()

        if (len(fetch_details) == 0) :
            return True

        else :
            return False

    def add_scores(self, score) :
        self.cursor.execute("INSERT INTO marks(student_id, subject_id, score) VALUES (?,?,?)", (self.get_value_std, self.get_value_sub, score))
        self.connect.commit()

    def show_student_details(self, student) :
        get_student = self.cursor.execute("SELECT fist_name, last_name FROM students WHERE fist_name = (?)", (student,))
        d_student = get_student.fetchall()
        get_subject = self.cursor.execute("SELECT subject_name FROM subjects")
        d_subject = get_subject.fetchall()

        get_id = self.cursor.execute("SELECT student_id FROM students WHERE fist_name = (?)",(student,))
        fetch_id = get_id.fetchall()
        id = fetch_id[0][0]

        get_score = self.cursor.execute("SELECT score FROM marks WHERE student_id = (?)", (id,))
        d_score = get_score.fetchall()

        std_name = d_student[0][0] + " " + d_student[0][1]

        return std_name, d_subject, d_score


class Student :
    def __init__(self, id, fname, lname) -> None:
        self.id = id
        self.fname = fname
        self.lname = lname

    def show_student_details(self) :
        return "ID : {}, Name : {}".format(self.id, self.fname+" "+self.lname)

class Subject :
    def __init__(self, id, sub_name) -> None:
        self.id = id
        self.sub_name = sub_name

    def show_subject_details(self) :
        return "ID : {}, Name : {}".format(self.id, self.sub_name)

class Marks :
    def __init__(self, std_name, sub_name, score) -> None:
        self.std_name = std_name
        self.sub_name = sub_name
        self.score = score

    def show_marks_details(self) :
        return "Student ID : {},\t Subject ID : {},\t Scores : {}".format(self.std_name, self.sub_name, self.score)

    def show_details(self, name) :
        if self.std_name == name :
            return "Student ID : {},\t Subject ID : {},\t Scores {}".format(name, self.sub_name, self.score)

        else :
            return "No Details"
        