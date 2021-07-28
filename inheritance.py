import time
class Person :
    def __init__(self,fname,lname) :
        self.firstname = fname
        self.lastname = lname
    def function(self) :
        print(self.firstname,self.lastname)
class Student(Person) :
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.this_year = year
    def welcome_function(self) :
        print("Welcome {} {} this year is {}".format(self.firstname.upper(),self.lastname.lower(),self.this_year))
        time.sleep(5)

myObj = Student("thiloka", "surantha",2019)
myObj.welcome_function()
