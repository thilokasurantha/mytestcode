import random
class GuessingGame :
    def __init__(self,computer_random,get_input):
        self.computer_random = computer_random
        self.get_input = get_input
    def compiling(self) :
        if (self.computer_random < self.get_input) :
            print("This is a computer random number :",self.computer_random)
            print("Your random number greater than computer random number .")
        elif (self.computer_random > self.get_input) :
            print("This is a computer random number :",self.computer_random)
            print("Your random number smaller than computer random number .")
        elif (self.computer_random == self.get_input) :
            print("This is a computer random number :", self.computer_random)
            print("Your random and computer random is Equals . ")
if __name__ == "__main__" :
    while (True) :
        random_number = random.randrange(1,10)
        user_number = input("Enter your lucky number :")
        myObj = GuessingGame(random_number,int(user_number))
        myObj.compiling()

