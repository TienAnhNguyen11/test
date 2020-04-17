def centuryFromYear(year):
    a=year/100
    if (year%100)==0:
        print(int(a))
    else:
        century= int(a)+1
        print(int(century))

centuryFromYear(1710)