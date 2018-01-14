#!/bin/python3

import sys
import copy
def miniMaxSum(arr):
    # Complete this function
    s = []
    for i in arr:
        #print("arr",arr)
        temp0 = copy.deepcopy(arr)
        temp0.remove(i)
        temp1 = temp0
        #print(temp1)
        s.append(sum(temp1))

    s.sort()
    print(s[0],s[4])

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
