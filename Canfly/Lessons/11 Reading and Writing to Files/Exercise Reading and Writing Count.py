# For every "hello" in the file, write a goodbye at the end
# read file
# count hello's
# write correct number of goodbyes in file

# Take up at 6:10

f = open("notes.txt", "r")
lines = f.read()

countHello = lines.count("Hello")

f = open("notes.txt", "a") # append
for i in range(countHello):
    f.write("Goodbye\n")

f.close()


open()
read()
readline()
write()
writelines()
count()
find()











