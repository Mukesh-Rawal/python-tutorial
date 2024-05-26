class square:
    def __init__(self, side):
        self.side = side

    def find_area(self):
        self.area = self.side ** 2

    def __str__(self):
        return("Area of square: " + str(self.area))

class cube(square):
    def __init__(self, side):
        square.__init__(self, side)

    def find_area(self):
        self.area = 6 * self.side ** 2

    def __str__(self):
        return("Area of cube: " + str(self.area))


shapes = [square(int(input("Enter the side of square: "))), cube(int(input("Enter the side of cube: ")))]

for shape in shapes:
    shape.find_area()
    print(shape)
