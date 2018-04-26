# coding=utf-8
import sys

t = 5
arr = []

for i in range(t):
    arr.append(float(input()))

print(arr.index(max(arr)))
