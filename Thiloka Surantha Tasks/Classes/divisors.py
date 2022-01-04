get_user_number = int(input("Enter the number ==>> "))
class division :
    def __init__(self,number) :
        self.number = number
    def divisors(self) :
        common = []
        for x in range(1,self.number) :
            if (self.number % x == 0) :
                common.append(x)
        print(common)
get_number = division(get_user_number)
get_number.divisors()

if __name__ == '__main__':
    division(get_user_number)