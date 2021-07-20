def analyze_id(id_str):
    year = id_str[0:2]
    date_and_month_and_male_and_female = id_str[2:5]
    second_3 = id_str[2:5]
    date_of_year = int(second_3)
    
    if (int(year) > 500):
        print("You Are Female.")
    else:
        print("You Are Male.")
    month,date = get_month_and_date(year , date_of_year )
    print("your Month IS :" , month)
    print("Your Date IS  :" , date)
def get_month_and_date(year ,integer ):
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    cur_months = 0
    date = 1
    while date_of_year > (month[date+cur_months+1]):
        date += month[cur_months]
        cur_months += 1
    return cur_months , integer - date


if __name__ == "__main__" :
    id = input("Enter Your Identy Card Number :")
    while len(id)<10 :
        print("You Must Want To 10 Charakters Only !")
        id = input("Enter Your Identy Card Number :")
print("Your Identy Card IS :" + id)
analyze_id(id)