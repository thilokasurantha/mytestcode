a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []

for ai in a :
    found = False
    for ci in common  :
        if (ai == ci) :
            found = True
            break
        if common :
            continue
        for bi in b :
                if (ai == bi) :
                    common.append(bi)
            
print(common)
