
class circle :
    import numpy
    def __init__(self,x,y,r) : 
        self.x = x
        self.y = y
        self.r = r
    
    def pos(self) :
        print(f"좌표 : ({self.x},{self.y})")

    def area(self) :
        self.area = numpy.math.pi * self.r**2
        print(self.area)

a = circle(3,4,5)
a.pos()
a.area()