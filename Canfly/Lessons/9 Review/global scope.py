

def function1():
    global num # how to write to a global variable inside a function
    num = 10

    m = num   # local inside of function
    # you can't write to global variables within a function (without the global keyword)
    # You can read global variable inside of a function (as long as you don't have a local variable with the same name)
    return m

num = 9    # global outside of function
print(function1())
print(num)


# Summary: tldr
# Local variable: inside of function
# Global variables: outside of function
#
# Cannot write global variables in function - unless using global declaration
# Can read global variables in function - as long as there is not a local variable with the same name






























