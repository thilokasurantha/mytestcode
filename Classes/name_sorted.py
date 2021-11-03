class NameSorter :
    def __init__(self,name) :
        self.name = name

    def name_sorter(self) :
        elements = self.name.split()
        abr=''
        for ele in elements:
            abr = abr+ele[0].upper()

    
        # for i in range(0,len(split)) :
        #    data.append(split[i][0])
        #         cur += 1 

        print(abr)

if __name__ == "__main__" :
    get_name = input("Enter you want to short ? ")
    myObj = NameSorter(get_name)
    myObj.name_sorter()

# [thiloka,surantha]
0,2