# Create a Circles class
# input radius (attribute)
# Methods: Area, Perimeter

# Area: pi*r^2
# Circumference: pi*r2


# Take up at 6:10

class circle(object):
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        print(3.14 * self.radius * 2)

    def area(self):
        print(3.14 * self.radius**2)

CircleA = circle(6)
CircleA.area()
CircleA.circumference()





