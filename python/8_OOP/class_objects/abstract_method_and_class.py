from abc import ABC, abstractmethod

class a(ABC):
    def m1(self):
        print("m1 method")

    @abstractmethod
    def m2(self):
        pass

class b(a):
    def m2(self):
        print("M2 method")

    def m3(self):
        print("m3 method")

b = b()
b.m1()
b.m2()
b.m3()
