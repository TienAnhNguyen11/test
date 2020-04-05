class Ex2:
    def __init__(self, list1, list2):
        self.list1= list1
        self.list2= list2
        self.tong=0
    def sum(self):
        for x in self.list1:
            self.tong +=x

    def append(self):
        self.list2.append(self.tong)
    def sum2(self):
        for a in self.list2:
             self.tong +=a

list1=[1,2,3]
list2=[4,5,6]
p1=Ex2(list1, list2)
p1.sum()
p1.sum2()
print (p1.tong)