from tkinter import messagebox
from tkinter import *
import student
import subjects
import items

class AddScore :
    def __init__(self, score) -> None:
        self.score = score

    def check_scores(self) :
        answer = None

        messagebox.showinfo("Information", "Sum = 12 Avarage = 12")
