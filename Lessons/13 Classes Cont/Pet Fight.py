# 3 pets for each player
# 2 players  turn based game

# For each pet: hp, ad
# Check in 10 mins (6:08) - create the turns

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
    print("Lizard2 is dead")
    del Lizard2


#while True:
    #input() - who's attacking
    #input()  - who's getting attacked
    # Update hp
    # Check for death
    # Repeat with other player



