# Take up at 40

# Bonus if you can create it as a function

# input: 4 integers
# output: string

num = []

for n in range(4):
    number = int(input())
    num.append(number)

def check_if_telemarketer(num):
    if num[0] == 8 or num[0] == 9:
        if num[3] == 8 or num[-1] == 9:
            if num[1] == num[2]:
                return False
    else:
        return True

result = check_if_telemarketer(num)

if result == False:
    print("ignore")
else:
    print("answer")






