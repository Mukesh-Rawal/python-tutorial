class a:
    def msg1(self):
        print("Hello")

class b:
    def msg2(self):
        print("Hi")

class c(b, a):
    pass
    #print("Bye")


c = c()
c.msg1()
