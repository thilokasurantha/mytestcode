num_1 = 1
num_2 = 2

fib = []
fib.append(num_1)
fib.append(num_2)

index = 0

while (len(fib)<8) :
    fib.append(fib[index] + fib[index +1])
    index = index +1

print(fib)


# def fab(n):
#     arr =[]
#     arr.append(1)
#     arr.append(2)
#     for i in range(2,n) :
#         #print (str(arr) + " i=" + str(i))
#         arr.append(arr[i-2] + arr[i-1])

#     return arr

# print(fab(25))

