# Reusing classes

class Cat(object):
    def __init__(self, name):
        self.name = name # belongs to instance
    def speak(self):
        print("Hi I'm", self.name)

class Dog(Cat): # inheritance copy over attributes and methods
    def __init__(self, name):
        super().__init__(name)

Husky = Dog("Husky")
Husky.speak()