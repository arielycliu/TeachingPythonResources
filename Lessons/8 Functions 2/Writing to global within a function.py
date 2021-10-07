
# Writing to a global variable
def xChange(val):
    global num
    # global variableName
    num = val

# Global variable num
num = 88
xChange(3)
print(num)