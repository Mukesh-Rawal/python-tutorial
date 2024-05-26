class Students:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
        #self.per = str((self.phy + self.che + self.math) / 3) + "%"

    #def percentage(self):
        #self.newPer = str((self.phy + self.che + self.math) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.che + self.math) / 3) + "%"

stu1 = Students(88,87,90)
print(stu1.percentage)

stu1.phy = 95
print(stu1.phy)

print(stu1.percentage)

