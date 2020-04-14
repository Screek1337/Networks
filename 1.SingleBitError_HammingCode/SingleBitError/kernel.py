import tkinter as tk
from gui import GUI


class Kernel(GUI):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.source.trace("w", self.check_lenght)

        for i in range(15):
            self.parity_btns[i].config(command=lambda i=i: self.inv_bit(i))
            for j in range(8):
                self.bit_btns[i][j].config(
                    command=lambda i=i, j=j: self.inv_bit(i, j, False))

    def check_lenght(self, *args):
        if len(self.source.get()) > 15:
            self.source.set(self.source.get()[:15])
        self.clear_btns()
        self.split_source()

    def split_source(self):
        self.original_checksum.set("")
        self.wrong_checksum.set("")
        checksum = ""
        for idx, val in enumerate(self.source.get()):
            self.source_btns[idx].configure(text=val)

            bin_char = self.text_to_bin(val)
            parity_bit = self.parity_check(bin_char)
            checksum += parity_bit

            self.parity_btns[idx].configure(text=parity_bit)

            for _idx, _val in enumerate(bin_char):
                self.bit_btns[idx][_idx].configure(text=_val)

        if self.source.get():
            self.original_checksum.set(self.parity_check(checksum))
            self.wrong_checksum.set(self.parity_check(checksum))

    def clear_btns(self):
        for i in range(15):
            self.source_btns[i].configure(text="")
            self.parity_btns[i].configure(text="")
            for j in range(8):
                self.bit_btns[i][j].configure(text="")

    def get_btns_checksum(self):
        checksum = ""
        for i in range(len(self.source.get())):
            checksum += str(self.parity_btns[i]["text"])
        self.wrong_checksum.set(self.parity_check(checksum))

    def text_to_bin(self, text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

    def parity_check(self, block):
        if sum([int(i) for i in block]) % 2 == 1:
            return "0"
        else:
            return "1"

    def inv_bit(self, i, j=None, parity=True):
        if parity:
            self.parity_btns[i]["text"] = 1 - int(self.parity_btns[i]["text"])
        else:
            self.bit_btns[i][j]["text"] = 1 - int(self.bit_btns[i][j]["text"])
            self.parity_btns[i]["text"] = 1 - int(self.parity_btns[i]["text"])
        self.get_btns_checksum()


if __name__ == "__main__":
    root = tk.Tk()
    kernel = Kernel(master=root)
    kernel.mainloop()
