from tkinter import *
from tkinter import messagebox
# Make a fuction
def numbers(number) :
        show_entry.insert(END, number)

def equal():
        get_the_items = show_entry.get()
        into_the_list = get_the_items.split()
        if (len(into_the_list) > 3):
            messagebox.showerror("Error", "Invalid Number :(")
        calculation = calculate(int(into_the_list[0]) ,int(into_the_list[2]),into_the_list[1] )
        show_entry.delete(0, END)
        show_entry.insert(0, calculation)


def calculate(n1, n2, operator):
    switcher = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        'x': lambda x, y: x*y,
        '÷': lambda x, y: x/y,
    }
    return switcher.get(operator)(n1, n2)
    



def clear() :
        show_entry.delete(len(show_entry.get())-1,END)

def substraction() :
    pass
def multipication () :
    pass
def division():
    pass


if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")
    # resources = "D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
    # root.iconbitmap(resources+"\pythontutorial-1-150x150.ico")

    # root.resizable(False,False)
    application_window_width = 575
    application_window_height =546

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = (screen_width//2 - application_window_width//2)
    center_y = (screen_height//2 - application_window_height//2)

    root.geometry("{}x{}+{}+{}".format(application_window_width,application_window_height,center_x,center_y))

    # Make a Frames
    frame0 = Frame(root)
    frame0.pack()
    frame1 = Frame(root)
    frame1.pack()
    frame2 = Frame(root)
    frame2.pack()
    frame3 = Frame(root)
    frame3.pack()
    frame4 = Frame(root)
    frame4.pack()
    frame5 = Frame(root)
    frame5.pack()
    # Make a GUI
    show_entry = Entry(frame0, width=57, font=("Segoe UI Black", 0))
    show_entry.pack()
    button_7 = Button(frame1, text="7", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: numbers("7"))
    button_7.pack(side=LEFT)
    button_8 = Button(frame1, text="8", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: numbers("8"))
    button_8.pack(side=LEFT)
    button_9 = Button(frame1, text="9", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: numbers("9"))
    button_9.pack(side=LEFT)
    button_substraction = Button(frame1, text="-", width=15,height=5, font=("Gill Sans Ultra Bold", 8),command = substraction)
    button_substraction.pack(side=LEFT)

    button_4 = Button(frame2, text="4", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: numbers("4"))
    button_4.pack(side=LEFT)
    button_5 = Button(frame2, text="5", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: numbers("5"))
    button_5.pack(side=LEFT)
    button_6 = Button(frame2, text="6", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: numbers("6"))
    button_6.pack(side=LEFT)
    button_mulipication = Button(frame2, text="x", width=15, height=5,font=("Gill Sans Ultra Bold", 8), command=multipication)
    button_mulipication.pack(side=LEFT)

    button_1 = Button(frame3, text="1", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: numbers("1"))
    button_1.pack(side=LEFT)
    button_2 = Button(frame3, text="2", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: numbers("2"))
    button_2.pack(side=LEFT)
    button_3 = Button(frame3, text="3", width=15, height=5, font=("Gill Sans Ultra Bold", 8), command=lambda: numbers("3"))
    button_3.pack(side=LEFT)
    button_division = Button(frame3, text="/", width=15, height=5,font=("Gill Sans Ultra Bold", 8), command=division)
    button_division.pack(side=LEFT)

    button_13 = Button(frame4, text="0", width=31,height=5, font=("Gill Sans Ultra Bold", 8),command=lambda : numbers("0"))
    button_13.pack(side=LEFT)
    button_14 = Button(frame4, text="+", width=15,height=5, font=("Gill Sans Ultra Bold", 8),command = lambda : numbers(" + "))
    button_14.pack(side=LEFT)
    button_14 = Button(frame4, text="=", width=15, height=5,font=("Gill Sans Ultra Bold", 8), command=lambda : numbers(" = "))
    button_14.pack(side=LEFT)
    button_clear = Button(frame5, text="clear", width=64, height=5,font=("Gill Sans Ultra Bold", 8),command = clear)
    button_clear.pack(side=LEFT)

    root.mainloop()
