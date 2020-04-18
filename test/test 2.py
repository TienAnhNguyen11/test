#ptbh
def division(a,b):
    return a/b
try:
    print(division(1,0))
except ZeroDivisionError:
    print("lỗi a ơi")
finally:
    print("học lại toán lớp 1 đi")
