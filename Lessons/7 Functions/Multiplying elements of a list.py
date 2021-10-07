# Take in list as argument
# Output the numbers multiplied together

# Take up at 6:13ish

def multiply(*nums):
    sum = 1
    for n in nums:
        sum *= n
    return sum

print(multiply(1,2,3))










