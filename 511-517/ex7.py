import  matplotlib.pyplot as plt
import  numpy as np

data= np.loadtxt("nagoya.txt")
data= data.transpose()
#data[i]的数据重组为51*12的数组，例如data[1]为年，data[2]为月
#tdata[ i ] [ j ] [k]は，”列iに関する1963年から数えてj年目のk+1月の値"が入っています
tdata= [data[i].reshape(51,12) for i in range(6)]

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
x=[]
y=[]
z=[]
for k in range(12):
 for j in range(51):
      a=tdata[2][j][k] #t
      b=tdata[4][j][k] #h
      c=0.81*a+0.01*b*(0.99*a-14.3)+43.6
      x.append(a)#temp
      y.append(b)#humi
      z.append(c)

size = 50*(z)
colors =z
plt.scatter(x,y,s=size,c=colors)
plt.xlabel("temperature")
plt.ylabel("humidity")
plt.title("unhappiness")
plt.show()
