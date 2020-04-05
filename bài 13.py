#
values = []
for i in range(100,300):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) :
        values.append(i)

print (",".join(values))