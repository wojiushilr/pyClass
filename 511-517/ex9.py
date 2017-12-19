import  matplotlib.pyplot as plt
import  numpy as np
import pylab as pl
data= np.loadtxt("nagoya.txt")
data= data.transpose()

tdata= [data[i].reshape(51,12) for i in range(6)]

x=[]
y=[]
z=[]
for k in range(12):
 z.append([])
 for j in range(51):
      a=tdata[2][j][k]
      b=tdata[4][j][k]
      c=0.81*a+0.01*b*(0.99*a-14.3)+43.6
      x.append(a)
      y.append(b)
      z[k].append(c)

fig = plt.figure(figsize=(6,4))

matr = z
print(matr)
plt.pcolor(matr)
plt.colorbar()
plt.xlabel("year")
plt.ylabel("month")
plt.show()
