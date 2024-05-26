class person:
    def __init__(self):
        self.msg = "Hello" # Instance variable

    def print_data(self):  # Instance Method
        print("Message: ", self.msg)


p1 = person()
p1.print_data()
