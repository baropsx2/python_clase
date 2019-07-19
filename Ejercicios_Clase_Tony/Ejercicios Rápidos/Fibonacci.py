"""
Sucesión de Fibonacci
fn = fn-1 + fn-2
n's son subíndices
fibonacci(6)

# First attempt
def fibonacci(numero):
    x = 0
    y = 1

    for i in range(numero):
        fib = y + x
        x = y
        y = fib
    print(x)
    return x

fibonacci(10)
"""


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(20))
fib(20)




