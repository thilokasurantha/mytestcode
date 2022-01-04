


def create_multip(x):
    row = []
    for i in range(1,13):
        row.append(x*i)
    return row

ma =[]
for i in range (1,13):
    ma.append(create_multip(i))

for y in ma :
    print(y)


print(ma[2][4])