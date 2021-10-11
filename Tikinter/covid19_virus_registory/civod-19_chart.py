from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class CovidChart :
    def __init__(self,chart) :
        self.chart = chart
    def make_screen(self) :
        self.resource = "D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
        self.chart.iconbitmap(self.resource+"\stats.ico")
        self.chart.title("Covid - 19 Vaccines Chart")
    def covid_chart(self) :
        self.astrazeneca = Label(self.chart, text="Oxfard - AstraZeneca :",  font=("Arial Black", 16, 'bold'))
        self.astrazeneca.grid(row=1,sticky=E)
        self.johnson = Label(self.chart, text="Johnson & Jhonson's :",  font=("Arial Black", 16, 'bold'))
        self.johnson.grid(row=2, sticky=E)
        self.pfizer = Label(self.chart, text="Pfizer :",  font=("Arial Black", 16, 'bold'))
        self.pfizer.grid(row=3, sticky=E)
        self.moderna = Label(self.chart, text="Moderna :",font=("Arial Black", 16, 'bold'))
        self.moderna.grid(row=4, sticky=E)
        
        self.inovio = Label(self.chart, text="Inovio :",  font=("Arial Black", 16, 'bold'))
        self.inovio.grid(row=5, sticky=E)
        self.sputnik_v = Label(self.chart, text="Sputnik - V :",  font=("Arial Black", 16, 'bold'))
        self.sputnik_v.grid(row=6, sticky=E)
        self.epi_vac_corona = Label(self.chart, text="EpiVacCorona :", font=("Arial Black", 16, 'bold'))
        self.epi_vac_corona.grid(row=7, sticky=E)
        self.sinoVac = Label(self.chart, text="CoronaVac/SinoVac :",font=("Arial Black", 16, 'bold'))
        self.sinoVac.grid(row=8, sticky=E)

        self.covaxin = Label(self.chart, text="Covaxin :", font=("Arial Black", 16, 'bold'))
        self.covaxin.grid(row=9, sticky=E)
        self.no_vaccines = Label(self.chart, text="No Vaccines :", font=("Arial Black", 16, 'bold'))
        self.no_vaccines.grid(row=10, sticky=E)
    def precentage(self) :
        
        self.chart.mainloop()
if __name__ == '__main__':
    myObj = CovidChart(Tk())
    myObj.make_screen()
    myObj.covid_chart()
    myObj.precentage()
