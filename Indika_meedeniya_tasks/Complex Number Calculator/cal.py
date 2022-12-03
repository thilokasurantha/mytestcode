import unittest
import re

class SimpleCalculations :
    def simple_calculations(self, formula) :
        # a = re.compile(r'[0-9]+|[\+\-\*\/]')
        # b = re.compile(r'[\+\-\*\/]')
        # x = a.findall(formula)
        # y = b.findall(formula)
        # print(y)
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
        #         del x[fidx:lidx+1]
        #         x.insert(0, dicto[o])
        #         cur = 0
        #     else :
        #         cur += 1
        # return dicto[o]



    while ((cur <= len(x)) or (dis <= len(y))) :
        if cur < len(x) and  y[dis] in x:
            f = int(x[cur-1])
            print("F = {}".format(x[cur-1]))
            o = x[cur]
            print("O = {}".format(x[cur]))
            l = int(x[cur+1])
            print("L = {}".format(x[cur+1]))
            fidx = cur-1
            lidx = cur+1
            dicto = {
                '+' : int(f) + int(l) ,
                '-' : int(f) - int(l) ,
                '*' : int(f) * int(l) ,
                '/' : int(f) // int(l)
            }
            del x[fidx:lidx+1]
            x.insert(0, dicto[o])
            print(x[0])
            cur = 0
            dis += 1
        else :
                cur += 1

                
    return dicto[o]


class HardCalculations :
    pass

class Test(unittest.TestCase) :
    def test_01(self) :
        self.assertEqual(SimpleCalculations().simple_calculations("12+13+14/3"),13)

    def test_02(self) :
        self.assertEqual(SimpleCalculations().simple_calculations("12+13+14+15*34"),1836)


if __name__ == "__main__" :
    SimpleCalculations().simple_calculations("12+13+14+(12*5)/(5+6)/(1321312312313323+23213123+213131332)")

