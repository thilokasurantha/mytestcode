import re

def simple_calculations(get_prob) :
    bodmas = ["/", "*", "+", "-"]
    get_prob.remove(")")
    cur = 0
    dis = 0
    while ((len(get_prob)>=cur)) :
        if bodmas[dis] in get_prob :
            f = int(get_prob[get_prob.index(bodmas[dis])-1])
            o = get_prob[get_prob.index(bodmas[dis])]
            l = int(get_prob[get_prob.index(bodmas[dis])+1])
            fidx = get_prob.index(bodmas[dis])-1
            lidx = get_prob.index(bodmas[dis])+1
            dicto = {
                '+' : int(f) + int(l) ,
                '-' : int(f) - int(l) ,
                '*' : int(f) * int(l) ,
                '/' : int(f) // int(l)
            }
            del get_prob[fidx:lidx+1]
            print("Answer IS >>>>", dicto[o])
            get_prob.insert(fidx, dicto[o])
            print("LENTH >>>>", len(get_prob))
            cur = 0
            if ((len(get_prob)<cur)) :
                dis = 0

            else :    
                dis += 1

        
        elif bodmas[dis] not in get_prob  :
            cur += 1
            dis += 1

        elif len(bodmas) < dis :
            dis += 0

        else :
            dis = 0
            cur = 0
            break

    return dicto[o]


def catogorising(prob) :
    re_exp_1 = re.compile(r'[0-9]+|[\+\-\*\/\(\)]')
    li_all = re_exp_1.findall(prob)
    starting_braket = []
    ending_braket = []
    t= []
    cur_s = 0
    cur_e = -1
    li_e = len(li_all)-1

    while ((len(li_all)>=cur_s)) :
        if (len(li_all)>cur_s) and ("(" in li_all[cur_s]) :
            starting_braket.append(cur_s)
            cur_s += 1

        else :
            cur_s += 1

    while (-(len(li_all))+(-1)<=cur_e) :
        if (-(len(li_all))<=cur_e) and (")" in li_all[cur_e]) :
            t.append(cur_e)
            x = cur_e-(-1)
            y = x + li_e
            ending_braket.append(y)
            cur_e = cur_e+(-1)

        else :
            cur_e = cur_e+(-1)
    print(li_all)
    print(str(starting_braket) + " " + str(ending_braket))

    for i,j in zip(starting_braket, reversed(ending_braket)) :
        result = li_all[i+1:j+1]
        update = simple_calculations(result)
        print(update)

if __name__ == "__main__" :
    problem = "12+13+14+(12+10/5*4)"
    catogorising(problem)