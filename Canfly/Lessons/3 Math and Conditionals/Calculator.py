# Calculator
# Input: operator, two numbers
# Take in operator: +, -, *, /
# Take in two numbers and perform  the operation
# Output: Result

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
op = input("Enter operator: ")
if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
else:
    print(x / y)