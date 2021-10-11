import emoji
import time
class RockPaperScissor :
    def __init__(self,name_1,name_2) :
        self.user_person_1 = name_1
        self.user_person_2 = name_2
    def rock_paper_scissor_game(self):
        print("{} Attension Please {}".format("="*10 , "="*10))
        items = ["1 : Rock","2 : Paper","3 : Scissor"]
        for index in items :
            print(index)
        self.user_game_1 = input("Hey {} this is your turn ==>> ".format(self.user_person_1))
        self.user_game_2 = input("Hey {} this is your turn ==>> ".format(self.user_person_2))

        if ((self.user_game_1 == "rock") and (self.user_game_2 == "rock")) :
            print("This game is equals .")
        elif ((self.user_game_1 == "rock") and (self.user_game_2 == "paper")) :
            print("The paper covered the stone")
        elif((self.user_game_1 == "rock") and (self.user_game_2 == "scissor")) :
            print("Scissors broken from the stone")
        elif ((self.user_game_1 == "paper") and (self.user_game_2 == "paper")) :
            print("This game is equals .")
        elif ((self.user_game_1 == "paper") and (self.user_game_2 == "rock")) :
            print("The paper covered the stone")
        elif((self.user_game_1 == "paper") and (self.user_game_2 == "scissor")) :
            print("Scissors broken from the stone")
        else :
            print("That has no named .")
        
        
if __name__ == '__main__':
    while(True) :
        ask_from_user = input("Do you want to repeat this prgramme ? ")
        if ((ask_from_user == "yes") or (ask_from_user == "y")) :
            user_1 = input("Enter your name ==>> ")
            user_2 = input("Enter your name ==>> ")
            myObj = RockPaperScissor(user_1,user_2)
            myObj.rock_paper_scissor_game()
        else :
            count = 0
            while (count < 10) :
                count += 1
                time.sleep(1)
                print("This programme is now be closed . "+str((count / 100)*100))
            


