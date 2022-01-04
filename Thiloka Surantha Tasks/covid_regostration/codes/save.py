class SaveFile :
    def __init__(self,s_name,s_age,s_card,s_vaccine):
        self.s_name = s_name
        self.s_age = s_age
        self.s_card = s_card
        self.s_vaccine = s_vaccine
    def save_the_text_file(self) :

        name_split = self.s_name.split()
        create_file = open("/home/thiloka/Documents/100 Python Projects/covid_regostration/save_files/{}_pacient.txt".format(name_split[0]) , "x")

        edit = (
                "Pacient Name                             =>> {} \n"
                "Pacient Age                              =>> {} \n"
                "Pacient Identy card                      =>> {} \n"
                "The pacient vaccine                      =>> {} \n"
        ).format(self.s_name,self.s_age,self.s_card,self.s_vaccine)
        write = create_file.write(edit)

        create_file.close()

        print("Pacient is created . path is >> {}".format("/home/thiloka/Documents/100 Python Projects/covid_regostration/save_files"))