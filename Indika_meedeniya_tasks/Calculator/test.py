import re

while True:
    user = input("bash >> ")
    
    all = re.compile(r'[0-9]+|[\+\-\*\/]')
    f_all = all.findall(user)
    
    f = 0
    o = 1
    l = 2
    x = f_all[f]
    n = 0
    empty = []
    while l <= len(f_all):
        dt = {
            "+" : int(x) + int(f_all[l]) ,
            "-" : int(x) - int(f_all[l]) ,
            "*" : int(x) * int(f_all[l]) ,
            "/" : int(x) //int( f_all[l]) ,
        }
        ans = dt[f_all[o]]
        x =  ans
        o += 2
        l += 2
        n += 1
        
        empty.append(ans)
        
    print(f"{user} = {empty[-1]}")

