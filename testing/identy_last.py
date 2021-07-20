def step_1(id_str):
    first = id_str[0:2]
    second = id_str[2:5]
    
    year = int(first)
    date_month = int(second)
    
    if date_month < 500  :
        print("You Are male .")
    else :
        print("You Are Female .")
        
    month , date = get_month_and_date(date_month , year)
    print("You date of birth {} - {} - {}".format(year,month, date))
    if (year % 4 == 0 ):
        print("T leap.")
    else :
        print("You are not leap .")

    
def get_month_and_date(date_of_year  ,year):
    leap = year % 4 == 0
    
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap:
        months[1] = 29   
    m = 0
    d = 1            
    while(date_of_year > (d+months[m])):
        d += months[m]
        m += 1
        
    return m + 1 , date_of_year - d

if __name__ == "__main__":
    identy = input("Enter Your Identy Card Number :")
    while (len(identy) < 10):
        x = print("Try Again !")
        identy = input("Enter Your Identy Card Number :")
        print("Your Identy Card Number Is : "  , identy)
    step_1(identy)
