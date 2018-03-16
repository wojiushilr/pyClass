#!/bin/python3

import sys

def factorial(n):
    # Complete this function
    k = n
    if n > 1:
        return k*factorial(n-1)
    else:
        return k

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)