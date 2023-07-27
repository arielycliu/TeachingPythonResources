
count = 0
while True:
    line = input()
    if line == "END":
        break # breaks the loop
    elif line == "SKIP":
        continue
    print("read")
print("OUTSIDE OF LOOP")


