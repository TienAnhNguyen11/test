# đếm chữ in hoa và chữ thường
s= input("Nhập đi oppa:")
d={"chữ hoa":0, "chữ thường":0}
for x in s:
    if x.islower():
        d["chữ thường"]+=1

    elif x.upper():
        d["chữ hoa"] +=1

    else:
        pass

print("số chữ hoa: ", d["chữ hoa"])
print("số chữ thường: ", d["chữ thường"])