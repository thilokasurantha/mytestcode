class number :
    def odd_or_even(self) :
        while(True) :
            genarating_number = int(input("Enter your lucky number : "))
            ask = input("Do you want to repat this programme ==> ")
            if (ask == "yes") :
                try :
                    if (genarating_number % 2 == 0) :
                        print("This is 'ODD'.")
                    else :
                        print("This is 'EVEN'.")
                except Exception:
                    print("You Type String . Please Type Inter type .")
            elif (ask == "no") :
                print("Bye")
                exit()
get_number = number()
get_number.odd_or_even()

if __name__ == '__main__':
    number(genarating_number)
