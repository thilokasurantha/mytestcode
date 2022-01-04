genarating_number = int(input("Enter your lucky number :"))
class number :
    def __init__(self,number):
        self.number = number
    def odd_or_even(self) :
            if (self.number % 2 == 0) :
                print("This is 'ODD'.")
            else :
                print("This is 'EVEN'.")
get_number = number(genarating_number)
get_number.odd_or_even()

if __name__ == '__main__':
    number(genarating_number)
