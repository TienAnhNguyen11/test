# kiểm tra số nguyên tố
N= int(input("Nhập N: "))
if N==1:
    print("k là snt")
elif N==2:
    print("là snt")
else:
    for i in range(2,N):
        if N%i==0:
            print("k là snt")
            break
        else:
            print("là snt")
            break