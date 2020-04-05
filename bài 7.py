class Class1(object):
    def __init__(self):
        self.chuoi= ""

    def nhap(self):
        self.chuoi= input("nhập cmmd")

    def inhoa(self):
        print(self.chuoi.upper())

string= Class1()
string.nhap()
string.inhoa()