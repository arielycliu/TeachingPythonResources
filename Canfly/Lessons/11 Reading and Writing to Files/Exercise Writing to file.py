# Read input from the user till they input END
# write the input from the user to the file

f = open("notes.txt", "w")


# Input below
while True:
    line = input()
    if line != "END":
        f.write(line)
    else:
        break
# Take up at 5:50





