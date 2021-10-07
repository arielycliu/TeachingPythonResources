# Recursion: calling function x within function x
# The function calls itself

def countdown(num):
    #print("Starting countdown function #: " + str(num))

    # Base case: when to exit
    # Make sure base case is meet
    if num <= 0:
        print("Finished!")
    # Regular case: it's calling itself
    else:
        print(num)
        countdown(num - 2)
    #print("Exiting countdown function #: " + str(num))

countdown(50)


