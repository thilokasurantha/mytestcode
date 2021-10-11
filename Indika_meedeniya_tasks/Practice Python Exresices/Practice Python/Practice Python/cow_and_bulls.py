import random
class CowAndBulls :
    def __init__(self,random_num,user_num) :
        self.random = random_num
        self.number = user_num

    def cow_and_bulls_game(self) :
        cows = 0
        bulls = 0
        for self.check_random in range(0,len(self.random)) :
            for self.check_number in range(0,len(self.number)) :
                if (self.random[self.check_random] == self.number[self.check_number]):
                    if (self.check_random == self.check_number) :
                        length = len(str(self.check_random))
                        x = []
                        x.append(int(length))
                        print(x)
                        print("You have {} cows .".format(length))

if __name__ == '__main__':
    genarating_random_number = str(random.randrange(1000,9999))
    print(genarating_random_number)
    user_number = input("Enter your favourite number :")
    myObj = CowAndBulls(str(genarating_random_number),str(user_number))
    myObj.cow_and_bulls_game()
