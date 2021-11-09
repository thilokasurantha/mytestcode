get_input = "12+12+12+12/3.55"
operator = ['+','-','*','/']

get_operator = []
get_number = []


over = 0
for x in range(0,len(get_input)) :
    if get_input[x] in operator :
        get_o_index = x
        numbers = get_input[over:get_o_index]
        over = get_o_index+1
        get_number.append(numbers)
        get_operator.append(get_input[x])

get_last_index = get_input[get_o_index+1:len(get_input)]
get_number.append(get_last_index)
print(get_number)
print(get_operator)