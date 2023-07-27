# Area of Circle Calculator

# Input: Radius
# Output: Area, (Circumference)

# pi * r^2

import math
pi = math.pi
radius = float(input("Enter your radius: "))
area = pi * (radius ** 2)
print(area)