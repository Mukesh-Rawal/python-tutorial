class complex_number:
    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img


    def print_complex_num(self):
        print(self.real, "+ i",self.img)


    def __add__(self, other):
        new = complex_number()
        new.real = self.real + other.real
        new.img = self.img + other.img
        return new


c1 = complex_number(4,5)
c1.print_complex_num()

c2 = complex_number(2,3)
c2.print_complex_num()

c3 = c1+c2
c3.print_complex_num()

