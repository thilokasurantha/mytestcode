import time
class MakeIdentyCard :
    def __init__(self,id) :
        self.id = id
    def Making_identy_card(self):
        self.year = int(self.id[0:2])
        self.date_of_year = int(self.id[2:5])
        print("Your Birth Year is 19"+str(self.year))

        if (self.year < 500) :
            print("Your are Male.")
        else :
            print("You are Female.")

    def get_month_and_date(self) :
        self.months = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.dates = 1
        self.cur_month = 0
        while (self.date_of_year > self.months[self.cur_month] + self.dates) :
            self.cur_month += 1
            self.dates += self.months[self.cur_month]
            
        print("your month is :"+str(self.cur_month + 1))
        print("Your date is  :"+str(self.date_of_year - self.dates))
        time.sleep(5)


if __name__ == "__main__" :
    def identy_card_entering() :
        id = input("Enter your identy card number :")
        while (10 > len(id)) :
            print("Invaliad Identy :(")
            id = input("Enter your identy card number")
        print("Your identy card number is {}".format(id))
        MakeIdentyCard(id)
    while (True) :
        ask = input("Do you want to repat this programme now ==> ")
        if (ask == "yes") :
            identy_card_entering()
            
myObj = MakeIdentyCard(id)
myObj.Making_identy_card()
myObj.get_month_and_date()
myObj.repeat_this_programme()