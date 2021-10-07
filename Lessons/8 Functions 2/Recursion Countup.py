# Recursive function
# Countup instead till a certain number


# Take up at 6:12


def countup(num):
    # Base case
    if num == 0:
        print("Starting")
    else:
        countup(num - 1) # recursive portion
        print(num)


countup(5)

