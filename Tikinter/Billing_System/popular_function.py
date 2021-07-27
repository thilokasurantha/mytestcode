from tkinter import *

root = Tk()
text_billing_system_frame = LabelFrame(root, fg="red", bg="#054465", relief=RAISED, bd=10)
text_billing_system_frame.grid(row=1)

biling_system = Label(text_billing_system_frame, text="Billing Software", font=("Britannic Bold", 28), fg="#EAD03D", bg="#054465", justify='center')
biling_system.grid(row=1,padx=500)

text_costomer_details = LabelFrame(root, text="Customer Details", fg="#EAD03D", bg="#054465", font=(
    "Britannic Bold", 11), relief=RAISED, bd=10)
text_costomer_details.grid(row=2,sticky=W)

biling_system = Label(text_costomer_details, text="Billing Software", font=(
    "Britannic Bold", 28), fg="#EAD03D", bg="#054465", justify='center')
biling_system.grid(row=2, padx=250)

text_costomer_details = LabelFrame(root, text="Customer Details", fg="#EAD03D", bg="#054465", font=(
    "Britannic Bold", 11), relief=RAISED, bd=10)
text_costomer_details.grid(row=2, sticky=E)

biling_system = Label(text_costomer_details, text="Billing Software", font=(
    "Britannic Bold", 28), fg="#EAD03D", bg="#054465", justify='center')
biling_system.grid(row=2, padx=250)



root.geometry("1280x720")
# Customer Details


root.mainloop()
