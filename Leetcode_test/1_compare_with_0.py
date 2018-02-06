#!/bin/python3

import sys


def plusMinus(arr):
    # Complete this function
    l = len(arr)
    np = 0
    nn = 0
    nz = 0
    for i in arr:
        if i > 0:
            np += 1
        elif i < 0:
            nn += 1
        else:
            nz += 1
    print(np / l, end='\n')
    print(nn / l, end='\n')
    print(nz / l)


if __name__ == "__main__":
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        plusMinus(arr)
