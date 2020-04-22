#in số ngày của tháng
m= int(input("Nhập tháng"))
a=[1,3,5,7,8,10,12]
def check():
    if m==2:
        print("28 ngày nhé")
    elif m in a:
        print("31 nhé bro")
    else:
        print("30 ạ")
check()