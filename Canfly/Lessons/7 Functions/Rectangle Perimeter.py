# Call a function within a function

def perimeter(width, height):
    p = timesTwo(width) + timesTwo(height)
    return p

def timesTwo(n):
    return n*2

print(perimeter(3, 5))







