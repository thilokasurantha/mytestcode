

# l1 = [2,3,4,5]
# l2 = []
# l = len(l1)-1

# while l 




def extract_reverse_number(arr) :
    s = ""

    for i in range(1,len(arr)+1) :
        s = s + str(arr[-1*i])
    return int(s)

def add_two_numbers(l1, l2) :
    n1 = extract_reverse_number(l1)
    n2 = extract_reverse_number(l2)

    return n1 + n2

result = add_two_numbers([2,4,3],[5,6,4])
print(result)
