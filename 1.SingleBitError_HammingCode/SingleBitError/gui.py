import tkinter as tk


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("Single Bit Error")
        master.grid_columnconfigure(0, minsize=30)
        master.grid_columnconfigure(10, minsize=30)
        master.grid_rowconfigure(1, minsize=40)
        master.grid_rowconfigure(18, minsize=35)

        self.source_btns = []
        self.bit_btns = []
        self.parity_btns = []

        self.source = tk.StringVar()
        self.original_checksum = tk.StringVar()
        self.wrong_checksum = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.top_label = tk.Label(master=self.master,
                                  text="Enter 10-15 characters:")

        self.source_field = tk.Entry(master=self.master,
                                     textvariable=self.source)

        self.check_sum_label = tk.Label(master=self.master, text="Checksum")
        self.check_sum_field = tk.Entry(master=self.master,
                                        width=2,
                                        textvariable=self.wrong_checksum)
        self.original_check_sum_label = tk.Label(master=self.master,
                                                 text="Original checksum")
        self.original_check_sum_field = tk.Entry(
            master=self.master, width=2, textvariable=self.original_checksum)

        self.top_label.grid(row=0, column=0, columnspan=10, sticky="W")
        self.source_field.grid(row=1, column=0, columnspan=10, sticky="W")
        self.check_sum_label.grid(row=18, column=0, columnspan=9, sticky="W")
        self.check_sum_field.grid(row=18, column=10, columnspan=9)
        self.original_check_sum_label.grid(row=19,
                                           column=0,
                                           columnspan=9,
                                           sticky="W")
        self.original_check_sum_field.grid(row=19, column=10, columnspan=9)

        self.create_source_btns()
        self.create_bit_btns()
        self.create_parity_btns()

    def create_source_btns(self):
        for i in range(15):
            btn = tk.Button(master=self.master, text="", width=2, height=1)
            btn.grid(row=i + 2, column=0, sticky="W")
            self.source_btns.append(btn)

    def create_bit_btns(self):
        for i in range(15):
            self.bit_btns.append([])
            for j in range(8):
                btn = tk.Button(master=self.master, text="", width=2, height=1)
                btn.grid(row=i + 2, column=j + 1)
                self.bit_btns[i].append(btn)

    def create_parity_btns(self):
        for i in range(15):
            btn = tk.Button(master=self.master, text="", width=2, height=1)
            btn.grid(row=i + 2, column=10, sticky="E")
            self.parity_btns.append(btn)


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(master=root)
    app.mainloop()
