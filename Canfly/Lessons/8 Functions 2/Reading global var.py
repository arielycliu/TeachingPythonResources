# You can read a global variable from inside of a function
# IF there is NO local variable with the same name

# Global variable
favFood = "pizza"

def orderFood(amount):
    # amount is local
    favFood = "hot dogs" # first local then global
    print("I'd like " + str(amount) + " " + favFood)

orderFood(5)

# Can read a global variable but can't edit, inside of a function

def changeVar(newVal):
    newVal = 0 # can't affect global

n = 6
changeVar(n)
print(n)









