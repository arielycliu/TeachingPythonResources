fruits = ["apples", "bananas", "melon", "grapes"]
print(fruits)

# Loop thru lists
for f in fruits:
    print(f)
    if f == "melon":
        fruits.remove("melon")


print(fruits)