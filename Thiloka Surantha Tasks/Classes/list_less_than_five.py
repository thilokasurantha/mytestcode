a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
class list_number :
    def __init__(self,number) :
        self.number = number
    def list_less_than_five(self):
        for x in self.number :
            if (x < 8) :
                print(x)
get_class = list_number(a)
get_class.list_less_than_five()

if __name__ == '__main__':
    list_number(a)