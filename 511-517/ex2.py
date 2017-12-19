import  matplotlib.pyplot as plt
import  numpy as np
#import sys
data= np.loadtxt("nagoya.txt")
#print(type(data))
#矩阵转置,data[ i ]はi列目全体を表すリストを示し
data= data.transpose()
#data[i]的数据重组为51*12的数组，例如data[1]为年，data[2]为月
#tdata[ i ] [ j ] [k]は，”列iに関する1963年から数えてj年目のk+1月の値"が入っています
tdata= [data[i].reshape(51,12) for i in range(6)]

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
x=range(1963,2014)
y=[]
temp=0
for j in range(51):
    for k in range(12):
      temp=temp+tdata[2][j][k]
    temp=temp/12
    y.append(temp)

print(x)
plt.plot(x,y)
plt.xlabel("year")
plt.ylabel("average temperature")
plt.show()