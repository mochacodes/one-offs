def fib(n: int):
    if (n <= 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)


arg = input("enter a num: ")
print(fib(int(arg)))