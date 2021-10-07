# Lists are mutable

# Changing elements in list
nums = [3, 6, 9]
nums[:2] = [1, 2]
print(nums)

# Joining lists
secondNums = [7, 2, 4]
combinedList = nums + secondNums
print(combinedList)

# Appending
# nameOfList.append(value)
combinedList.append(0)
print(combinedList)

# Pop function
# nameOfList.pop(index)
combinedList.pop(6)
print(combinedList)

# Remove function
combinedList.remove(2)
print(combinedList)  # only removes the first instant
# nameOfList.remove(value)


















