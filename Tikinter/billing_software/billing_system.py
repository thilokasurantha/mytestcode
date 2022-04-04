from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class MakeBillingSoftware :
    def __init__(self,root) :
        self.root = root
    def search(self):
        print("Saved")
    def make_the_screen(self) :
        self.window_width = 1335
        self.window_height = 790

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.center_x = (self.screen_width//2 - self.window_width//2)
        self.center_y = (self.screen_height//2 - self.window_height//2)

        self.root.geometry("{}x{}+{}+{}".format(self.window_width,self.window_height,self.center_x,self.center_y))
        self.root.resizable(False,False)
    def make_billing_system_gui(self) :
        # Resources_pasths
        self.resources = "C:\\Users\\HP\\Downloads"


        # Make Billing Label
        self.billing_software_frame = LabelFrame(self.root, relief=RAISED, bd=5, bg="#074463")
        self.billing_software_frame.pack(fill=X)
        self.billing_software = Label(self.billing_software_frame, text="Billing Software", font=("Elephant", 24), bg="#074463", fg="#F8D529")
        self.billing_software.pack(side=BOTTOM)


        # Cutomer Details
        self.customer_details_frame = LabelFrame(self.root, text="Customer Details", font=("Elephant", 14),fg="#F8D529",bg="#074463",relief=RAISED,bd=5,width=359)
        self.customer_details_frame.pack(fill=X)
        self.customer_name = Label(self.customer_details_frame, text="Customer Name",font=("Elephant",12),bg="#074463",fg="#FFFFFF")
        self.customer_name.pack(anchor=W, side=LEFT, fill=X,padx=20, pady=2)
        self.customer_name_entry = Entry(self.customer_details_frame,font=("Elephant",12))
        self.customer_name_entry.pack(anchor=W, side=LEFT,  padx=5)
        self.contact_number = Label(self.customer_details_frame, text="Contact Number", font=("Elephant", 12), bg="#074463", fg="#FFFFFF")
        self.contact_number.pack(anchor=W, side=LEFT, fill=X,padx=20,pady=2)
        self.contact_number_entry = Entry(self.customer_details_frame, font=("Elephant", 12))
        self.contact_number_entry.pack(anchor=W, side=LEFT,  padx=5,fill=X)
        self.bill_number = Label(self.customer_details_frame,text="Bill No.",font=("Elephant",12),bg="#074463",fg="#FFFFFF")
        self.bill_number.pack(side=LEFT,anchor=W,fill=X,padx=20,pady=2)
        self.bill_number_entry = Entry(self.customer_details_frame, font=("Elephant", 12))
        self.bill_number_entry.pack(anchor=W, side=LEFT,  padx=5, fill=X)



        # Cosmetics sectionary
        self.cosmetics = LabelFrame(self.root, text="Cosmetics", font=("Elephant", 14), fg="#F8D529", bg="#074463", relief=RAISED, bd=5)
        self.cosmetics.pack(side=LEFT, anchor=N,fill=X)


        # Make the Frame
        self.another_frame = Frame(self.cosmetics,bg="#074463")
        self.another_frame.pack(side=RIGHT)


        # Catogories the programme
        self.bath_soup = Label(self.cosmetics, text="Bath Soup", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.bath_soup.pack(anchor=W, pady=5)
        self.bath_soup_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.bath_soup_entry.pack(pady=5,padx=20)

        self.face_cream= Label(self.cosmetics, text="Face Cream", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.face_cream.pack(anchor=W,pady=5)
        self.face_cream_entry = Entry(self.another_frame, font=("Elephant", 12),width=10)
        self.face_cream_entry.pack(pady=5, padx=20)

        self.face_wash = Label(self.cosmetics, text="Face Wash", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.face_wash.pack(anchor=W, pady=5)
        self.face_wash_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.face_wash_entry.pack(pady=5, padx=20)

        self.hair_spray = Label(self.cosmetics, text="Hair Spray", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.hair_spray.pack(anchor=W,pady=5)
        self.hair_spray_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.hair_spray_entry.pack(pady=5, padx=20)

        self.hair_gel = Label(self.cosmetics, text="Hair Gel", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.hair_gel.pack(anchor=W,pady=5)
        self.hair_gel_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.hair_gel_entry.pack(pady=5, padx=20)

        self.body_losion = Label(self.cosmetics, text="Body Losion", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.body_losion.pack(anchor=W,pady=5)
        self.body_losion_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.body_losion_entry.pack(pady=5, padx=20)

        # Cosmetics sectionary
        self.cosmetics = LabelFrame(self.root, text="Grocery", font=("Elephant", 14), fg="#F8D529", bg="#074463", relief=RAISED, bd=5)
        self.cosmetics.pack(side=LEFT, anchor=N, fill=X)

        # Make the Frame
        self.another_frame = Frame(self.cosmetics, bg="#074463")
        self.another_frame.pack(side=RIGHT)

        # Catogories the programme
        self.bath_soup = Label(self.cosmetics, text="Rice", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.bath_soup.pack(anchor=W, pady=5)
        self.bath_soup_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.bath_soup_entry.pack(pady=5, padx=20)

        self.face_cream = Label(self.cosmetics, text="Food Oil", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.face_cream.pack(anchor=W, pady=5)
        self.face_cream_entry = Entry( self.another_frame, font=("Elephant", 12), width=10)
        self.face_cream_entry.pack(pady=5, padx=20)

        self.face_wash = Label(self.cosmetics, text="Daal", font=( "Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.face_wash.pack(anchor=W, pady=5)
        self.face_wash_entry = Entry( self.another_frame, font=("Elephant", 12), width=10)
        self.face_wash_entry.pack(pady=5, padx=20)

        self.hair_spray = Label(self.cosmetics, text="Wheat", font=( "Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.hair_spray.pack(anchor=W, pady=5)
        self.hair_spray_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.hair_spray_entry.pack(pady=5, padx=20)

        self.hair_gel = Label(self.cosmetics, text="Sugar", font=( "Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.hair_gel.pack(anchor=W, pady=5)
        self.hair_gel_entry = Entry( self.another_frame, font=("Elephant", 12), width=10)
        self.hair_gel_entry.pack(pady=5, padx=20)

        self.body_losion = Label(self.cosmetics, text="Tea", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.body_losion.pack(anchor=W, pady=5)
        self.body_losion_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.body_losion_entry.pack(pady=5, padx=20)

        # Cosmetics sectionary
        self.cosmetics = LabelFrame(self.root, text="Cold Drinks", font=("Elephant", 14), fg="#F8D529", bg="#074463", relief=RAISED, bd=5)
        self.cosmetics.pack(side=LEFT, anchor=N, fill=X)

        # Make the Frame
        self.another_frame = Frame(self.cosmetics, bg="#074463")
        self.another_frame.pack(side=RIGHT)

        # Catogories the programme
        self.bath_soup = Label(self.cosmetics, text="Maza", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.bath_soup.pack(anchor=W, pady=5)
        self.bath_soup_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.bath_soup_entry.pack(pady=5, padx=20)

        self.face_cream = Label(self.cosmetics, text="Cock", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.face_cream.pack(anchor=W, pady=5)
        self.face_cream_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.face_cream_entry.pack(pady=5, padx=20)

        self.face_wash = Label(self.cosmetics, text="Frooti", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.face_wash.pack(anchor=W, pady=5)
        self.face_wash_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.face_wash_entry.pack(pady=5, padx=20)

        self.hair_spray = Label(self.cosmetics, text="Thumbs UP", font=( "Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.hair_spray.pack(anchor=W, pady=5)
        self.hair_spray_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.hair_spray_entry.pack(pady=5, padx=20)

        self.hair_gel = Label(self.cosmetics, text="Limca", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.hair_gel.pack(anchor=W, pady=5)
        self.hair_gel_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.hair_gel_entry.pack(pady=5, padx=20)

        self.body_losion = Label(self.cosmetics, text="Sprite", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.body_losion.pack(anchor=W, pady=5)
        self.body_losion_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.body_losion_entry.pack(pady=5, padx=20)


        # Cosmetics sectionary
        self.cosmetics = LabelFrame(self.root, text="Fruits", font=("Elephant", 14), fg="#F8D529", bg="#074463", relief=RAISED, bd=5)
        self.cosmetics.pack(side=LEFT, anchor=N, fill=X)

        # Make the Frame
        self.another_frame = Frame(self.cosmetics, bg="#074463")
        self.another_frame.pack(side=RIGHT)

        # Catogories the programme
        self.bath_soup = Label(self.cosmetics, text="Apple", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.bath_soup.pack(anchor=W, pady=5)
        self.bath_soup_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.bath_soup_entry.pack(pady=5, padx=20)

        self.face_cream = Label(self.cosmetics, text="Mangoes", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.face_cream.pack(anchor=W, pady=5)
        self.face_cream_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.face_cream_entry.pack(pady=5, padx=20)

        self.face_wash = Label(self.cosmetics, text="Banana", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.face_wash.pack(anchor=W, pady=5)
        self.face_wash_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.face_wash_entry.pack(pady=5, padx=20)

        self.hair_spray = Label(self.cosmetics, text="Pine Apple", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.hair_spray.pack(anchor=W, pady=5)
        self.hair_spray_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.hair_spray_entry.pack(pady=5, padx=20)

        self.hair_gel = Label(self.cosmetics, text="Papaya", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.hair_gel.pack(anchor=W, pady=5)
        self.hair_gel_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.hair_gel_entry.pack(pady=5, padx=20)

        self.body_losion = Label(self.cosmetics, text="Grapes", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.body_losion.pack(anchor=W, pady=5)
        self.body_losion_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.body_losion_entry.pack(pady=5, padx=20)

        # Cosmetics sectionary
        self.cosmetics = LabelFrame(self.root, text="Another", font=("Elephant", 14), fg="#F8D529", bg="#074463", relief=RAISED, bd=5)
        self.cosmetics.pack(side=LEFT, anchor=N, fill=X)

        # Make the Frame
        self.another_frame = Frame(self.cosmetics, bg="#074463")
        self.another_frame.pack(side=RIGHT)

        # Catogories the programme
        self.bath_soup = Label(self.cosmetics, text="Apple", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.bath_soup.pack(anchor=W, pady=5)
        self.bath_soup_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.bath_soup_entry.pack(pady=5, padx=20)

        self.face_cream = Label(self.cosmetics, text="Mangoes", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.face_cream.pack(anchor=W, pady=5)
        self.face_cream_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.face_cream_entry.pack(pady=5, padx=20)

        self.face_wash = Label(self.cosmetics, text="Banana", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.face_wash.pack(anchor=W, pady=5)
        self.face_wash_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.face_wash_entry.pack(pady=5, padx=20)

        self.hair_spray = Label(self.cosmetics, text="Pine Apple", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.hair_spray.pack(anchor=W, pady=5)
        self.hair_spray_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.hair_spray_entry.pack(pady=5, padx=20)

        self.hair_gel = Label(self.cosmetics, text="Papaya", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.hair_gel.pack(anchor=W, pady=5)
        self.hair_gel_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.hair_gel_entry.pack(pady=5, padx=20)

        self.body_losion = Label(self.cosmetics, text="Grapes", font=("Elephant", 12), bg="#074463", fg="#8FEDB1")
        self.body_losion.pack(anchor=W, pady=5)
        self.body_losion_entry = Entry(self.another_frame, font=("Elephant", 12), width=10)
        self.body_losion_entry.pack(pady=5, padx=20)




        
        self.root.mainloop()

if __name__ == '__main__':
    myObj = MakeBillingSoftware(Tk())
    myObj.make_the_screen()
    myObj.make_billing_system_gui()
