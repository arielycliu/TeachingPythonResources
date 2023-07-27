# Practice reading a txt file
# Print out each line of the text file
# But if it's the word "SKIP"
# Then don't print that line

# Hello World
# This is Ariel
# A cat walks across

# Take up at 5:35

f = open("notes.txt", "r")
for line in f:
    if line != "SKIP\n":
        print(line)
