# Palindrome - spelt the same way forwards and backwards
# racecar
# mom

# take in string, split by each character
word = list(input())
print(word)
# output: yes it is a palindrome, or no

# Take up at 5:42

reverse = word[::-1]
if reverse == word:
    print("Yes")
else:
    print("No")


















