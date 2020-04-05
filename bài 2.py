class Ex3:
    def __init__ (self, list1, list2):
        self.list1=list1
        self.list2=list2
        self.sum= 0

    def sum1(self):
        for x in self.list1:
            self.sum+=x

    def append1(self):
        self.list2.append(self.sum)

    def sum2(self):
        for y in self.list2:
            self.sum+=y

list1 = [1,2,3,4,5]
list2 = [7,8,9]
p1= Ex3(list1, list2)
p1.sum1()
p1.sum2()
print (p1.sum)