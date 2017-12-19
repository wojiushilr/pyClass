import matplotlib.pyplot as plt
import numpy as np
import random as rnd

def ca_1d(l, t, rule, cell_i):
    cell= cell_i
    data= [cell]
    for i in range(t):
        cell_next= [0 for i in range(l)]
        for j in range(l):
            neighboringstate= cell[(j-1+l)%l]*4+cell[j]*2+cell[(j+1)%l]
            #print('j=',j,neighboringstate)
            cell_next[j]= rule[neighboringstate]
        cell= cell_next #cell_nextをcellに割り当て
        data.append(cell)
    return(data)

L=11 #cell数
T=5 # Ca的回数
SEED=100 #
rnd.seed(SEED)

RNO= 90#ルールの通し番号を表す
RULE= [(RNO>>i)&1 for i in range(8)]
print(RULE)
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
b = [4,16,36]
print(np.log2(b))
for m in range(1):
    print('m',m)

j=5
l=11
print((j+1)%l)
print(rnd.randint(1,5))