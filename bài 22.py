mydict={"name":"Tien Anh", "age":22, "size":15}

class Class1:
    def __init__(self):
        self.values= ""

    def Nhap(self):
        self.values= input("Nhập cmmd")

    def Check(self):
        print(self.values in mydict)

c1= Class1()
c1.Nhap()
c1.Check()


