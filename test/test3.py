class Triangle():
    def __init__(self, angle1, angel2, angle3):
        self.angle1= angle1
        self.angle2= angel2
        self.angle3= angle3

    def check_angles(self):
        summ = self.angle1+self.angle2+self.angle3
        if summ==180:
            print ("đúng")
        else:
            print("sai")


class1= Triangle(30,60,90)
class1.check_angles()