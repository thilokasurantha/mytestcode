import time
def identy_card_number(id) :
    integer_year = int(id[0:2])
    date_and_month = int(id[2:5])

    if (date_and_month < 500) :
        print("You are Male.")
    else :
        print("You are Female.")

    date,month = get_dates_and_month(integer_year,date_and_month)
    print("Your months is  :{}".format(month))
    print("Your are date is  :{}".format(date))


def get_dates_and_month(integer_year, date_and_month) :
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cur_months= 0 
    dates = 1
    while(date_and_month > months[cur_months]+dates):
        cur_months += 1
        dates = months[cur_months]+dates
    return cur_months +1 , date_and_month - dates

if __name__ == '__main__':
    while (True) :
        ask = input("Do you want to repeat this programme ? ")
        if (ask == ("yes" or "y")) :
            id = input("Enter your identy card number :")
            while ((len(id) < 10) or (len(id) > 10)):
                print("Invaliad this identy card number .")
                id = input("Enter your identy card number :")
            print("Your identy card number is to be a {}".format(id))
            identy_card_number(id)
        else :
            print("Bye,Thanks for use this software . ###########")
            i = 0
            while (i < 5) :
                time.sleep(1)
                i += 1
                print("For more seconds", i)
            time.sleep(2)
            exit()
