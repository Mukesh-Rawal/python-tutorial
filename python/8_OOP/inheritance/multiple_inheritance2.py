class a:
    def msg1(self):
        print("Hello")

class b:
    def msg2(self):
        print("Hi")

class c(a, b):
    pass


c = c()
c.msg2()
