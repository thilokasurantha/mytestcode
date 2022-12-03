import unittest

import re

def simple_calculator_old(formula):
    a = re.compile(r'[0-9]+|[\+\-\*\/]')
    b = re.compile(r'[\+\-\*\/]')
    x = a.findall(formula)
    y = b.findall(formula)
    # print(x)
    # print(y)
    # for n in x :
    #     if n in y :
    #         f = x[x.index(n)-1]
    #         o = str(x[x.index(n)])
    #         l = x[x.index(n)+1]

    #         print("Theory is ==>>" ,"(" + f + " : " + o + " : " + l + ")")

    #         dicto = {
    #             '+' : int(f) + int(l) ,
    #             '-' : int(f) - int(l) ,
    #             '*' : int(f) * int(l) ,
    #             '/' : int(f) // int(l)
    #         }
    #         print("Answer is ==>> ",dicto[o])
    #         f = int(dicto[o])
    print(y)
    cur = 0
    while (cur <= len(x)) :
         if cur < len(x) and x[cur] in y :
             f = int(x[cur-1])
             o = x[cur]
             l = int(x[cur+1])
             fidx = cur-1
             lidx = cur+1
             dicto = {
                 '+' : int(f) + int(l) ,
                 '-' : int(f) - int(l) ,
                 '*' : int(f) * int(l) ,
                 '/' : int(f) // int(l)
             }
             print("Answer is ==>> ",dicto[o])
             del x[fidx:lidx+1]
             x.insert(0, dicto[o])
             cur = 0
         else :
             cur += 1
    return dicto[o]



# def simple_calculations(formula) :
    # x = formula
    # y = ["+","-","*","/"]
    # cur = 0
    # while (cur <= len(x)) :
    #     if cur < len(x) and x[cur] in y :
    #         f = int(x[cur-1])
    #         o = x[cur]
    #         l = int(x[cur+1])
    #         fidx = cur-1
    #         lidx = cur+1

    #         dicto = {
    #             '+' : int(f) + int(l) ,
    #             '-' : int(f) - int(l) ,
    #             '*' : int(f) * int(l) ,
    #             '/' : int(f) // int(l)
    #         }
    #         print("Answer is ==>> ",dicto[o])

    #         del x[fidx:lidx+1]
    #         x.insert(0, dicto[o])
    #         cur = 0

    #     else :
    #         cur += 1

    # return dicto[o]


    
def calculator(prob) :
    operators = ["+","-","*","/"]
    f_brackets = []
    l_brackets = []
    numbers = []
    empty = []
    dis1 = 0
    dis2 = 1
    dis3 = 0
    ls = 0

    in_brkt = []

    while (dis1 <= len(prob)) :
        if (dis1 == len(prob)) :
            dis1 = 0
            break

        elif ((dis1 < len(prob)) and (prob[dis1] in "(")) :
            f_brackets.append(dis1)
            dis1 += 1

        elif ((dis1 < len(prob)) and (prob[dis1] in ")")) :
            l_brackets.append(dis1+1)
            dis1 += 1

        else :
            dis1 += 1

    for i,j in zip(f_brackets, l_brackets) :
            cato = prob[i+1:j]
            in_brkt.append(cato)

    while (dis2 <= len(in_brkt[dis3])) :
        if (dis2==len(in_brkt[dis3])) :
            simple_calculations(numbers[-1])
            dis3 += 1
            if dis3 < len(in_brkt) :
                if (in_brkt[dis3]) :
                    dis1 = 0
                    dis2 = 0

            else : 
                break

        elif ((dis2<len(in_brkt[dis3])) and ((in_brkt[dis3][dis2] in operators))) :
            numbers.append([])
            numbers[ls].append(in_brkt[dis3][dis1:dis2])
            numbers[ls].append(in_brkt[dis3][dis2:dis2+1])
            dis1 = dis2
            dis2 += 1

        elif ((dis2<len(in_brkt[dis3])) and (in_brkt[dis3][dis2] in ")")) :
            numbers[ls].append(in_brkt[dis3][dis1+1:dis2])
            dis1 = dis2+1
            dis2 += 1
            ls += 1

        else :
            dis2 += 1

    print(numbers)

class Tester(unittest.TestCase):
    
    def test_01(self):
        self.assertEqual(simple_calculator_old("3+2"),5)

    def test_02(self):
        self.assertEqual(simple_calculator_old("13+22"),35)

    def test_03(self):
        self.assertEqual(simple_calculator_old("3*2+12"),18)

    def test_04(self):
        self.assertEqual(simple_calculator_old("3*2/6"),1)

    def test_05(self):
        self.assertEqual(simple_calculator_old("3+2+10"),15)    


if __name__ == "__main__" :
   # problem = "(12+13)+5(12+20)/2+(3260*20/5)"
    # problem = "12*4"
    # simple_calculations(problem)
    # myObj = calculator(problem)
#
    # 12+5
    # 12 + 21 - 8
    # 32.5 - 11 + 3
    # 3*21 + 8

    unittest.main()
    # simple_calculations("12+13*25+5")