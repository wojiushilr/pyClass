import  matplotlib.pyplot as plt
import  numpy as np

data= np.loadtxt("nagoya.txt")
data= data.transpose()
#data[i]的数据重组为51*12的数组，例如data[1]为年，data[2]为月
#tdata[ i ] [ j ] [k]は，”列iに関する1963年から数えてj年目のk+1月の値"が入っています
tdata= [data[i].reshape(51,12) for i in range(6)]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
x=[]
a=[]
b=[]
c=[]
for k in range(12):
      #x.append(tdata[0][j][k])
      temp=tdata[2][0][k]
      if temp < 5:
        a.append(temp)
      elif 5<temp<=25:
        b.append(temp)
      else:
        c.append(temp)
#获取a,b,c对应个数
a=len(a)
b=len(b)
c=len(c)
print(a,b,c)
x=[a,b,c]
labels=['T=<5','5<T<=25','25<T']
plt.pie(x,labels=labels)
plt.show()
