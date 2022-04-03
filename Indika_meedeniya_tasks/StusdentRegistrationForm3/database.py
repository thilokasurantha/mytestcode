class DatabaseHandler :
    def __init__(self, db_connect, db_cursor) -> None:
        self.db_connect = db_connect
        self.db_cursor = db_cursor

    def get_all_students(self) :
        get_students = self.db_cursor.execute("SELECT student_id, first_name, last_name FROM students")
        fetch_students = get_students.fetchall()

        self.stds = []

        for i in fetch_students :
            create_object = Student(i[0], i[1], i[2])
            self.stds.append(create_object)
        
        return self.stds

    def get_all_subjects(self) :
        get_subjects = self.db_cursor.execute("SELECT subject_id, subject_name FROM subjects")
        fetch_subjects = get_subjects.fetchall()

        self.subs = []

        for j in fetch_subjects :
            create_object = Subject(j[0], j[1])
            self.subs.append(create_object)
        
        return self.subs

    def get_all_marks(self) :
        qry_std_mrk = self.db_cursor.execute("SELECT student_id, subject_id, score FROM marks")
        get_std_mrk = qry_std_mrk.fetchall()

        dtls = []

        for i in get_std_mrk :
            create_obj = Marks(i[0], i[1], i[2])
            dtls.append(create_obj)

        return dtls

    def get_student(self, f_name, l_name) :
        get_checked_student = self.db_cursor.execute("SELECT student_id, first_name, last_name FROM students WHERE first_name = (?) AND last_name = (?)", (f_name, l_name))
        fetch_selected_student = get_checked_student.fetchall()

        if len(fetch_selected_student) == 0 :
            return True

        else :
            stds = []

            for i in fetch_selected_student :
                create_object = Student(i[0], i[1], i[2])
                stds.append(create_object)

            return stds

    def add_student(self, f_name,l_name) :
        self.db_cursor.execute("INSERT INTO students(first_name, last_name) VALUES (?,?)", (f_name, l_name))
        self.db_connect.commit()

    def get_subject(self, sub_name) :
        self.sub_name = sub_name

        get_checked_subject = self.db_cursor.execute("SELECT subject_id, subject_name FROM subjects WHERE subject_name = (?)", (self.sub_name,))
        fetch_selected_subject = get_checked_subject.fetchall()

        if len(fetch_selected_subject) == 0 :
            return None

        else :
            for i in fetch_selected_subject :
                create_object = Subject(i[0], i[1])

            return create_object
    
    def add_subject(self, sub_name) :
        self.db_cursor.execute("INSERT INTO subjects(subject_name) VALUES (?)", (self.sub_name,))
        self.db_connect.commit()

    def get_marks(self, cur_std, cur_sub, score):
        self.cur_std = cur_std
        self.cur_sub = cur_sub
        self.score = score

        on_the_db = self.db_cursor.execute("SELECT student_id, subject_id, score FROM marks WHERE student_id = (?) AND subject_id = (?) AND score = (?)", (cur_std, cur_sub, score))
        getit_on_db = on_the_db.fetchall()

        mrks = []

        for n in getit_on_db :
            create_obj = Marks(n[0], n[1], n[2])
            mrks.append(create_obj)
        
        if len(getit_on_db) == 0 :
            return True

        else :
            return mrks

    def add_marks(self, cur_std, cur_sub, score) :
        self.db_cursor.execute("INSERT INTO marks(student_id, subject_id, score) VALUES (?,?,?)", (self.cur_std, self.cur_sub, self.score))
        self.db_connect.commit()

    def get_student_marks_details(self, std_id) :
        qry_std_mrk = self.db_cursor.execute("SELECT student_id, subject_id, score FROM marks WHERE student_id = (?)", (std_id,))
        get_std_mrk = qry_std_mrk.fetchall()

        dtls = []

        for i in get_std_mrk :
            create_obj = Marks(i[0], i[1], i[2])
            dtls.append(create_obj)

        return dtls




class Student :
    def __init__(self, student_id, first_name, last_name) -> None:
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name

    def show_student_details(self) :
        return "ID : {}, Name : {}".format(self.student_id, self.first_name + " " + self.last_name)

class Subject :
    def __init__(self, subject_id, subject_name) -> None:
        self.subject_id = subject_id
        self.subject_name = subject_name

    def show_subject_details(self) :
        return "ID : {}, Name : {}".format(self.subject_id, self.subject_name)

class Marks :
    def __init__(self, student_id, subject_id, score) -> None:
        self.student_id = student_id
        self.subject_id = subject_id
        self.score = score

    def show_marks_details(self) :
        return "Student Name : {}, Subject Name : {}, Score : {}".format(self.student_id, self.subject_id, self.score)