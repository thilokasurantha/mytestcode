class Pallindroma :
    def __init__(self, get_word) -> None:
        self.get_word = get_word

    def check_word_simmilar(self) :
        start_checking = 0
        end_checking = -1
        #pallindrome = []

        is_pal = True

        while start_checking < len(self.get_word)/2 :
            if self.get_word[start_checking] != self.get_word[end_checking] :
                #pallindrome.append("pallindrome")
                is_pal = False
                break
            #else :
            #    pallindrome.append("not pallindrome")

            start_checking += 1
            end_checking += -1

        if (is_pal ) :
            print("This is a Pallidrome.")
        else :
            print("This is not a Pallindrome.")

if __name__ == "__main__" :
    while True :
        repeating = input("Do you want to repeat this programme again ? ")
        if repeating == "y" :
            word = input("Type the word ? ")
            myObj = Pallindroma(word)
            myObj.check_word_simmilar()

        else :
            exit()