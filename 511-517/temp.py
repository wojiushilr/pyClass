import matplotlib.pyplot as plt
import numpy as np

data= np.loadtxt("nagoya.txt")
print(type(data))
data= data.transpose()
tdata= [data[i].reshape(51,12) for i in range(6)]
print(type(tdata))
#设置画布大小，添加子图
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)

y=[]
for j in range(51):
 for k in range(12):
      #x.append(tdata[0][j][k])
      y.append(tdata[2][j][k])

#plt.plot(y)
#设置x刻度
ax.set_xticks(range(0,6))
#设置y刻度
ax.set_xticklabels(['1963','1973','1983','1993','2003','2013'])
plt.show()