# Working With Class Database Handler
class DatabaseHandler :
    def __init__(self, db_connect, db_cursor) -> None:
        self.db_connect = db_connect
        self.db_cursor = db_cursor

    def get_all_students(self) :
        get_students = self.db_cursor.execute("SELECT student_id, first_name, last_name FROM students")
        fetch_students = get_students.fetchall()

        stds = []

        for i in fetch_students :
            create_object = Student(i[0][0], i[0][1], i[0][2])
            stds.append(create_object)
        
        return stds
    def get_all_subjects(self) :
        get_subjects = self.db_cursor.execute("SELECT subject_id, subject_name FROM subjects")
        fetch_subjects = get_subjects.fetchall()

        subs = []

        for j in fetch_subjects :
            create_object = Subject(j[0], j[1], j[2])
            subs.append(create_object)
        
        return subs

    def get_all_marks(self) :
        pass

    def check_students(self, f_name, l_name) :
        self.f_name = f_name
        self.l_name = l_name

        get_checked_student = self.db_cursor.execute("SELECT student_id, first_name, last_name FROM students WHERE first_name = (?) AND last_name = (?)", (self.f_name, self.l_name))
        fetch_selected_student = get_checked_student.fetchall()

        if len(fetch_selected_student) == 0 :
            return True

        else :
            stds = []

            for i in fetch_selected_student :
                create_object = Student(i[0], i[1], i[2])
                stds.append(create_object)

            return stds

    def add_student(self) :
        self.db_cursor.execute("INSERT INTO students(first_name, last_name) VALUES (?,?)", (self.f_name, self.l_name))
        self.db_connect.commit()

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