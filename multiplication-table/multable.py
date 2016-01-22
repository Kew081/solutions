#!/usr/bin/env python3

def multable():
    # prints easy to read multiplication table for numbers 1-12
    for num in range(1, 13):
        for i in range(1, 13):
            print(str(i * num).rjust(4), end='')
        print()

if __name__ == '__main__':
    multable()
