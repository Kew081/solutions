def fib(n):
    # returns nth term in fibonacci sequence
    x, y = 0, 1
    for i in range(1, n):
        x, y = y, x + y
    return x
