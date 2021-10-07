# Pig Latin
# Move the first letter to the end of the word
# add "ay" to the end of the word

# Input: Cat
# Output: atcay

# Input: funky
# Output: unkyfay

string = input()
print(string[1:] + string[0] + "ay")

