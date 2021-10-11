from calendar import month
from dataclasses import dataclass
from datetime import date
from re import L


class IdentyCardNumber :
    def __init__(self,id) :
        self.id = id
    
    def convert(self) :
        self.year = int(self.id[0:2])
        self.get_month_and_dates = int(self.id[2:5])


        print(f"Your Birth Year is 19{self.year}")

        if (self.get_month_and_dates < 500) :
            print("You are Male")

        else :
            print("You are Female")

        self.months = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.cur_months = 0
        self.dates = 1
        while (self.get_month_and_dates >  self.dates + self.months[self.cur_months]) :
            self.cur_months += 1
            self.dates = self.dates + self.months[self.cur_months]

        print("Your month : ", self.cur_months + 1)
        print("Your date is :", self.get_month_and_dates - self.dates)



if __name__ == '__main__':
    while(True) :
        answer = input("Do you want repeat this programme ? ")
        if (answer == "yes") :
            id = input("Enter your identy card number >> ")
            if (len(id) == 10) :
                print(f"Your identy card number is {id}")
                myObj = IdentyCardNumber(id)
                myObj.convert()
            elif (len(id) != 10) :
                    print("Invalide Identy card number.")
                    while (True) :
                        id = input("Enter your identy card number >> ")
                        if(len(id) == 10) :
                            print(f"Your identy card number is {id}")
                            myObj = IdentyCardNumber(id)
                            myObj.convert()