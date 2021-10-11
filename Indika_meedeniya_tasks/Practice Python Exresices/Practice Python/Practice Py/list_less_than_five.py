class ListLessThanFive :
    def __init__(self, chk_list) :
        self.chk_list = chk_list

    def list_less_than_five(self) :
        for self.catogorising in self.chk_list :
            if (self.catogorising < 5) :
                print(self.catogorising)
if __name__ == '__main__':
    a = [1,2,2,3,4,3,5,6,7,8,9,10]

    myObj = ListLessThanFive(a)
    myObj.list_less_than_five()