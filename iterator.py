#iterator
mytuple=("Tien Anh", "dep trai", "coder")
myiter= iter(mytuple)

print(next(myiter))
print(next(myiter))
print(next(myiter))

mystr= iter(mytuple[1])
print(next(mystr))
print(next(mystr))
print(next(mystr))
print(next(mystr))
print(next(mystr))
print(next(mystr))
print(next(mystr))
print(next(mystr))


class numbers():
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        x=self.a
        self.a+=1
        return x

class1= numbers()
myit= iter(class1)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#stopIteration

class Myclass():
    def __iter__(self):
        self.b =1
        return self

    def __next__(self):
        if self.b <=30:
            y=self.b
            self.b+=1
            return y

        else:
            raise StopIteration

myclass=Myclass()
myiter1=iter(myclass)

for x in myiter1:
    print(x)
