# Triangle Class
# Attribute (__init__)
# height, base
# Method - Area = height* base/2
# 5:30

class Triangle(object):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        print(self.height*self.base/2)

SampleTriangle = Triangle(6, 2)
SampleTriangle.area()
