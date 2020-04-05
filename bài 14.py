# đếm số có các chữ số là số chẵn
value =[]
for x in range(200,300):
    s=str(x)
    if (int(s[0]%2==0)) and (int(s[1]%2==0)) and (int(s[2]%2==0)):
        value.append(s)
print(','.join(value))


