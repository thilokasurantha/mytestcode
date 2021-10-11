class NameAndAge :
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def charackter_input(self):
        print("Hey {} Your birth year is : {}".format(self.name,2021-self.age))
        print("Hey {} your 100 years old : {}".format(self.name,self.age+100))


if __name__ == '__main__':
    user_name = input("Enter your name :")
    user_age = int(input("Enter your age :"))
    myObj = NameAndAge(user_name, user_age)
    myObj.charackter_input()
