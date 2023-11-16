# # import math
# # a = "7.666666666666667"
# # x = list(a)
# # [print(x)]

# def scientific_number(num) :
#     x = str(num)
#     y = x.index(".")
#     del x[y+1:len(x)-1]
#     print(x)

# scientific_number(7.6666666667778)

import nltk

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)