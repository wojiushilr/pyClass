import matplotlib.pyplot as plt
import numpy as np
import random as rnd

data = [0, 1, 0, 1, 1]
dic= {}
for d in data:
    if d in dic:
        dic[d]= dic[d]+1
    else:
        dic[d]= 1
#probdist= np.array(dic.values())/(float)(len(data))
#	In python3, dict.values returns a dict_values object,
# which is not a list or tuple. Try coercing that into a list. total_minutes = list(total_minutes_by_account.values())
a=np.array([1,1,1])
c=[1,1,1]
b = 2
print(np.array(list(dic.values()))/2)
print(a)
print(a*b)
print(c*b)