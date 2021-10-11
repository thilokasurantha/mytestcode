class OddOrEven :
    def __init__(self,u_number) :
        self.u_num = u_number

    def odd_or_even(self) :
        if (self.u_num % 2 == 0) :
            print("This is 'ODD'")
        
        else :
            print("This is 'EVEN'")
            
if __name__ == '__main__':
    while (True) :
        answer = input("Do you want to repeat this programme ? ")
        if (answer == "yes") :
            number = int(input("Enter the number ? "))

            myObj = OddOrEven(int(number))
            myObj.odd_or_even()

        else :
            print("Bye")
            exit()