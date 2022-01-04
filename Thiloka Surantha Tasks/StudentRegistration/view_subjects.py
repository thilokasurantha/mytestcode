from tkinter import *
import database_handler

def view_subjects() :
    view = Tk()

    db_handler = database_handler.DatabaseHandler()
    result = db_handler.get_all_subjects()


    maths = Label(view, text="1.\tMathematics",font=("Source Sans Pro",12,'bold'))
    maths.pack(anchor=W)
    ict = Label(view, text="2.\tInformation Communication Technology",font=("Source Sans Pro",12,'bold'))
    ict.pack(anchor=W)
    sin = Label(view, text="3.\tSinhala",font=("Source Sans Pro",12,'bold'))
    sin.pack(anchor=W)
    geo = Label(view, text="4.\tGeography",font=("Source Sans Pro",12,'bold'))
    geo.pack(anchor=W)
    his = Label(view, text="1.\tHistory",font=("Source Sans Pro",12,'bold'))
    his.pack(anchor=W)
    tam = Label(view, text="1.\tTamil",font=("Source Sans Pro",12,'bold'))
    tam.pack(anchor=W)
    scie = Label(view, text="1.\tScience",font=("Source Sans Pro",12,'bold'))
    scie.pack(anchor=W)
    budd = Label(view, text="1.\tBuddhishm",font=("Source Sans Pro",12,'bold'))
    budd.pack(anchor=W)
    art = Label(view, text="1.\tART",font=("Source Sans Pro",12,'bold'))
    art.pack(anchor=W)
    pts = Label(view, text="1.\tP.T.S",font=("Source Sans Pro",12,'bold'))
    pts.pack(anchor=W)
    pt = Label(view, text="1.\tP.T",font=("Source Sans Pro",12,'bold'))
    pt.pack(anchor=W)
    eng = Label(view, text="1.\tEnglish",font=("Source Sans Pro",12,'bold'))
    eng.pack(anchor=W)
    civ = Label(view, text="1.\tCivics",font=("Source Sans Pro",12,'bold'))
    civ.pack(anchor=W)


    view.mainloop()

view_subjects()