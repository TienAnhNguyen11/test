#tìm điểm gần gốc tọa độ
a= list(input("nhập a:"))
b= list(input("nhập b:"))
c= list(input("nhập c:"))
if ((int(a[0]))**2+(int(a[1]))**2)>((int(b[0]))**2+(int(b[1]))**2):
    if ((int(b[0]))**2+(int(b[1]))**2)>((int(c[0]))**2+(int(c[1]))**2):
        print("c gần hơn")
    else:
        print("b gần hơn")
else:
    if ((int(a[0]))**2+(int(a[1]))**2)>((int(c[0]))**2+(int(c[1]))**2):
        print("c gần hơn")
    else:
        print("a gần hơn")