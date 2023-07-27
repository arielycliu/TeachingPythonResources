import random
n = random.randint(0,20)
print(n)

guess = int(input())

while guess != n:
    print("Guess again")
    if guess > n:
        print("Try smaller")
    else:
        print("Try bigger")
    guess = int(input())

print("Correct")