

class ChosingLabForm:
    def __init__(self, choose):
        self.choose = choose

    def choose_compare_screen(self):
        pass

    def choose_lab_form(self):
        # Asgiriya Lab
        self.asgiriya_lab = ImageTk.PhotoImage(Image.open(ASGIRIYA))
        self.asgiriya_lab_label = Button(image=self.asgiriya_lab, borderwidth=0)
        self.asgiriya_lab_label.grid(row=1)

        self.test_request_asgiriya = ImageTk.PhotoImage(Image.open(TEST_REQUEST))
        self.test_request_asgiriya_label = Button(image=self.test_request_asgiriya, borderwidth=0, command=self.test_request)
        self.test_request_asgiriya_label.grid(row=2)

        self.new_test_request_asgiriya = ImageTk.PhotoImage(Image.open(NEW_TEST_REQUEST))
        self.new_test_request_asgiriya_label = Button(image=self.new_test_request_asgiriya, borderwidth=0, command=self.new_test_request)
        self.new_test_request_asgiriya_label.grid(row=3)

        self.request_asgiriya = ImageTk.PhotoImage(Image.open(REQUEST))
        self.request_label_asgiriya = Button(image=self.request_asgiriya, borderwidth=0, command=self.request_details)
        self.request_label_asgiriya.grid(row=4)

        # Hasalaka Lab
        self.hasalaka_lab = ImageTk.PhotoImage(Image.open(HASALAKA))
        self.hasalaka_lab_label = Button(image=self.hasalaka_lab, borderwidth=0)
        self.hasalaka_lab_label.grid(row=5)

        self.test_request_hasalaka = ImageTk.PhotoImage(Image.open(TEST_REQUEST))
        self.test_request_hasalaka_label = Button(image=self.test_request_hasalaka, borderwidth=0, command=self.test_request)
        self.test_request_hasalaka_label.grid(row=6)

        self.new_test_request_hasalaka = ImageTk.PhotoImage(Image.open(NEW_TEST_REQUEST))
        self.new_test_request_hasalaka_label = Button(image=self.new_test_request_hasalaka, borderwidth=0, command=self.new_test_request)
        self.new_test_request_hasalaka_label.grid(row=7)

        self.request_hasalaka = ImageTk.PhotoImage(Image.open(REQUEST))
        self.request_label_hasalaka = Button(image=self.request_hasalaka, borderwidth=0, command=self.request_details)
        self.request_label_hasalaka.grid(row=8)

        # Methsuwa Lab
        self.methsuwa_lab = ImageTk.PhotoImage(Image.open(METHSUWA))
        self.methsuwa_lab_label = Button(image=self.methsuwa_lab, borderwidth=0)
        self.methsuwa_lab_label.grid(row=9)

        self.test_request_methsuwa = ImageTk.PhotoImage(Image.open(TEST_REQUEST))
        self.test_request_methsuwa_label = Button(image=self.test_request_methsuwa, borderwidth=0, command=self.test_request)
        self.test_request_methsuwa_label.grid(row=10)

        self.new_test_request_methsuwa = ImageTk.PhotoImage(Image.open(NEW_TEST_REQUEST))
        self.new_test_request_methsuwa_label = Button(image=self.new_test_request_methsuwa, borderwidth=0, command=self.new_test_request)
        self.new_test_request_methsuwa_label.grid(row=11)

        self.request_methsuwa = ImageTk.PhotoImage(Image.open(REQUEST))
        self.request_label_methsuwa = Button(image=self.request_methsuwa, borderwidth=0, command=self.request_details)
        self.request_label_methsuwa.grid(row=12)

        # Family Lab
        self.family_lab = ImageTk.PhotoImage(Image.open(FAMILY))
        self.family_lab_label = Button(image=self.family_lab, borderwidth=0)
        self.family_lab_label.grid(row=13)

        self.test_request_family = ImageTk.PhotoImage(Image.open(TEST_REQUEST))
        self.test_request_family_label = Button(image=self.test_request_family, borderwidth=0, command=self.test_request)
        self.test_request_family_label.grid(row=14)

        self.new_test_request_family = ImageTk.PhotoImage(Image.open(NEW_TEST_REQUEST))
        self.new_test_request_family_label = Button(image=self.new_test_request_family, borderwidth=0, command=self.new_test_request)
        self.new_test_request_family_label.grid(row=15)

        self.request_family = ImageTk.PhotoImage(Image.open(REQUEST))
        self.request_label_family = Button(image=self.request_family, borderwidth=0, command=self.request_details)
        self.request_label_family.grid(row=16)

        self.choose.mainloop()

    def test_request(self):
        pass

    def new_test_request(self):
        self.choose.destroy()
        import new_test_request

        self.importing_new_test = new_test_request.NewTestRequestForm(Tk())
        self.importing_new_test.new_test_request_compare_screen()
        self.importing_new_test.new_test_request_form()

    def request_details(self):
        pass
