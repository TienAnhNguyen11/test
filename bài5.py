from math import sqrt
class ptbh:
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def myfunc(self):
        if self.a==0:
            x=-self.c/self.b
            print("phương trình có nghiệm ",x)

        else:
            d= self.b**2-4*self.a*self.c
            x= -self.b/(2*self.a)
            x1= (-self.b+sqrt(d))/(2*self.a)
            x2= (-self.b-sqrt(d))/(2*self.a)

            if d==0:
                print("phương trình có nghiệm ",x)

            elif d>0:
                print("phương trình có nghiệm x1= ", x1)
                print("phương trình có nghiệm x2= ", x2)

            else:
                print("phương trình vô nghiệm")

p1= ptbh(1,-4,4)
p1.myfunc()



