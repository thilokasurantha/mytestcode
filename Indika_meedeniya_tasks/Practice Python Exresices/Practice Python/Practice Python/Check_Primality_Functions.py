from divisors import *

class CheckPrimalityFunctions :
    def __init__(self,number) :
        self.number = number

    def check_primality_functions(self)  :
        myObj = Divisors(self.number)
        divs = myObj.get_divisors()
        if ((len(divs) == 1) and (divs[0] == 1)) :
            print("This prime number.")
        else :
            print("Not a prime number. ")
        
if __name__ == '__main__':
    while (True) :
        ask = input("Do you want to continue this programme >> ")
        if ((ask == "yes") or (ask == "y")) :
            genarating_number = int(input("Enter the number :"))
            myObj = CheckPrimalityFunctions(genarating_number)
            myObj.check_primality_functions()
