import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import itertools
import math
def ca_1d(l, t, rule, cell_i):
    cell= cell_i
    data= [cell]
    for i in range(t):
        cell_next= [0 for i in range(l)]
        for j in range(l):
            neighboringstate= cell[(j-1+l)%l]*4+cell[j]*2+cell[(j+1)%l]
            cell_next[j]= rule[neighboringstate]
        cell= cell_next #cell_nextをcellに割り当て
        data.append(cell)
    return(data)
#一次元データの系列をリストで受け取り，そのエントロピーを返す関数calcEntropy(data)を作成
def calcEntropy(data):
    dic= {}
    for d in data:
        if d in dic:
            dic[d]= dic[d]+1
        else:
            dic[d]= 1
    probdist= np.array(list(dic.values()))/(float)(len(data))
    #	In python3, dict.values returns a dict_values object,
    # which is not a list or tuple. Try coercing that into a list. total_minutes = list(total_minutes_by_account.values())
    return(np.sum([-p * np.log2(p) for p in probdist]))


def calcJointEntropy(X,Y):

   probdist = []
   for c1 in set(X):
        for c2 in set(Y):
            probdist.append(np.mean(np.logical_and(X == c1, Y == c2)))

   return np.sum(-p * np.log2(p) for p in probdist if p > 0)


def calcMI(x, y):
    return
def calcCAMIList(data):
    return
def calcCAMI(data):
    return

L=101 #cell数
T=100 # Ca的回数
SEED=100 #
rnd.seed(SEED)

RNO= 90#ルールの通し番号を表す
RULE= [(RNO>>i)&1 for i in range(8)]

#[0, 0, ..., 0, 1, 0, ..., 0, 0]
cell_init= [0 for i in range(L)] #セルの初期状態
cell_init[L//2]= 1

#random
#cell_init= [rnd.randint(0, 1) for i in range(L)]
dataXY= ca_1d(L, T, RULE, cell_init)

fig= plt.figure(figsize=(5, 6))
ax= fig.add_subplot(1,1,1)
ax.pcolor(np.array(dataXY), vmin = 0, vmax = 1,  cmap= plt.cm.binary)
ax.set_xlim(0, L)
ax.set_ylim(T-1, 0)
ax.set_xlabel("cell number")
ax.set_ylabel("step")
ax.set_title("rule" + str(RNO))
plt.show()

a = ['hello', 'world', 123]
print (tuple(a))

datatemp2 = [[1,1,1,0,1,1,1],[1,0.5,0,0,1,0,0.5]]
datatemp2 = np.array(datatemp2)
print(calcEntropy(datatemp2[1]))
print(calcJointEntropy(datatemp2[0],datatemp2[1]))