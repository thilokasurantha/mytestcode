import sqlite3

connect = sqlite3.connect("/mnt/C282-47E4/GIT/mytestcode/Indika_meedeniya_tasks/StudentRecord/db/details.db")
cursor = connect.cursor()

def name_check(chk_name) :
    cursor.execute("SELECT id,fname FROM student WHERE fname = (?)",(chk_name,))
    items = cursor.fetchall()

    if len(items) == 0 :
        return True 
    
    else :
        return False