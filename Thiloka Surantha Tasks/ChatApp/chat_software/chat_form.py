from tkinter import *
import db_handler as db
from tkinter import messagebox

class ChatForm :
    def __init__(self, root) -> None:
        self.root = root
        self.root.resizable(False, False)

    def click_3(self, event) :
        self.name_entry_1.delete(0, END)
    def click_4(self, event) :
        self.key_entry_1.delete(0, END)

    def form(self, name, key) :
        self.frame = Frame(self.root)
        self.frame.grid(row=0, column=0)

        self.sender = Label(self.frame, text="Sender's Details", font=("Source Sans Pro",17,"bold"))
        self.sender.grid(row=0, column=0, sticky=W)
        self.name_entry = Entry(self.frame, font=("Source Sans Pro",17,"bold"))
        self.name_entry.insert(0, name)
        self.name_entry.grid(row=1, column=0)
        self.key_entry = Entry(self.frame, font=("Source Sans Pro",17,"bold"))
        self.key_entry.insert(0, key)
        self.key_entry.grid(row=1, column=2)

        self.reciever = Label(self.frame, text="Reciever's Details", font=("Source Sans Pro",17,"bold"))
        self.reciever.grid(row=2, column=0, sticky=W)
        self.name_entry_1 = Entry(self.frame, font=("Source Sans Pro",17,"bold"))
        self.name_entry_1.insert(0, "Name:")
        self.name_entry_1.bind('<ButtonRelease-1>', self.click_3)
        self.name_entry_1.grid(row=3, column=0)
        self.key_entry_1 = Entry(self.frame, font=("Source Sans Pro",17,"bold"))
        self.key_entry_1.insert(0, "Key:")
        self.key_entry_1.bind('<ButtonRelease-1>', self.click_4)
        self.key_entry_1.grid(row=3, column=2)

        self.connectb = Button(self.root, text="Conect Each Others", font=("Source Sans Pro",17,"bold"), command=self.connect, width=39)
        self.connectb.grid(row=4, column=0, sticky=W)

        self.text = Text(self.root, font=("Source Sans Pro",12,"bold"), width=58)
        self.text.grid(row=5,column=0)

        self.message = Text(self.root, font=("Source Sans Pro",12,"bold"), width=52, height=3)
        self.message.grid(row=6, column=0, sticky=W)
        self.send = Button(self.root, text="SEND",  font=("Source Sans Pro",12,"bold"), height=3)
        self.send.grid(column=0, row=6, sticky=E)

        self.root.title("WeChatApp")
        self.root.mainloop()

    def connect(self) :
        self.bot_name = self.name_entry_1.get()
        self.bot_key = self.key_entry_1.get()
        result = db.DatabaseHandlerLogin().register_form(self.bot_name)

        if result :
            messagebox.showinfo("Information", "Your now connecting bots.")
            sender = {
                "name":self.name_entry.get(),
                "key":self.key_entry.get(),
                "mode":"sender",
            }
            reciever = {
                "name":self.bot_name,
                "key":self.bot_key,
                "mode":"reciever",
            }
            obj = db.DatabaseHandlerMessages(sender, reciever)
            out = obj.output()
            print(out)
            
        else :
            messagebox.showerror("Error", "Please type correctly.")
            self.name_entry_1.delete(0, END)
            self.key_entry_1.delete(0, END)