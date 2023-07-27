# Guessing numbers game
# programs pick a random secret number
# User enters a guess and the program tells the user
# whether their number was too large or too small or correct

#6:00 I'll take it up

import random
n = random.randint(0, 20)
print(n)

guess = int(input())
while guess != n:
    if guess < n:
        print("Try bigger")
    else:
        print("Try smaller")
    print("Try again")
    guess = int(input())
print("Correct")


