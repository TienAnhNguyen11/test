# đếm số chữ cái và chữ số
s=input("Nhập chuỗi cmmd:")
d= {"chữ":0 , "số":0 }
for x in s:
    if x.isdigit():
        d["số"]+=1

    elif x.isalpha():
        d["chữ"]+=1

    else:
        pass

print('số chữ cái là:',d["chữ"])
print("số chữ số là: ", d["số"])
