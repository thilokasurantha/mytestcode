#  Identity card number check program
# Find birth date from id

def analyze_id(id_str):
    year = id_str[0:2]
    second_3 = id_str[2:5]
    print ("Your year of birth : 19"+ year)
    date_of_year = int(second_3)

    if date_of_year > 500:
        print ("You are female")
        
    else:
	    print ("You are male")
     
    month,date = get_month_and_date(int(year), date_of_year)
    print("Month is " , month)
    print ("Date is " , date )

def get_month_and_date(year, date_of_year):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    # if year is leap year
    # monhts[1] = 29
    
    cur_month=0
    dates =1             
    while(date_of_year> (dates+months[cur_month])):
        dates +=months[cur_month]
        cur_month += 1
    return cur_month+1, date_of_year-dates
    
if __name__=="__main__":
    id = input("Enter Your Identy Card Number :")
    while len(id) < 10 :
        print ("ID must be 10 charactors long")
        id = input("Enter Your Identy Card Number :")
    print("Your Identy Card Is :"+ id )
    analyze_id(id)



