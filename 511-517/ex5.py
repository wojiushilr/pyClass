import  matplotlib.pyplot as plt
import  numpy as np

data= np.loadtxt("nagoya.txt")
data= data.transpose()
#data[i]的数据重组为51*12的数组，例如data[1]为年，data[2]为月
#tdata[ i ] [ j ] [k]は，”列iに関する1963年から数えてj年目のk+1月の値"が入っています
tdata= [data[i].reshape(51,12) for i in range(6)]


y1=tdata[2][0]
y2=tdata[3][0]
x=np.arange(0,12,1)
el= 0.3*np.abs(y1)#abs绝对值

fig = plt.figure(figsize=(6,4))
ax1 = fig.add_subplot(111)
ax1.errorbar(x,y1,yerr=el,ecolor='r',fmt='o-')
ax1.set_ylabel('average temperature')
ax2= ax1.twinx()
ax2.bar(x,y2)
plt.ylabel("average rain")
plt.xlabel("month")
plt.show()
