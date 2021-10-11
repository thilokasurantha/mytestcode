class StringList(object) :
    def __init__(self, usr) :
        self.usr = usr

    def string_list(self) :
        print(self.usr.sort(reverse=True))
if __name__ == '__main__':
    user = input("Enter word ? ")
    myString = StringList(user)
    myString.string_list()