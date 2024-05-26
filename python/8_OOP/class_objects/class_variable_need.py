class person:
    def __init__(self):
        self.count = 0
        self.count += 1

    def get_data(self):
        print("Counter: ", self.count)

p1 = person()
p1.get_data()

p2 = person()
p2.get_data()
