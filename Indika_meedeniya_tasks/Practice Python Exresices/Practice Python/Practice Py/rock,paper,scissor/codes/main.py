from tkinter import *
from PIL import ImageTk,Image
import computer as cmp
import user as usr

COMPUTER = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/Practice Py/rock,paper,scissor/img/computer.png"
MAN = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/Practice Py/rock,paper,scissor/img/man.png"

class MainForm :
    def __init__(self,main) :
        self.main = main

    def compare_screen(self) :
        self.main.title("Main Page")

    def import_images(self) :
        self.computer_img = ImageTk.PhotoImage(Image.open(COMPUTER))
        self.man_img = ImageTk.PhotoImage(Image.open(MAN))

    def main_form(self) :
        self.computer_button = Button(self.main, image=self.computer_img, text="User Vs Computer", compound=LEFT, command=self.computer,font=("Source Sans Pro",12,'bold'),width=500)
        self.computer_button.pack()

        self.user_button = Button(self.main, image=self.man_img, text="User Vs User", compound=LEFT,command=self.user,font=("Source Sans Pro",12,'bold'),width=500)
        self.user_button.pack()

        self.main.mainloop()
    def user(self) :
        self.main.destroy()

        myUserGame = usr.UserGame(Tk())
        myUserGame.compare_screen()
        myUserGame.import_images()
        myUserGame.user_game_form()
    def computer(self) :
        self.main.destroy()

        myComputerGame = cmp.ComputerGame(Tk())
        myComputerGame.compare_screen()
        myComputerGame.import_images()
        myComputerGame.computer_game_form()

if __name__ == '__main__':
    myMain = MainForm(Tk())
    myMain.import_images()
    myMain.compare_screen()
    myMain.main_form()
    myMain.user()
    myMain.computer()
            