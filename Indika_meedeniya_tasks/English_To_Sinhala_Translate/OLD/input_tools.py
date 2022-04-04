import dictionary as dicto

def input_tools() :
    word = "kaalakanniyaakaaa"

    vowels = dicto.vowels
    consonants = dicto.consonants
    symbols = dicto.symbols
    main_symbol = dicto.main_symbol

    for i in range(0, len(word)) :
        # Check First Letter Vowels
        if word[i] in vowels.keys() :
            f_vowel_letter = word[i]
            f_vowel_index = i

            if word[i+1] in vowels.keys() :
                s_vowel_letter = word[i+1]
                s_vowel_index = i+1

            elif word[i+1] in consonants.keys() :
                pass

        # Check First Letter Consonants
        elif word[i] in consonants.keys() :
            f_consonants_index = i
            f_consonants_letter = word[i]
            if len(word) == f_consonants_index+1 :
                break

            else :
                if word[f_consonants_index+1] in vowels.keys() :
                    f_vowel_nd_letter = word[i+1]
                    f_vowel_nd_index = i+1
                    print("First Letter Checked :"+str(f_vowel_nd_index))
                    if word[f_vowel_nd_index+1] in vowels.keys() :
                        f_vowel_rd_index = f_vowel_nd_index+1
                        f_vowel_rd_letter = word[f_vowel_rd_index]
                        print("Second Letter Checked : "+str(f_vowel_rd_index))
                        print(f_vowel_rd_index+1)
                        if word[f_vowel_rd_index+1] in vowels.keys() :
                            f_vowel_rth_index = f_vowel_rd_index+1
                            f_vowel_rth_letter = word[f_vowel_rth_index]
                            print("Third Letter Checked : "+str(f_vowel_rth_index))
                            generate_3_key = word[f_vowel_nd_index]+word[f_vowel_rd_index]+word[f_vowel_rth_index]
                            generate_2_key = word[f_vowel_nd_index]+word[f_vowel_rd_index]
                            print("All Keys : " + str(word[f_vowel_nd_index]))
                            if f"{generate_3_key}" in vowels.keys() :
                                pass

                            # else :
                            #     # generate_2_key = f_vowel_nd_index+f_vowel_rd_index
                            #     if f"{generate_2_key}" in vowels.keys() :
                            #         pass
                            
                            #     elif f_vowel_nd_index in vowels.keys() :
                            #         pass

                        elif word[f_vowel_rd_index+1] in vowels.keys() :
                            print("No Vowel")

                    elif word[f_vowel_nd_index+1] in consonants.keys() :
                        pass

                elif word[i+1] in consonants.keys() :
                    pass


    return word



input_tools()