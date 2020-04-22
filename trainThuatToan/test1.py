#ước chung lớn nhất
a= int(input("Nhập a: "))
b= int(input("Nhập b: "))
n=[]
for i in range(1,a):
    if a%i==0 and b%i==0:
        n.append(i)
        UCLN= max(n)
print(UCLN)
