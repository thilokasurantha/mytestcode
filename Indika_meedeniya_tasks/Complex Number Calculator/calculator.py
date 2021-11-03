import re

# #x = input(">>> ")
x="12 + 36.5 + 12.5 - 22"

# a = re.compile("(\d+(\.)?\d+)|[\+\-\*\/]")
# match = a.finditer(x)
# # for b in match :
# #     group_in = b.group()
# #     print (group_in)

n_regex= r"[0-9\.\s]"

nstart=-1
for i in range(0,len(x)) :
    if (re.match(n_regex,x[i])):
        if nstart<0:
            nstart=i
            # print(i)
        # print ( x[i] + "  Is part of a number")
    else:
        # print ( x[i] + " is not number")
        current_nubmer = x[nstart:i-1]
        # print(i-1)
        # print(current_nubmer)
        print("number :"+ str(current_nubmer))
        nstart = -1


# if nstart>=0:
#     current_nubmer = x[nstart:]
#     print("number :"+ str(current_nubmer))



#     print ("i="+str(i))
#     for j in range(0,len(x)) :
#         print ("\tj="+str(j))
#     # for z in x :
#         #  print(z)
# #         for b in match :
# #             group_in = b.group()

# #             if (z[y] == group_in) :
# #                 print("Number")

# #             else :
# #                 print("Not Number")