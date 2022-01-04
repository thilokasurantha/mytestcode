import random

class Dice :
    def __init__(self):

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

    def roll(self):
        n = random.randrange(1,7)
        self.draw_dice(n)

    def draw_line(self):
        print("#"*9)


    def draw_dice(self,n):
        print(n)
        self.draw_line()
        print(self.first_row.get(n))
        print(self.second_row.get(n))
        print(self.third_row.get(n))
        self.draw_line()



if __name__ == '__main__':
    print("This is a random Cude Game")
    print("__________________________ \n\n")

    myDice = Dice()
    result = input("Roll Dice (y/n) ?")
    while(result == "yes" or result == "y") :
        myDice.roll() 
        result = input("Roll Dice (y/n) ? ")

    print("Bye")
