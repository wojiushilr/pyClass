import  matplotlib.pyplot as plt
import  numpy as np

data= np.loadtxt("nagoya.txt")
print(type(data))
#矩阵转置,data[ i ]はi列目全体を表すリストを示し
data= data.transpose()
#data[i]的数据重组为51*12的数组，例如data[1]为年，data[2]为月
#tdata[ i ] [ j ] [k]は，”列iに関する1963年から数えてj年目のk+1月の値"が入っています
tdata= [data[i].reshape(51,12) for i in range(6)]

#设置画布大小，添加子图
fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot(111)
#全年にわたる気温の変化の推移を示した折れ線グラフ
#print(tdata[3][0][0]),out:16.7
x=[]
y=[]
for j in range(51):
 for k in range(12):
      x.append(tdata[0][j][k])
      y.append(tdata[2][j][k])


print(y)
plt.plot(y)
#ax.set_xticks(x)
ax.set_xticklabels(['1963','1963','1971','1979','1988','1996','2004','2013'])
plt.xlabel("year")
plt.ylabel("temperature")
#ax.set_axis_off()
plt.show()
print(list(zip([1, 3, 5], [2, 4, 6])))