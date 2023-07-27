string = list(input())
key = int(input())
def decrypt(string, key):
    for char in string:
        if char != " ":
            code = ord(char) + key
            if code > 90:
                code = code - 26
            if code < 65:
                code = code + 26
            print(chr(code), end="")
        else:
            print(" ", end = " ")

print(string)
decrypt(string, key)