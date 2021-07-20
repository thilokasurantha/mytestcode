#  Identity card number check program
# Find birth date from id


id = input("Enter Your Identy Card Number :")
print("Your Identy Card Is :"+ id )

# advanced ..................................................................
year = id[0:2]
second_3 = id[2:5]
rest = id[0:9]


print ("Your year of birth", year)

second_3_int = int(second_3)
if second_3_int > 500:
	print ("You are female")
else:
	print ("You are male")



# def thiloka_function():
#     print("Your Year IS : 19" + l)
#     if (m > "500"):
#         print("You Are Female")
#     else :
#         print("You Are male")
##
#
#

#def identy_card():
#    if (x != o):
#        print("Thast Wrong !!!")
#
#    elif ((x == o) or (x == p)):
        print("Lets Go To The Next Step !!!! ")
#    else:
#        print("Try Again !!!")

#identy_card()
#thiloka_function()
