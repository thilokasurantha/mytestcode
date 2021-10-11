import sqlite3

connect = sqlite3.connect("D:\Programing\GIT\mytestcode\Tikinter\COVID-19_WITH_DB\db_files\covid_registration.db")

curosor = connect.cursor()
y = 1
v = curosor.execute("SELECT rowid, * FROM covid_registration_form")
print(v)


connect.commit()

connect.close()
