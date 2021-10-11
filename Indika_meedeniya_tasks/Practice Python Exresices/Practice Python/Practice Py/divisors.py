class Divisors :
    def __init__(self, get_number) :
        self.g_num = get_number

    def divisors(self) :
        self.common = []
        for self.get_lst in range(1,self.g_num) :
            if (self.get_lst % 2 == 0) :
                self.common.append(self.get_lst)
                print(self.common)

if __name__ == '__main__':
    number = int(input("Enter your number ? "))
    myObj = Divisors(int(number))
    myObj.divisors()