from math import sqrt
t=[6.31, 2.92, 2.35, 2.13, 2.02, 1.943, 1.895, 1.860, 1.833]  #Nhập list t

#bước 1:
a=[]
n= int(input("Nhập số lần đo: "))
for i in range(n):
    a.append(float(input("lần thứ %d:" %(i+1))))                   #đẩy các giá trị vừa nhập vào list a

#bước 2
s= sum(a)                                                          #tính tổng các giá trị đo
Stb= s/n                                                           # TB các giá trị đo

#bước 3: tính sai số dư và sai số TB bình phương
e=[]                                                                #list các sai số dư
b=0
for i in a:
    c= i-Stb
    e.append(c)
for i in range(0,len(e)):
    b+=e[i]**2
    Sm = sqrt(b/(n-1))
    M= t[n-2]*Sm

#bước 4: loại
for i in range(0, len(e)):
     if abs(e[i])>M:
          a.pop(i)                                          #loại bỏ giá trị với index i
s= sum(a)
Stb= s/(n-1)
print(Stb)
e=[]                                                                #list các sai số dư
b=0
for i in a:
    c= i-Stb
    e.append(c)
for i in range(0,len(e)):
    b+=e[i]**2
    Sm = sqrt(b/(n-2))
    M= t[n-2]*Sm
print(M)
