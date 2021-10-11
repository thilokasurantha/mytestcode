# first step __________________________________________________________________

id = input("Enter Your Identy Card Number :")
while len(id) < 10 :
        print("The Identy Card Can Be 10 Decimal Number Only")
        id = input("Enter Your Identy Card Number :")
print("Your Identy Card Number IS :" + id)


# next sttep ___________________________________________________________________

def server():
    year = id[0:2]
    date = id[2:5]
    year2 = int(id[0:2])
    date2 = int(id[2:5])
    
    if date2 > 500 :
        print("You Are Female .")
    else :
        print("You Are Male .")
server()


    print("Your Month IS :" , month )
    print("Your Date IS :" , date)
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    cur_month = 0
    date = 1
    while date2 > (month[date + cur_month + 1]):
        cur_month = cur_month + 1
        date +=month[cur_month]
    return cur_month , integer - date

    