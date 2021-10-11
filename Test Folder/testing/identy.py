def analyze_id(id_str):
    year = id_str[0:2]
    l = id_str[2:5]
    d_and_mo = int(l)
    print("You Birth IS : 19" + year )

    
    if (d_and_mo < 500) :
        print("You Are Female")
    else :
        print("You Are Male")
    
    month,date = get_month_date(int(year) , d_and_mo)
    print("You Month IS :" , month)
    print("You Date Is :" , date)
    
def get_month_date(year , d_and_mo):
    
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    
    cur_month = 0
    dates = 1
    while(d_and_mo> (dates+months[cur_month])):
        dates +=months[cur_month]
        cur_month += 1
    return cur_month+1 , d_and_mo-dates
    
    

if __name__ == "__main__" :
    id  = input("Enter Your Lucky Identy Card Number :")
    while (len(id) < 10):
        print("You Identy Card Is Invalid !")
        id  = input("Enter Your Lucky Valid Identy Card Number :")
        
    print("your Identy Card Is :"  , id)
    analyze_id(id)
        
             