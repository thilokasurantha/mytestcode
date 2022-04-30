import sqlite3
import dictionary
# get current letter i  (1)
# if vowel -> 
#     check including next letter (2)
#     if volwel -> check including next letter (3)
#         if volwel -> check including next letter (4)
#             convert[i,i+4] lookup in volwels
#             i+=4
#         else
#             convert[i,i+3] lookup in volwels
#             i+=3
#     else
#         convert[i,i+2] lookup in volwels
#             i+=2

#     else :
#         convert[i,i+1] lookup in volwels
#         i+=1
# else



class SinhalaConverter :
    def __init__(self) -> None:
        self.vowels = dictionary.vowels
        self.consonants = dictionary.consonants
        self.symbols = dictionary.symbols

    def generate_sinhala_word(self, word) :
        # for x in range(0, len(word)) :
        #     first_index = x
        #     try :
        #         if word[x] in self.consonants.keys() :
        #             first_conso_conso_letter = word[x]
        #             first_conso_conso_index = x
        #             print("FIRST CONSO CONSO LETTER : ",first_conso_conso_letter)

        #             if word[first_conso_conso_index+1] in self.consonants.keys() :
        #                 second_conso_conso_letter = word[first_conso_conso_index+1]
        #                 second_conso_conso_index = first_conso_conso_index+1

        #                 check_two_letters = DatabaseHandler().database_handler(word[first_conso_conso_index:second_conso_conso_index+1])
        #                 print("THAT HAS TWO LETTER : ", check_two_letters)

        #         elif self.word[x] in self.vowels.keys() :
        #             first_conso_vowel_letter = self.word[x]
        #             first_conso_vowel_index  = x

        #             print("FIRST CONSO VOWEL LETTER :",first_conso_vowel_letter)

        #     except :
        #         exit()
        cur = 0
        res = ""
        while (cur < len(word)) :
            if word[cur] in self.vowels.keys() :
                if (cur+1 < len(word)) and word[cur:cur+2] in self.vowels.keys() :
                    res = res+self.vowels.get(word[cur:cur+2])
                    cur += 2
                else :
                    res = res+self.vowels.get(word[cur])
                    cur += 1
         # first letter is a consonent
            elif word[cur] in self.consonants.keys() :
                if (cur+1 < len(word)) and word[cur+1] in self.vowels.keys() :
                    if (cur+2 < len(word)) and word[cur+2] in self.vowels.keys() :
                        res = res+self.consonants.get(word[cur])+self.symbols.get(word[cur+1 : cur+3])
                        cur += 3

                    else :
                        res = res+self.consonants.get(word[cur])+self.symbols.get(word[cur+1])
                        cur += 2
                else : # Hal kirima
                    res = res+self.consonants.get(word[cur])+self.symbols.get("h")
                    cur += 1
                
            else :
                cur+=1
        return res
        





# class DatabaseHandler :
#     def __init__(self) -> None:
#         self.connect = sqlite3.connect("dictionary.db")
#         self.cursor = self.connect.cursor()

#     def database_handler(self, ranges) :
#         get_values = self.cursor.execute("SELECT conso_key FROM consonants WHERE conso_key = (?)", (ranges,))
#         get_items = get_values.fetchall()

#         for n in get_items :
#             return n[0]


if __name__ == "__main__" :
    words = str(input("Enter your word : "))
    myObj = SinhalaConverter()
    res = myObj.generate_sinhala_word(words)
    print(res)