class loops :
    def __init__(self):
        self.number = 0
    def user_number(self):
        while(self.number < 100) :
            self.number += 1
            print(self.number)
        print("This programme will be ended .")
number_get = loops()
number_get.user_number()

if __name__ == '__main__':
    loops()