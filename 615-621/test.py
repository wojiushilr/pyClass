import matplotlib.pyplot as plt
import numpy as np
import random as rnd

N = 3
K = 2
LAMBDA= 0.1
def ca_1d(l, t, n, k, rule, cell_i):
    cell = cell_i
    data = [cell]
    for i in range(t):
        cell_next = [0 for i in range(l)]
        for j in range(l):
            neighboringstate = 0
            for m in range(k):
                neighboringstate += cell[int((j + (m - (k - 1) / 2) + l) % l)] * (n ** (k - 1 - m))

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
#RULE= [(0 if rnd.random()<(1.0-LAMBDA) else rnd.randint(1, N-1)) for i in range(N**K)]

# [0, 0, ..., 0, 1, 0, ..., 0, 0]
cell_init = [0 for i in range(L)]
cell_init[L // 2] = 1
# random
# cell_init= [rnd.randint(0, 1) for i in range(L)]
dataXY = ca_1d(L, T, N, K, RULE, cell_init)

def calcEntropy(data):
    dic= {}
    for d in data:
        if d in dic:
            dic[d]= dic[d]+1
        else:
            dic[d]= 1
    probdist= np.array(list(dic.values()))/(float)(len(data))
    return(np.sum([-p * np.log2(p) for p in probdist]))

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
    dimension = len(data)
    result = []
    for j in range(0,dimension):
        data_j = [dataXY[i][j] for i in range(len(dataXY))]
        data_X = data_j[0:dimension-1]
        data_Y = data_j[1:dimension]
        result.insert(j,calcMI(data_X,data_Y))
    return result

def calcCAMI(data):
    result = calcCAMIList(data)
    return np.sum(result)/len(data)

#x = [1,0,1,1,0]
#y = [0,1,1,0,1]


#print calcEntropy(x)
#print calcJointEntropy(x,y)
#print calcMI(x,y)
print (calcCAMIList(dataXY))
print (calcCAMI(dataXY))

X = np.arange(0,1.01,0.01)
Y = calcCAMIList(dataXY)
plt.xlabel("LAMBDA")
plt.ylabel("MI")
plt.plot(X,Y)


fig = plt.figure(figsize=(5, 6))
ax = fig.add_subplot(1, 1, 1)
#ax.pcolor(np.array(dataXY), vmin = 0, vmax = 1, cmap= plt.cm.binary)
ax.pcolor(np.array(dataXY), vmin = 0, vmax = N-1)
ax.set_xlim(0, L)
ax.set_ylim(T - 1, 0)
ax.set_xlabel("cell number")
ax.set_ylabel("step")
ax.set_title("Rule=" + str(RNO) +"  MI=" + str(calcCAMI(dataXY)))
plt.show()

