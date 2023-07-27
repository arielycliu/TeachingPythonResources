# Overloading
# add, sub, str
# eq, gt, ge, lt, le
checkX = p1 > p2

class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


p1 = point(1, 2)
p2 = point(3, 1)
p3 = p1 + p2

print(p3)



