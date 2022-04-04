import dictionary as dicto

def input_tools(word) :
    word = word
    vowels = dicto.symbols
    consonants = dicto.consonants
    symbols = dicto.symbols

    for x in range(0, len(word)) :
        if word[x] in vowels.keys() :
            F_VWL_LTR = word[x]
            F_VWL_ID = x

            if word[F_VWL_ID+1] in vowels.keys() :
                S_VWL_LTR = word[F_VWL_ID+1]
                S_VWL_ID = F_VWL_ID+1

                if word[S_VWL_ID+1] in vowels.keys() :
                    RD_VWL_LTR = word[S_VWL_ID+1]
                    RD_VWL_ID = S_VWL_ID+1

                    if word[RD_VWL_ID+1] in vowels.keys() :
                        RTH_VWL_LTR = word[RD_VWL_ID+1]
                        RTH_VWL_ID = RD_VWL_ID+1

                    elif word[RD_VWL_ID+1] in consonants.keys() :
                        pass


                elif word[S_VWL_ID+1] in consonants.keys() :
                    pass

            elif word[F_VWL_ID+1] in consonants.keys() :
                pass

        elif word[x] in consonants.keys() :
            F_CONS_LTR = word[x]
            F_CONS_ID = x

            if word[F_CONS_ID+1] in consonants.keys() :
                pass

            elif word[F_CONS_ID+1] in vowels.keys() :
                END_CONSO_ID = F_CO
                BIND_CONSO = word[F_CONS_ID : ]


if __name__ == "__main__" :
    word = "kaalakanniya"

    input_tools(word)