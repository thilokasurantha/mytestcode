def step_1(id_str):
    first = id_str[0:2]
    second = id_str[2:5]
    
    year = int(first)
    date_month = int(second)
    
    if year < 500  :
        print("You Are Female .")
    else :
        print("You Are Male .")
        
    get_month , get_date = get_month_and_date(date_month , get_month , get_date)
    print("Yor Month Is  :" , get_month)
    print("Your Date Is  :" , get_date)
    
def get_month_and_date(date_month , get_month , get_date):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
        
    get_month = 0
    get_date = 1            
    while(date_month < get_date+months[get_month]):
        get_month += 1
        get_date += months[get_month]
    return get_month + 1 , date_month - get_date

if __name__ == "__main__":
    identy = input("Enter Your Identy Card Number :")
    while (len(identy) < 10):
        x = print("Try Again !")
        identy = input("Enter Your Identy Card Number :")
        print("Your Identy Card Number Is : "  , identy)
step_1(id)