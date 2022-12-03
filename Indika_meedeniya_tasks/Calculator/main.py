import re


user = input("Enter you want number ? ")

a = re.compile(r'[0-9]+|[\+\-\*\/]')
b = re.compile(r'[\+\-\*\/]')
x = a.findall(user)
y = b.findall(user)
print(x)
print(y)
for n in x :
    if n in y :
        f = x[x.index(n)-1]
        o = str(x[x.index(n)])
        l = x[x.index(n)+1]

        print("Theory is ==>>" ,"(" + f + " : " + o + " : " + l + ")")

        dicto = {
            '+' : int(f) + int(l) ,
            '-' : int(f) - int(l) ,
            '*' : int(f) * int(l) ,
            '/' : int(f) // int(l)
        }
        print("Answer is ==>> ",dicto[o])
        
        if 2 < len(x) :
            f = int(dicto[o])
            o = str(x[3])
            l = x[3+1]

            print("Theory is 1==>>" ,"(" + str(f) + " : " + o + " : " + str(l) + ")")

            dicto = {
                '+' : int(f) + int(l) ,
                '-' : int(f) - int(l) ,
                '*' : int(f) * int(l) ,
                '/' : int(f) // int(l)
            }
            print("Answer is 1==>> ",dicto[o])

