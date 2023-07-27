lines = []
f = open("myfile.txt", "r")
lines = f.read()
lines_noK = []
for line in lines:
    for character in line:
        print(character)
        if character != "o" and character != "O":
            lines_noK.append(character)

f = open("myfile.txt", "w")
f.writelines(lines_noK)
f.close()