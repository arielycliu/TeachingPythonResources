# Method - called with object.operatorName()
#   - methods are called on the object
# Function - call with functionName()
#   - call and pass an object thru them


# Creating Classes

class Cat(object): # Class

    def __init__(self, name, age): # Constructor: initiate the attributes
        self.name = name
        self.age = age
        self.species = "Cat" # hard code for every object

    def talk(self): # Method (similair to functions)
        print("Meow")
        print("Hello I'm", self.name)
        print("I am", self.age, "years old")

    def change_age(self, age): # Change attribute outside of init
        self.age = age

# Creating object
Pudding = Cat("Pudding", 7)
print(Pudding.age)

Pudding.change_age(5)
print(Pudding.age)



# Pudding.talk()  # Running method
# print(Pudding.species)  # Calling attribute directly
#
# # Deleting objects and attributes
# del Pudding.species
# print(Pudding.species)
# # Attributes - variables of an object
