class NameSorter :
    def __init__(self,name) :
        self.name = name

    def name_sorter(self) :
        split = self.name.split()
        data = []
        cur = 0
        for looping in range(0,len(split)) :
            while (looping == cur) :
                data.append(split[cur][0])
                cur += 1

        print(data)
if __name__ == "__main__" :
    get_name = input("Enter you want to short ? ")
    myObj = NameSorter(get_name)
    myObj.name_sorter()