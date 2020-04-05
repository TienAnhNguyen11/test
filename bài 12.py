class Class1:
    def __init__(self):
        self.chuoi=""

    def nhap(self):
        self.chuoi = input("nhập cmmd") 

    def inhoa(self):
        print(self.chuoi.upper())

Str1= Class1()
Str1.nhap()
Str1.inhoa()
