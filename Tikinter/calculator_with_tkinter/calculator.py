from tkinter import *
def main_calculator_gui_making(root):
        # Make a Frames
        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack() 
        frame3 = Frame(root)
        frame3.pack()
        frame4 = Frame(root)
        frame4.pack()
        # Make a GUI
        show_entry = Entry(frame1, width=43, font=("Segoe UI Black", 0))
        show_entry.pack()
        button_7 = Button(frame1, text="7", width=15, height=5,font=("Gill Sans Ultra Bold",8))
        button_7.pack(side=LEFT)
        show_entry.insert(0, "7")
        button_8 = Button(frame1, text="8", width=15, height=5,font=("Gill Sans Ultra Bold", 8))
        button_8.pack(side=LEFT)
        button_9 = Button(frame1, text="9", width=15, height=5,font=("Gill Sans Ultra Bold",8))
        button_9.pack(side=LEFT)
    
        button_4 = Button(frame2, text="4", width=15,height=5,font=("Gill Sans Ultra Bold",8))
        button_4.pack(side=LEFT)
        button_5 = Button(frame2, text="5", width=15,height=5,font=("Gill Sans Ultra Bold",8))
        button_5.pack(side=LEFT)
        button_6 = Button(frame2, text="6", width=15, height=5,font=("Gill Sans Ultra Bold",8))
        button_6.pack(side=LEFT)
    
        button_1 = Button(frame3, text="1", width=15, height=5,font=("Gill Sans Ultra Bold",8))
        button_1.pack(side=LEFT)
        button_2 = Button(frame3, text="2", width=15, height=5,font=("Gill Sans Ultra Bold",8))
        button_2.pack(side=LEFT)
        button_3 = Button(frame3, text="3", width=15, height=5,font=("Gill Sans Ultra Bold",8))
        button_3.pack(side=LEFT)
    
        button_12 = Button(frame4, text="+/-", width=15, height=5,font=("Gill Sans Ultra Bold",8))
        button_12.pack(side=LEFT)
        button_13 = Button(frame4, text="0", width=15, height=5,font=("Gill Sans Ultra Bold",8))
        button_13.pack(side=LEFT)
        button_14 = Button(frame4, text="/", width=15, height=5,font=("Gill Sans Ultra Bold",8))
        button_14.pack(side=LEFT)
    
if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")
    resources = "D:\Programing\GIT\mytestcode\Tikinter\labsoft\iresources"
    root.iconbitmap(resources+"\pythontutorial-1-150x150.ico")

    root.resizable(False,False)
    application_window_width = 426
    application_window_height = 426

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = (screen_width//2 - application_window_width//2)
    center_y = (screen_height//2 - application_window_height//2)

    root.geometry("{}x{}+{}+{}".format(application_window_width,application_window_height,center_x,center_y))

    main_calculator_gui_making(root)

    root.mainloop()

