import sys

class BinToDec:
    def __init__(self, ui, dec=True):
        self.ui = ui
        self.dec = dec
    
    def bin_to_dec(self):
        self.decimal = 0
        if self.dec:
            ui = self.ui
            ui.reverse()
            for i, j in enumerate(ui):
                self.decimal += (2 ** i) * int(j)  

    def dec_to_bin(self):
        ui = int(self.ui)
        self.binary = []
        while ui > 0:
            self.binary.append(ui % 2)
            ui = ui // 2
        self.binary.reverse()

    def option_selector(self):
        if self.dec:
            self.bin_to_dec()
            print(self.decimal)
        elif self.dec == False:
            self.dec_to_bin()
            print(self.binary)
            print(''.join(str(e) for e in self.binary))

def main():
    if sys.argv[1] == "--bin":
        ui = input("Enter the binary number: ")
        ui = list(ui)
        bindtodec = BinToDec(ui)
        bindtodec.option_selector()
    elif sys.argv[1] == "--dec":
        ui = int(input("Enter the decimal number: "))
        dectobin = BinToDec(ui, dec=False)
        dectobin.option_selector()
    
