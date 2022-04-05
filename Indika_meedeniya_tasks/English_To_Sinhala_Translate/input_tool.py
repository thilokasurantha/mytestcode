import dictionary 

def input_tools(word) :
    print(word)

    vowels = dictionary.vowels
    consonants = dictionary.consonants
    symbols = dictionary.symbols

    for x in range(0, len(word)) :
        if word[x] in vowels.keys() :
            f_vwl_letter = word[x]
            f_vwl_index = x

            if word[f_vwl_index+1] in vowels.keys() :
                s_v_vwl_letter = word[f_vwl_index+1]
                s_v_vwl_index = f_vwl_index+1
                print("Index : "+str(s_v_vwl_index))
                if word[s_v_vwl_index+1] in vowels.keys() :
                    t_v_vwl_letter = word[s_v_vwl_index+1]
                    t_v_vwl_index = s_v_vwl_index+1

                    if word[t_v_vwl_index+1] in vowels.keys() :
                        f_v_vwl_letter = word[t_v_vwl_index+1]
                        f_v_vwl_index = t_v_vwl_index+1

                        if word[f_v_vwl_index+1] in consonants.keys() :
                            vowel_w = word[f_vwl_index: f_vwl_index+1]

                    elif word[t_v_vwl_index+1] in consonants.keys() :
                        f_v_con_letter = word[t_v_vwl_index+1]
                        f_v_con_index = t_v_vwl_index+1

                elif word[s_v_vwl_index+1] in consonants.keys() :
                    t_v_con_letter = word[s_v_vwl_index+1]
                    t_v_con_index = s_v_vwl_index+1

            elif word[f_vwl_index+1] in consonants.keys() :
                s_v_con_letter = word[f_vwl_index+1]
                s_v_con_index = f_vwl_index+1

        elif word[x] in consonants.keys() :
            f_con_letter = word[x]
            f_con_index = x

            if word[f_con_index+1] in consonants.keys() :
                s_c_con_letter = word[f_con_index+1]
                s_c_con_index = f_con_index+1

                if word[s_c_con_index+1] in vowels.keys() :
                    conso_w = word[f_con_index : s_c_con_index+1]

            elif word[f_con_index+1] in vowels.keys() :
                s_c_vwl_letter = word[f_con_index+1]
                s_c_vwl_index = f_con_index+1




if __name__ == "__main__" :
    word = "kaalakanniyaa"

    myObj = input_tools(word)