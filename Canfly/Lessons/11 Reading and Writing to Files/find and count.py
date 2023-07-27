# .find() .count() string methods
s = "hello"
print(s.find("o")) # find: returns index of char in string
print(s.find("5")) # when it isn't there returns -1

print(s.count("l")) # counts instances of char
print(s.count("4")) # returns 0

str = input("Check username: ")
if str.count("_") > 0:
    print("INVALID USERNAME")
else:
    print("VALID USERNAME")
