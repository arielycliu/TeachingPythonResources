# hp, ad, armour


class pet():
    def __init__(self, hp, ad):
        self.hp = hp
        self.ad = ad

    def attack(self, victim):
        victim.hp = victim.hp - self.ad

Snake = pet(10, 15)
Turtle = pet(20, 5)
Lizard = pet(15, 10)

Snake2 = pet(10, 15)
Turtle2 = pet(20, 5)
Lizard2 = pet(15, 10)

Snake.attack(Lizard2)
print(Lizard2.hp)
if Lizard2.hp <= 0:
    print("he ded")
    del Lizard2






