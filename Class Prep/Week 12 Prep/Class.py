


class Cat(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.l = [4.3, 6.4, 1.4]

    def speak(self):
        print("Hi I'm", self.name)
        print("I am", self.age, 'years old')
    def change_age(self, age):
        self.age = age
    def add_weight(self, weight):
        self.weight = weight

    def talk(self):
        print("Meow!")

class Dog(Cat):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        print("Bark!")


Husky = Dog("Husky", 5, "grey")
Husky.talk()
