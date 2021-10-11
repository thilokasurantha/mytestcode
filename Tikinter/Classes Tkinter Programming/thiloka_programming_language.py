import math
class MakeProgrammingLanguageOperatorsUsing :
    def shell(self) :
        print("Python 3.9.5 (tags/v3.9.5: 0a7dcbd, May  3 2021, 17: 27: 52)[MSC v.1928 64 bit(AMD64)] on win32 Type 'help', 'copyright', 'credits' or 'license' for more information.")
        while (True) :
            self.bash = input(">>> ")
            self.into_the_list()
            self.variables()
            self.operators()
    def into_the_list(self) :
        self.bash_code = self.bash.split()
        self.fisrt_index = self.bash_code[0]
        self.moddle_index = self.bash_code[1]
        self.last_index = self.bash_code[2]

    def variables(self) :
        self.TH_ADDTION = "+"
        self.TH_SUBSTRACTION = "-"
        self.TH_MULTIPLYCATION = "*"
        self.TH_DIVISION = "/"
        self.TH_EQUALANCI = "="
        self.TH_FLOOR_DIVISION = "//"
        self.TH_SQRT_FIRST = "sqrt"
        self.TH_SQRT_LAST = "()"
        self.TH_DICT = "da"
    def operators(self) :
        if (self.moddle_index == self.TH_ADDTION) :
            print(int(self.fisrt_index) + int(self.last_index))

        elif (self.moddle_index == self.TH_DICT) :
            self.get_first = self.main_variable_dictionary[str(self.fisrt_index)]
            print(int(self.get_first) + int(self.get_first))

        elif (self.moddle_index == self.TH_SUBSTRACTION) :
            print(int(self.fisrt_index) - int(self.last_index))

        elif (self.moddle_index == self.TH_MULTIPLYCATION) :
            print(int(self.fisrt_index) * int(self.last_index))

        elif (self.moddle_index == self.TH_DIVISION):
            print(int(self.fisrt_index) / int(self.last_index))

        elif (self.moddle_index == self.TH_EQUALANCI) :
            self.main_variable_dictionary = {}
            self.main_variable_dictionary[str(self.fisrt_index)] = str(self.last_index)
            self.common = []
            self.common.append(self.main_variable_dictionary[str(self.fisrt_index)])
            print(self.common)

        elif (self.moddle_index == self.TH_FLOOR_DIVISION) :
            print(int(self.fisrt_index) // int(self.last_index))

        elif ((self.moddle_index == self.TH_SQRT_LAST) and (str(self.fisrt_index) == self.TH_SQRT_FIRST)) :
            print("{:.2f}".format(math.sqrt(int(self.last_index))))

        elif (self.bash == self.main_variable_dictionary[str(self.fisrt_index)]) :
            print(self.main_variable_dictionary[str(self.last_index)])

        else :
            print("That is not a name in this Dictionary.")



if __name__ == '__main__':
    myObj = MakeProgrammingLanguageOperatorsUsing()
    myObj.shell()
    myObj.into_the_list()
    myObj.variables()
    myObj.operators()
