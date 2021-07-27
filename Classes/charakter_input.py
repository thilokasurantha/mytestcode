user_name = input("Enter your name :")
user_age = int(input("Enter your age :"))
class name_and_age :
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def charackter_input(self):
        print("Hey {} Your birth year is : {}".format(self.name,2021-self.age))
        print("Hey {} your 100 years old : {}".format(self.name,self.age+100))
get_input = name_and_age(user_name, user_age)
get_input.charackter_input()

if __name__ == '__main__':
    name_and_age(user_name,user_age)