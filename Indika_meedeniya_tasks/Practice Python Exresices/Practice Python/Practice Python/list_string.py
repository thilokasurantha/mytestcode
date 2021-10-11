user_input = int(input("Enter your lucky number :"))
class main_class :
    def __init__(self,number) :
        self.user = number
    def list_commpherisions(self) :
        common = []
        for loops in str(self.user) :
            common.append(loops)
        print(common)
        common.sort(reverse=True)
        print(common)
myObj = main_class(user_input)
myObj.list_commpherisions()
if __name__ == '__main__':
    main_class