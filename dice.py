import random
class Dice :
    def __init__(self,random_number,dice_answer):
        self.random_number = random_number
        self.dice_answer = dice_answer

    def genarate_dice(self):
        if (self.random_number == 1) :
            self.one_side_dice()

        elif(self.random_number == 2) :
            self.two_side_dice()

        elif(self.random_number == 3) :
            self.three_side_dice()

        elif(self.random_number == 4) :
            self.four_side_dice()

        elif(self.random_number == 5) :
            self.five_side_dice()

        elif(self.random_number == 6) :
            self.six_side_dice()

    def one_side_dice(self):
        print("#"*10)

        for one in range(1,5) :
            left_align = ((10-2)-1)//2
            right_align = (10-2)-(((10-2)+1)//2)
            print("#" + " "*(10-2) + "#")

            if (one == 5//2) :
                print("#" + " "*left_align + "0" + " "*right_align + "#")

        print("#" * 10)
    def two_side_dice(self):

        print("#"*10)
        print("#0"+" "*((10-2)-1) + "#")
        print("#"+" "*(10-2) + "#")
        print("#" + " "*((10-2)-1) + "0#")
        print("#"*10)

    def three_side_dice(self):
        left_align = ((10-2)-1)//2
        right_align = (10-2)-(((10-2)+1)//2)

        print("#"*10)
        print("#0"+" "*((10-2)-1) + "#")
        print("#"+ " "*left_align + "0" + " "*right_align + "#")
        print("#" + " "*((10-2)-1) + "0#")
        print("#"*10)

    def four_side_dice(self):
        
        print("#"*10)
        print("#" + "  " + "0" + "  " + "0" + "  " +"#")
        print("#" + " "*(10-2) + "#")
        print("#" + "  " + "0" + "  " + "0" + "  " +"#")
        print("#"*10)

    def five_side_dice(self):

        left_align = ((11-2)-1)//2
        right_algn = ((11-2)-1)//2
        print("#"*11)
        print("#" + "  " + "0" + "   " + "0" + "  " +"#")
        print("#" + " "*left_align + "0" + " "*right_algn + "#")
        print("#" + "  " + "0" + "   " + "0" + "  " +"#")
        print("#"*11)

    def six_side_dice(self):

            print("#"*13)
            print("#" + "  " + "0" + "  " + "0" + "  "  + "0" + "  "+"#")
            print("#" + " "*(13-2)+ "#")
            print("#" + "  " + "0" + "  " + "0" + "  "  + "0" +"  "+"#")
            print("#"*13)

if __name__ == '__main__':
    result = "yes"
    while((result == "yes") or (result == "y")) :
        result = input("Enter do you want to repeat this programme ? ")
        random = random.randrange(1,6)
        dice_answer = input("Enter you rolling the cube ? ")
        if ((dice_answer == "yes") or (dice_answer == "y")) :
            myDice = Dice(random,dice_answer)
            myDice.genarate_dice()
    else :
        print("Bye")