#!/bin/python3

import sys


n = int(input().strip())

#to binary

#print(type(bin(n)))
#print(n_bin_list[2:])

numbers = str(bin(n)[2:]).split('0')
print(numbers)
lenghts = [len(num) for num in numbers]
print(max(lenghts))



