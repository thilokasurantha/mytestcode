class Car  :
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def print_details(self) :
        print(self.name)
    def print_detail(self) :
        print(self.age)

x = Car("thiloka", 23)
x2 = Car("surantha", 90) 
x.print_details()
x.print_detail()

x2.print_details()
x2.print_detail()