import math
class MainVariable :
    def shell(self) :
        print("Python 3.9.5 (tags/v3.9.5: 0a7dcbd, May  3 2021, 17: 27: 52)[MSC v.1928 64 bit(AMD64)] on win32 Type 'help', 'copyright', 'credits' or 'license' for more information.")
        while (True) :
            self.bash = input("bash >> ")
            self.help_function()
            self.variable()
    def help_function(self) :
        if (self.bash == "help()") :
            self.help_file  =  open("help.txt",'r')
            print(self.help_file.read())
            self.help_file.close()
    def variable(self) :
        self.TH_DIVISION = "/"
        self.TH_ADDITION = "+"
        self.TH_MINESE = "-"
        self.TH_MULTIPLICATION = "*"
        self.TH_SQRT = "squrt"
        self.TH_MIN_TO_MAX =  "min_to_max"

        self.into_the_list = self.bash.split()
        self.first_index  = int(self.into_the_list[0])
        self.second_index = self.into_the_list[1]
        self.third_index = int(self.into_the_list[2])

        if (str(self.second_index) == str(self.TH_ADDITION)) :
            print(self.first_index + self.third_index)

        elif (str(self.second_index) == str(self.TH_DIVISION)) :
            self.find_max_number = max(self.first_index, self.second_index)
            self.max_number = self.find_max_number
            print(type(self.max_number))
            self.find_min_number = min(self.first_index, self.second_index)
            self.min_number = self.find_min_number
            print(self.min_number)
            print(self.max_number / self.min_number)

        elif (str(self.second_index) == str(self.TH_MINESE)) :
            self.find_max_number = max(self.first_index, self.second_index)
            self.max_number = self.find_max_number
            print(type(self.max_number))
            self.find_min_number = min(self.first_index, self.second_index)
            self.min_number = self.find_min_number
            print(self.min_number)
            print(self.max_number - self.min_number)

        elif (str(self.second_index) == str(self.TH_MULTIPLICATION)) :
            print(self.first_index * self.third_index)

        elif (self.bash == "sqrt ()") :
            self.ask = int(input("Enter the bash number >> "))
            self.sqrt = math.sqrt(ask)
            print(self.sqrt)

        

myObj = MainVariable()
myObj.shell()
myObj.variable()
