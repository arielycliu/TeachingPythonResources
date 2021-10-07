# Have two lists, combine them

nums = [1, 2, 3]
letters = ['a', 'b', 'c']

# Combine the two lists, by alternate taking elements
# [1, a, 2, b, 3, c]

combinedList = []

for n in range(len(nums)):
    combinedList.append(nums[n])
    combinedList.append(letters[n])

print(combinedList)

