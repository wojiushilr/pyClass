#!/bin/python3

import sys

'''
arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
'''


arr = [["1","8","3","4","5","6"],
       ["1", "2", "3", "4", "5", "6"],
       ["1", "2", "3", "4", "5", "6"],
       ["1", "2", "3", "4", "5", "6"],
       ["1", "2", "3", "4", "5", "6"],
       ["1", "2", "3", "4", "5", "6"]]
print(arr[0][0:3])



s = []
sum1 = 0
i = 0
j = 0

for i in range(3):
    print("i",i)

    for j in range(3):
        #print("j",j)

        #sum1 = sum(arr[i][j:int(j)+2])
        print(arr[i][j:int(j)+3])


s.append(sum1)
print(s)


