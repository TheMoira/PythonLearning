#from helps import *
import helps

helps.title("Classes")

#lowercase letters always for functions
#uppercase letters always for classes

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print("draw")

point1 = Point(5,6)
point1.r = 10
point1.fi = 20
#doesnt matter that neither r nor fi are defined in class

print(point1.r)

class RedPoint(Point):
    def __init__(self, x, y):
        Point(x,y)

    def drawred(self):
        print("I am red")


red = RedPoint(3,4)
red.draw()
red.drawred()