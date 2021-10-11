number_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
class Compherisons :
    def __init__(self,number) :
        self.compare = number
    def list_commpherisions(self) :
        for columns_by_columns in self.compare :
            if (columns_by_columns % 4 == 0) :
                print(columns_by_columns)
myObj = Compherisons(number_a)
myObj.list_commpherisions()
if __name__ == '__main__':
    Compherisons