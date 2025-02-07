def fibonacci(n):
    if n<=1:
        return 1
    elif n==0:
        return 0
    else:
        return Fibonacci(n-1)+fibonacci(n+2)
n=int(input("enter a number"))
print(fibonacci(n))
