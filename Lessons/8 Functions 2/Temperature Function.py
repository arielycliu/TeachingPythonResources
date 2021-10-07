# Two arguments: temperature, type
# Create a function that convert temperature in C to F and vice versa

# C = (F - 32) * 5/9
# F = C * (9/5) + 32

def tempConvertor(temp, type):
    if type == "C":
        # Convert to F
        Ftemp = temp * (9/5) + 32
        print(str(Ftemp) + " F")
    else:
        # Convert to C
        Ctemp = (temp - 32)*(5/9)
        print(str(Ctemp) + " C")

tempConvertor(23.5, "F")
# Output: 101.084 F

# Take up at 5:30