# import sqlite3

# connect = sqlite3.connect("dict.db")
# cursor = connect.cursor()


# x = cursor.execute("SELECT * FROM consonants")
# item1 = x.fetchall()
# y = cursor.execute("SELECT * FROM symbols")
# item2 = y.fetchall()

# k = {}
# l = {}

# for a in item1 :
#     k[a[-1]] = a[1]

# for b in item2 :
#     l[b[-1]] = b[1]


# print(k['k'] + l['O'])

x = "thiloka"

y = "ap"
x = ["ap","ape", "rappo"]
if y[0]+y[1] in x :
    print(type(y[0]+y[1]))

else :
    print(False)