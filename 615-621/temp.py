import matplotlib.pyplot as plt
import numpy as np
import random as rnd

def ca_1d(k,n,l, t, rule, cell_i):
    cell= cell_i
    data= [cell]
    for i in range(t):
        cell_next= [0 for i in range(l)]
        for j in range(l):
            #neighboringstate= cell[(j-1+l)%l]*4+cell[j]*2+cell[(j+1)%l]
            neighboringstate = 0
            for m in range(k):
                neighboringstate =neighboringstate + cell[int(j+(m-(k-1)/2)+l)%l]*(n**(k-1-m))
            #print('j=',j,neighboringstate)
            cell_next[j]= rule[int(neighboringstate)]
        cell= cell_next #cell_nextをcellに割り当て
        data.append(cell)
        #print(neighboringstate)
        #print(data)
    return(data)
'''
neighboringstate= 0
for m in range(k):
    neighboringstate+= cell[(j+(m­(k­1)/2)+l)%l]*(n**(k­1­m))'''
L=51 #cell数
T=50 # Ca的回数
SEED=100 #
rnd.seed(SEED)
LAMBDA = (9-3.901)/9
K=3 #neighbor
N=2 #status
RNO= 90#ルールの通し番号を表す
#RULE = [(RNO >> i) & 1 for i in range(N**K)]
RULE= [(0 if rnd.random()<(1.0-LAMBDA) else rnd.randint(1,N-1)) for q in range (N**K)]
print(RULE)
#[0, 0, ..., 0, 1, 0, ..., 0, 0]
#cell_init= [0 for i in range(L)] #セルの初期状態
#セルの初期状態,0からN­1までの値をランダムに取る
cell_init = []
for i in range(L):
    cell = rnd.randint(0,N-1)
    cell_init.append(cell)
print(cell_init)

#random
#cell_init= [rnd.randint(0, 1) for i in range(L)]
dataXY= ca_1d(K,N,L, T, RULE, cell_init)

fig= plt.figure(figsize=(5, 6))
ax= fig.add_subplot(1,1,1)
ax.pcolor(np.array(dataXY), vmin = 0, vmax =  N-1,  cmap= plt.cm.binary)
#ax.pcolor(np.array(dataXY), vmin = 0, vmax =N-1)
ax.set_xlim(0, L)
ax.set_ylim(T-1, 0)
ax.set_xlabel("cell number")
ax.set_ylabel("step")
ax.set_title("rule" + str(RNO))
plt.show()
'''
b = [4,16,36]
print(np.log2(b))'''
