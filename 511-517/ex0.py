#implement of gaussian distribution
#μ=0 σ=1
import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
ax1=plt.subplot(221)#分成2x2，占用第一个，即第一行第一列的子图
ax2=plt.subplot(222)#在图表1中创建子图2
ax3=plt.subplot(223)#在图表1中创建子图2
ax4=plt.subplot(224)#在图表1中创建子图2

plt.sca(ax1)
mu = 0
sigma = 1
x1= np.random.randn(100)
y1= np.random.randn(100)
plt.scatter(x1, y1)


plt.sca(ax2)
y2 = np.random.randn(100)
'''pl t .hi st(y ,  n)は配列yの中の要素でヒストグラムをつくる関数．このときデータをn個の階級に分ける（省略可）．
np.random.randn(x)は，標準正規分布（平均0，分散1）からランダムに生成したx個の実数値からなるnp.array配列を返す関数で
す．hi st関数は，配列の中身から自動的に分布を計算してグラフをつくります'''
plt.hist(y2,10)
plt.xlabel("y")

plt.sca(ax3)
x2 = np.random.randn(100)
print(x2)
plt.hist(x2,10)
plt.xlabel("x")

plt.sca(ax4)
# 第一个参数是x轴坐标
# 第二个参数是y轴坐标
# 第三个参数是要显式的内容 
plt.text(0.5,0.8,'subplot words',color='blue',ha='center')
plt.show()