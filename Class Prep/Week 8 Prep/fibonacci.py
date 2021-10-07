def Fib(n):
    if (n==1 or n==2):
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

n = 8
for i in range(1, n+1):
    print(Fib(i))