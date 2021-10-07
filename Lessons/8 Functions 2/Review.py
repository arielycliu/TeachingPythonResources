# Defining Functions
def greeting():
    print("Hi")

# Calling functions
greeting()

# Using arguments
def greeting(name):
    print("Hi " + name)
greeting("Ari")

# Using Return
def greeting(name):
    return "Hi " + name
print(greeting("Ari"))

# Lists as an argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Arbitrary arguments
def students(*names):
    print("The third child is " + names[2])

students("Emil", "Tobias", "Linus")