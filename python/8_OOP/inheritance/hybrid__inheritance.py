class a:
    def m1(self):
        print("M1 method")

class b(a):
    def m2(self):
        print("m2 method")

class c:
    def m3(self):
        print("m3 method")

class d(c, b):
    def m4(self):
        print("m4 method")


d =d()
d.m1()
