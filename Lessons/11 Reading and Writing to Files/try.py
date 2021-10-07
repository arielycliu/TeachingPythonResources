l = input().split()

for n in l:
    try:
        num = int(n)
    except:
        print("Input four numbers")
        break

try:
    l[3]
except:
    print("Need four inputs")