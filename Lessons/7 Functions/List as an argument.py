# Passing a list as an argument
# def printList(food):
#     for f in food:
#         print(f)
#
#
# listFood = ["kiwi", "lemon", "melon"]
# printList(["kiwi", "lemon", "melon"])

# Arbitrary Arguments
# When you don't know how many arguments there are

def foods(*fruits):
    print(fruits[1])

foods("apple", "berry", "grape")












