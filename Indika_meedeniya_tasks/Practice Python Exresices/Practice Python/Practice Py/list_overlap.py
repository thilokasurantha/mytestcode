class ListrOverlap :
    def __init__(self,a,b) :
        self.a = a
        self.b = b

    def list_overlap(self) :
        a_set = set(self.a)
        b_set = set(self.b)
        common = []
        for ai in a_set :
            for bi in b_set :
                if (ai == bi) :
                    common.append(bi)
        print(common)

if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    myList = ListrOverlap(a,b)
    myList.list_overlap()