class square:
    def __init__(self, side):
        self.side = side

    def find_area(self):
        self.area = self.side ** 2
        print("Area of square: ", self.area)


class cube(square):
    def __init__(self, side):
        square.__init__(self, side)

    def find_area(self):
        self.area = 6 * self.side ** 2
        print("Area of cube: ", self.area)


s = square(int(input("Enter the side of square: ")))
s.find_area()

c = cube(int(input("Enter the side of cube: ")))
c.find_area()
