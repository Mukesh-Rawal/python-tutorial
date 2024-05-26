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


shape = None
while True:
    print("Enter s to find area of square: ")
    print("Enter c to find area of cube: ")
    print("Enter e to exit: ")
    ch = input("Enter your choice: ")

    if ch =="s":
        shape = square(int(input("Enter side of square: ")))

    elif ch =="c":
        shape = cube(int(input("Enter side of cube: ")))

    elif ch =="e":
        break

    else:
        print("Wrong input")

    if shape is not None:
        shape.find_area()
        print(shape)
