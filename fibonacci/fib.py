#!/usr/bin/env python3

def fib(n):
    # returns nth term in fibonacci sequence
    x, y = 0, 1
    for i in range(1, n):
        x, y = y, x + y
    return x

if __name__ == '__main__':
    print(fib(10))
