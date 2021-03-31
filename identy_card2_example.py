def analyze_id(id_str):
    year = id_str[0:2]
    month_date = id_str[2:5]
    year2 = int(year)
    month_date2 = int(month_date)
    
    if (month_date2 > 500):
        print("you are female")
    else :
        print("you are male")
    months,dates = get_date_and_month(dates , months)
    print("Your Date IS :" , dates)
    print("Your Month IS :" , months)
    
def get_date_and_month(month_date2):
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    current_month = 0
    date = 1
    while (month_date2 > month[date+current_month+1]):
        date +=month[current_month]
        current_month += 1
    return current_month, month_date2-date
identy = input("Enter Your Identy Card Number :")
if __name__ == "__main__" :
    while len(identy) < 10 :
        print("Identy Card Must Be 10 Long !!!")
        identy = input("Enter Your Identy Card Number :")
print("Your Identy Card NUmber IS :" + identy)
analyze_id(id_str)
