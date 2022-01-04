over = 0
get = "12+12+12+12+3213123132133123" 
o = ['+','-','*','/','(',')']
ope = []
num = []

for x in range(0, len(get)) :
    if get[x] in o :
        li = x
        ope.append(get[x])

        number = get[over:li]
        over = li+1

        num.append(number)

if over > 0 :
    num.append(get[over:len(get)])


print(num)
print(ope)


# if '' in num :
#     num.remove('')

# print(num)
# print(ope)

# a = 0
# b = 0
# c = 1

# f = num[a]
# o = ope[b]
# all = []

# while c < len(num) :
#     dicto = {
#         "+" : int(f) + int(num[c]),
#         "-" : int(f) - int(num[c]),
#         "*" : int(f) * int(num[c]),
#         "/" : int(f) // int(num[c]),
#         "(" : int(f) * int(num[c]),
#     }

#     answer = dicto[ope[b]]
#     f = answer
#     b += 1
#     c += 1


#     all.append(answer)

# print(all[-1])

