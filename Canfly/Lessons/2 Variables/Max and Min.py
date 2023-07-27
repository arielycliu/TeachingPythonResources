# Task: Find the Range of three numbers
# Input: three numbers
# Output: Range

# Range = max - min
# max()
# min()

n = int(input())
m = int(input())
l = int(input())

Biggest = max(n, m, l)
Smallest = min(n, m, l)
Range = (Biggest - Smallest)
print(Range)

# + - /