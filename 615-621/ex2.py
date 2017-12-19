import matplotlib.pyplot as plt
import numpy as np
import random as rnd

def ca_1d(l, t, rule, cell_i):
    cell = cell_i
    data = [cell]
    for i in range(t):
        cell_next = [0 for i in range(l)]
        for j in range(l):
            neighboringstate = cell[(j - 1 + l) % l] * 4 + cell[j] * 2 + cell[(j + 1) % l]
            cell_next[j] = rule[neighboringstate]
        cell = cell_next
        data.append(cell)
    return (data)

L = 101
T = 100
SEED = 100
rnd.seed(SEED)
RNO = 90
RULE = [(RNO >> i) & 1 for i in range(8)]
# [0, 0, ..., 0, 1, 0, ..., 0, 0]
cell_init = [0 for i in range(L)]
cell_init[L // 2] = 1
# random
# cell_init= [rnd.randint(0, 1) for i in range(L)]
dataXY = ca_1d(L, T, RULE, cell_init)

def calcEntropy(data):
    dic= {}
    for d in data:
        if d in dic:
            dic[d]= dic[d]+1
        else:
            dic[d]= 1
    probdist= np.array(list(dic.values()))/(float)(len(data))
    return(np.sum([-p * np.log2(p) for p in probdist]))
# p(x,y)的意义是：比如1,0 // 0,1 // 1,1 // 1,0 // 0,0 //以上5中情况，那么p(1，0)的值为1,0出现的概率=2/5
def calcJointEntropy(x,y):
    dic = {(0,0):0, (0,1):0, (1,0):0, (1,1):0}
    for i in range(len(x)):
        if x[i] == 0 and y[i] == 0:
            dic[(0,0)] = dic[(0,0)] + 1
        if x[i] == 0 and y[i] == 1:
            dic[(0,1)] = dic[(0,1)] + 1
        if x[i] == 1 and y[i] == 0:
            dic[(1,0)] = dic[(1,0)] + 1
        if x[i] == 1 and y[i] == 1:
            dic[(1,1)] = dic[(1,1)] + 1
    probdist = np.array(list(dic.values())) / (float)(len(x))
    result = 0
    for i in probdist:
        if i == 0:
            continue
        else:
            result += -i * np.log2(i)
    return result

def calcMI(x, y):
    return calcEntropy(x) + calcEntropy(y) - calcJointEntropy(x,y)

def calcCAMIList(data):
    d = len(data)
    result = []
    for j in range(0,d):
        data_j = [dataXY[i][j] for i in range(len(dataXY))]
        data_X = data_j[0:d-1]
        data_Y = data_j[1:d]
        result.insert(j,calcMI(data_X,data_Y))
    return result

def calcCAMI(data):
    result = calcCAMIList(data)
    return np.sum(result)/len(data)
'''
x = [1,0,1,1,0]
y = [0,1,1,0,1]


print (calcEntropy(x))
print (calcJointEntropy(x,y))
print (calcMI(x,y))
print (calcCAMIList(dataXY))
print (calcCAMI(dataXY))'''



fig = plt.figure(figsize=(9, 5))
plt.figure(1)
ax1=plt.subplot(131)#在图表1中创建子图1
ax2=plt.subplot(132)#在图表1中创建子图2
ax3=plt.subplot(133)
plt.sca(ax1)
X = range(0,len(dataXY),1)
Y = calcCAMIList(dataXY)
plt.xlabel("cell number")
plt.ylabel("MI")
plt.plot(X,Y)
plt.sca(ax2)
ax2.pcolor(np.array(dataXY), vmin=0, vmax=1, cmap=plt.cm.binary)
ax2.set_xlim(0, L)
ax2.set_ylim(T - 1, 0)
ax2.set_xlabel("cell number")
ax2.set_ylabel("step")
ax2.set_title("Rule=" + str(RNO) +"  MI=" + str(calcCAMI(dataXY)))

plt.sca(ax3)
plt.xlabel("λ")
plt.ylabel("MI")
#X=
#Y = calcCAMI(dataXY)
plt.show()


