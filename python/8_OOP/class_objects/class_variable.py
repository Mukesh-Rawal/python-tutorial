class person:
    count = 0
    def __init__(self):
        person.count += 1

    def get_data(self):
        print("Counter: ", self.count)

p1 = person()
p1.get_data()

p2 = person()
p2.get_data()

p3 = person()
p3.get_data()
