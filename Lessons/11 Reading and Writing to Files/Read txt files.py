
# Prep the file
f = open("notes.txt", "r")
# a - append, write to the end of the file
# w - overwrite, overwrite everything in the file
# r - reading the file
# x - create the file

# open("filename", "mode")
# read(), readline()
# read(index) - reads everything

print(f.read(5))
f.readline()

f.close()