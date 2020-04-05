from math import sqrt
print ("giải phương trình bậc 2")
a=float(input("nhập a"))
b=float(input("nhập b"))
c=float(input("nhập c"))

if a==0:
    print("phương trình có nghiệm x ", -c/b)

else:
    delta = b**2-4*a*c
    if delta==0:
        print ("phương trình có nghiệm x1=x2= ", -b/(2*a))
    elif delta>0:
        print("phương trình có nghiệm x1= ", (-b+sqrt(delta))/(2*a))
        print("phương trình có nghiệm x2= ", (-b-sqrt(delta))/(2*a))
    else:
        print ("phương trình vô nghiệm")

