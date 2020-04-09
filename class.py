class Person():
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def inten(self):
        print("ten toi là: ", self.name)

    def tuoi(self):
        print("toi nam nay: ", self.age)

p1= Person("John", 27)
p1.inten()
p1.tuoi()


