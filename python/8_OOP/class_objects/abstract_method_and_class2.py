from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self):
        self.area = 0

    @abstractmethod
    def find_area(self):
        pass

class square(shape):
    def __init__(self, side):
        shape.__init__(self)
        self.side = side

    def find_area(self):
        self.area = self.side ** 2

    def __str__(self):
        return "Area of square: " + str(self.area)

class rectangle(shape):
    def __init__(self, l, b):
        shape.__init__(self)
        self.l = l
        self.b = b

    def find_area(self):
        self.area = self.l * self.b

    def __str__(self):
        return "Area of rectangle: " + str(self.area)

s = square(5)
s.find_area()
print(s)

s = rectangle(4,6)
s.find_area()
print(s)
