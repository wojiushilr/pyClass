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
for j in range(51):
  for k in range(12):
      #x.append(tdata[0][j][k])
      y.append(tdata[3][j][k])

print(y)
plt.hist(y,20)

plt.show()