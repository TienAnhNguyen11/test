# tính 1*3*5+3*5*7+...+n(n+2)(n+4)
n= int(input("Nhập n: "))
s=[]
for i in range(n+1):
    if i%2!=0:
        a= i*(i+2)*(i+4)
        s.append(a)
        S=sum(s)
print(S)