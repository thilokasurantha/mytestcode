class ShellConsole :
    def shell(self) :
        while (True) :
            bash = input("bash >> ")
            print(bash)
myObj = ShellConsole()
myObj.shell()