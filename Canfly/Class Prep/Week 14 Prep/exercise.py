#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

num = []

for n in range(4):
    num.append(int(input()))

def check_if_telemarketer(a, b, c, d):
    if a == 8 or a == 9:
        if d == 8 or d == 9:
            if b == c:
                return False
    else:
        return True

val = check_if_telemarketer(num[0], num[1], num[2], num[3])

if val == False:
    print("ignore")
else:
    print("answer")


