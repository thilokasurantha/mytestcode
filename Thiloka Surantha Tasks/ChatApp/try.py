class name:
    def __init__(self) -> None:
        self.name = "thiloka"

class age(name) :
    def __init__(self) -> None:
        super().__init__()

    def printname(self) :
        print(self.name)


my = age()
x= my.printname()
print(x)