import re

class SpecialVariables :
    def __init__(self, terminal) :
        self.terminal = terminal

class Lexer(SpecialVariables) :
    def __init__(self, terminal):
        super().__init__(terminal)

    def lexer(self) :
        main_re = re.compile(r'[0-9]+|[\+\-\*\/]|[\(\)]')
        compile_num = re.compile(r'[0-9]+')
        compile_operators = re.compile(r'[\+\-\*\/]')
        compile_symbols = re.compile(r'[\(\)]')

        number = compile_num.findall(self.terminal)
        operators = compile_operators.findall(self.terminal)
        symbols = compile_symbols.findall(self.terminal)
        main = main_re.findall(self.terminal)

        explain = []

        for check in main :
            if check in number :
                explain.append(f"number:{check}")

            elif check in operators :
                explain.append(f"operator:{check}")

            elif check in symbols :
                explain.append(f"brackets:{check}")

        print(explain)
        if (self.terminal == "exit()") :
            exit()

if __name__ == '__main__':
    while (True) :
        bash = input(">>> ")
        myProgramme = Lexer(bash)
        myProgramme.lexer()
