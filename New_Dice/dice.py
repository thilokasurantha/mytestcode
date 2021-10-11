import random

class Dice :
    def __init__(self,random_number):
        self.random_number = random_number

        self.first_row = {
            1: "#       #",
            2: "# 0     #",
            3: "# 0     #",
            4: "# 0   0 #",
            5: "# 0   0 #",
            6: "# 0 0 0 #"
        }

        self.second_row = {
            1: "#   0   #",
            2: "#       #",
            3: "#   0   #",
            4: "#       #",
            5: "#   0   #",
            6: "#       #"      
        }

        self.third_row = {
            1: "#       #",
            2: "#     0 #",
            3: "#     0 #",
            4: "# 0   0 #",
            5: "# 0   0 #",
            6: "# 0 0 0 #"   
        }

    def draw_line(self):
        print("#"*9)


    def draw_dice(self):
        print(self.random_number)
        self.draw_line()
        print(self.first_row.get(self.random_number))
        print(self.second_row.get(self.random_number))
        print(self.third_row.get(self.random_number))
        self.draw_line()

def roll_dice():
    genarate_random = random.randrange(1,7)
    myDice = Dice(genarate_random)
    myDice.draw_dice()

if __name__ == '__main__':
    print("This is a random Cude Game")
    print("__________________________ \n\n")
    result = input("Roll Dice (y/n) ?")
    while(result == "yes" or result == "y") :
        roll_dice() 
        result = input("Roll Dice (y/n) ? ")

    print("Bye")
