class father():
    def __init__(self, name, age):
        self.name= name
        self.age=age

    def printname(self):
        print("tên tôi là: ", self.name)

    def printage(self):
        print("tôi năm nay: ", self.age)

f1= father("Steven Gerrard", 41)
f1.printname()
f1.printage()

class son(father):
    pass

x= son("Daniel Gerrard", 12)
x.printname()
x.printage()

class daughter(father):
    def __init__(self, name, age):
        father.__init__(self, name, age)

y= daughter("Natt Gerrard",8)
y.printname()
y.printage()