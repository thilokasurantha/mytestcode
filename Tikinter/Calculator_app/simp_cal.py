import re
def simple_calculations(get_prob) :
    bodmas = ["/", "*", "+", "-"]
    if ")" in get_prob :
        get_prob.remove(")")
    
    else :
        pass
    cur = 0
    dis = 0
    while (len(get_prob)>=cur) :
        if bodmas[dis] in get_prob :
            f = float(get_prob[get_prob.index(bodmas[dis])-1])
            o = get_prob[get_prob.index(bodmas[dis])]
            l = float(get_prob[get_prob.index(bodmas[dis])+1])
            fidx = get_prob.index(bodmas[dis])-1
            lidx = get_prob.index(bodmas[dis])+1
            dicto = {
                '+' : float(f) + float(l) ,
                '-' : float(f) - float(l) ,
                '*' : float(f) * float(l) ,
                '/' : float(f) / float(l)
            }
            del get_prob[fidx:lidx+1]
            get_prob.insert(fidx, dicto[o])
            if len(get_prob) == 1 :
                break

            elif bodmas[dis] in get_prob :
                continue
            else :    
                dis += 1

        elif bodmas[dis] not in get_prob :
            dis += 1
        
    return dicto[o]


def catogorising(prob) :
    re_exp_1 = re.compile(r'[0-9]+|[\+\-\*\/\(\)]')
    li_all = re_exp_1.findall(prob)
    starting_braket = []
    ending_braket = []
    t = []
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

    fid_li = []
    lid_li = []
    brkt_solv = []
    for i,j in zip(starting_braket, reversed(ending_braket)) :
        result = li_all[i+1:j+1]
        update = simple_calculations(result)
        fid_li.append(i)
        lid_li.append(j+1)
        brkt_solv.append(str(update))
        print(update)

    del li_all[fid_li[0]+1:lid_li[0]]
    distance = lid_li[0]-(fid_li[0]+1)
    li_all[fid_li[0]] = str(brkt_solv[0])
    del brkt_solv[0]
    del fid_li[0]
    del lid_li[0]

    f_1 = []
    for x,y in zip(fid_li, lid_li):
        x = (x+1)-distance
        y = y-distance
        del li_all[x:y]
        new_dis = y-x
        distance = distance+new_dis
        f_1.append(x)

    n = 0
    for x in range(0, len(li_all)) :
        if "(" in li_all[x] :
            li_all[x] = brkt_solv[n]
            if len(brkt_solv) < n :
                break

            else :
                n += 1

    answer = simple_calculations(li_all)
    scie_num = scientific_number(answer)
    return scie_num

def scientific_number(num) :
    x = list(str(num))
    y = x.index(".")
    del x[y+2:len(x)-1]
    res = ""
    for n in x : 
        res += n
    return res
    
if __name__ == "__main__" :
    while (True) :
        problem = str(input("ENTER THE CALCULATION >> "))
        if "(" in problem :
            x = catogorising(problem)
            print("THE ANSWER IS >>> {}".format(x))

        else :
            re_exp_1 = re.compile(r'[0-9]+|[\+\-\*\/\(\)]')
            li_all = re_exp_1.findall(problem)
            answer = simple_calculations(li_all)
            scie_num = scientific_number(answer)
            print("THE ANSWER IS >>> {}".format(scie_num))