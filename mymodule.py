# module
def greeting(name):
    print("tên tôi là: ", name)


import mymodule
mymodule.greeting("Tien Anh")

import platform
x=dir(platform)
print(x)

y=platform.system()
print(y)

import datetime
z=datetime.datetime.now()
print(z)
print(z.year)