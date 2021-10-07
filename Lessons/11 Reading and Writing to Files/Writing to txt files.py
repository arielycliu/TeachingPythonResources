f = open("notes.txt", "w") # w - overwrites

f.read()
f.readline()
f.write()
f.writelines()

sentence = "I like blueberries"
f.write(sentence) # Writes a piece of string

l = ["I like blueberries\n", "My cat doesn't listen to me\n", "I despise data management\n"]
f.writelines(l) # Writes a list






