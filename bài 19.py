#in ra các số chẵn

values=input("Nhập cmmd")
chan= [x for x in values.split(",") if int(x)%2==0]
print(",".join(chan))

