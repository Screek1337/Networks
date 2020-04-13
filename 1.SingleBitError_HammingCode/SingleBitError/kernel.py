import tkinter as tk
from gui import GUI


class Kernel(GUI):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.source.trace("rw", self.split_source)

    def split_source(self, *args):
        self.clear_btns()
        for idx, val in enumerate(self.source.get()):
            self.source_btns[idx].configure(text=val)

            bin_char = self.text_to_bin(val)
            self.parity_btns[idx].configure(text=self.parity_check(bin_char))

            for _idx, _val in enumerate(bin_char):
                self.bit_btns[idx][_idx].configure(text=_val)

    def clear_btns(self):
        for i in range(15):
            self.source_btns[i].configure(text="")
            self.parity_btns[i].configure(text="")
            for j in range(8):
                self.bit_btns[i][j].configure(text="")

    def text_to_bin(self, text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

    def parity_check(self, block):
        if sum([int(i) for i in block]) % 2 == 1:
            return "0"
        else:
            return "1"


if __name__ == "__main__":
    root = tk.Tk()
    kernel = Kernel(master=root)
    kernel.mainloop()
