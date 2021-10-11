class Divisors :
    def __init__(self,number) :
        self.number = number
    def get_divisors(self) :
        common = []
        for x in range(1,self.number) :
            if (self.number % x == 0) :
                common.append(x)
        print(common)
        return common


# if __name__ == '__main__':
#     # get_user_number = int(input("Enter the number ==>> "))
#     # myObj = Divisors(get_user_number)
    # myObj.get_divisors()