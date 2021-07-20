def list_less_than_five():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    i = 0
    list_1 = []
    while (5 >= a[i]):
        i = i+1
        list_1.append(i)
    print(list_1)
    return i+1
list_less_than_five()