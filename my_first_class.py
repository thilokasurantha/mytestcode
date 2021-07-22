class myclass :
    def __init__(self):
        self.a = 0
    def loops(self):
        while(self.a < 20) :
            self.a += 1
            print(self.a)

        print("Thank you very much")
p1 = myclass()
print(p1.loops())