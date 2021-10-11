from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

ROCK = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/Practice Py/rock,paper,scissor/img/rock.png"
PAPER = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/Practice Py/rock,paper,scissor/img/paper.png"
SCISSOR = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/Practice Py/rock,paper,scissor/img/scissor.png"
MAN = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/Practice Py/rock,paper,scissor/img/man.png"
COMPUTER = r"/media/thiloka/PythonPrograming/Programing/GIT/mytestcode/Practice Py/rock,paper,scissor/img/computer.png" 

class ComputerGame :
    def __init__(self,game) :
        self.game = game

    def compare_screen(self) :
        pass

    def import_images(self) :
        self.rock_img = ImageTk.PhotoImage(Image.open(ROCK))
        self.paper_img = ImageTk.PhotoImage(Image.open(PAPER))
        self.scissor_img = ImageTk.PhotoImage(Image.open(SCISSOR))
        self.man_img = ImageTk.PhotoImage(Image.open(MAN))
        self.computer = ImageTk.PhotoImage(Image.open(COMPUTER))

    def user_game_form(self) :
        pass