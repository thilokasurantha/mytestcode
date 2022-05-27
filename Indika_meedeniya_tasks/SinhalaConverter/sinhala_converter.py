import dictionary

class SinhalaConverter :
    def __init__(self) -> None:
        self.vowels = dictionary.vowels
        self.consonants = dictionary.consonants
        self.symbols = dictionary.symbols

    def generate_word(self, word) :
        cur = 0
        result = ""

        while (cur <= len(word)) :
            if word[cur] in self.consonants.keys() :
                if word[cur+1] in self.consonants.keys() :
                    print("Y")

            else :
                print("N")

if __name__ == "__main__" :
    word = "prabhashansleshanaya"

    myObj = SinhalaConverter()
    myObj.generate_word(word)
        