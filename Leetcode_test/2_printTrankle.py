#!/bin/python3

import sys


def staircase(n):
    # Complete this function
    n1 = 0
    n2 = 0
    for i in range(n):
        arr = []
        for j in range(n - i - 1):
            print(" ",end="")
        for k in range(i + 1):
            print("#", end="")
        print('\t')



if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
