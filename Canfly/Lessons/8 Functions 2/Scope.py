
def squared(x):
    # local variable inside of the function
    # when inside a function you USUALLY cannot change global variables
    localvar = x*x
    return localvar

globalvar = 7
threeSquare = squared(3)

print("Num is " + str(num))
print("threeSquare is " + str(threeSquare))






