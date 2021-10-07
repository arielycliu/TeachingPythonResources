def most_frequent(lines):
    print(lines)
    print(lines.count)
    return max(lines, key=lines.count)


line = input()
lines = []
while line != '###':
    words = line.lower().split()
    for i in words:
        lines.append(i)
    line = input()

print(most_frequent(lines))