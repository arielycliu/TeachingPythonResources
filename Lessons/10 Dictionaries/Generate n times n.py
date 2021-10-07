# Exercise: Generate Dictionary
# keys: 1, 2, 3, ... n
# values: 1*1, 2*2, 3*3, ... n*n

#dictName[key] = NewValue

# Try to get this done in 4 lines (don't need to ask for n input)
# Take up at 5:35

n = int(input())
dictVal = {}
for num in range(1, n+1):
    dictVal[num] = num*num
print(dictVal)

print(dictVal[6]) # Read values


dict2 = {n: n*n for n in range(6)}






















