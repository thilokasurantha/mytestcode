from re import L


class CharackterInput(object) :
    def __init__(self, u_name, u_age) :
        self.u_name = u_name
        self.u_age = u_age

    def charackter_input(self) :
        print(f"Hey {self.u_name}, your Birth year is {2021 - self.u_age}")
        print(f"Hey {self.u_name}, your death year is {(2021 - self.u_age) + 100}")


if __name__ == '__main__':
    while (True) :
        answer = input("Do you want to repeat this programme ? ")
        if (answer == "yes") :
            name = input("Enter your name ? ")
            age = int(input("Enter your age ? "))
            myObj = CharackterInput(name, int(age))
            myObj.charackter_input()

        else :
            print("Good bye .")
            exit()