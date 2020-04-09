x= lambda a: a+10
print(x(5))

y=lambda a,b: a*b+10
print(y(7,8))

#lambda function

def myfunc(n):
    return lambda a:a*n

mydoubler = myfunc(2)
print(mydoubler(11))