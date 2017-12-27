import re
import numpy as np

a=input()
b=a.split(" ")
n=int(b[0])
k=int(b[1])
#init m
m = np.zeros((n,k))
m = m.tolist()
for i in range(n):

     temp = input()
     temp = temp.split(" ")
     #print(temp[1])
     for n in range(len(temp)):
         m[i][n] = temp[n]




print(m)
