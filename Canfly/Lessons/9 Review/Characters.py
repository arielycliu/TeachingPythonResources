
# Manipulating strings


'''
ord: 32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47
chr:      !   "   #   $   %   &   '   (   )   *   +   ,   -   .   /
ord: 48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63
chr:  0   1   2   3   4   5   6   7   8   9   :   ;   <   =   >   ?
ord: 64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79
chr:  @   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O
ord: 80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95
chr:  P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _
ord: 96  97  98  99  100 101 102 103 104 105 106 107 108 109 110 111
chr:  `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o
ord: 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
chr:  p   q   r   s   t   u   v   w   x   y   z   {   |   }   ~
'''


print(ord("A"))   # Returns the ord code
print(chr(97))    # Returns the characters

# Caesar cipher decoder function
# Input: sentence all caps, with spaces
# Output: decoded version
# Key: -9
# Input: QNUUX FXAUM
# Output: HELLO WORLD

# Take up at 5:40

def decrypt(string, key):
    for char in string:
        if char != " ":
            code = ord(char) + key
            if code < 65:
                code += 26
            if code > 90:
                code -= 26

            print(chr(code), end="")

        else:
            print(" ", end="")


string = list(input())
key = -9

decrypt(string, key)





























