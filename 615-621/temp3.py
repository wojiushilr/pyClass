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

def getRule(r):
    RULE= [(0 if rnd.random()<(1.0-r) else rnd.randint(1,N-1)) for q in range (N**K)]
    return RULE

'''
x = [1,0,1,1,0]
y = [0,1,1,0,1]
print (calcEntropy(x))
print (calcJointEntropy(x,y))
print (calcMI(x,y))
print (calcCAMIList(dataXY))
print (calcCAMI(dataXY))'''
#parameter setting
L=101 #cell数
T=50 # Ca的回数
SEED=100 #
rnd.seed(SEED)
LAMBDA = np.linspace(0,1,100)
K=5 #neighbor
N=4 #status
#RNO= 90#ルールの通し番号を表す
#RULE = [(RNO >> i) & 1 for i in range(N**K)]
#RULE= [(0 if rnd.random()<(1.0-LAMBDA) else rnd.randint(1,N-1)) for i in range (N**K)]
# [0, 0, ..., 0, 1, 0, ..., 0, 0]
#セルの初期状態,0からN­1までの値をランダムに取る
cell_init = []
for i in range(L):
    cell = rnd.randint(0,N-1)
    cell_init.append(cell)
print(cell_init)

mi=[]
for k in range(100):
    rule = getRule(LAMBDA[k])
    #print(rule)
    dataXY = ca_1d(K, N, L, T, rule, cell_init)
    temp = calcCAMI(dataXY)
    print(temp)
    mi.append(temp)
print(mi)

# random
# cell_init= [rnd.randint(0, 1) for i in range(L)]
#dataXY= ca_1d(K,N,L, T, RULE, cell_init)
#print(LAMBDA)

#picture plot
fig = plt.figure(figsize=(9, 5))

X = LAMBDA
Y = mi
plt.xlabel("λ")
plt.ylabel("MI")
plt.plot(X,Y)
plt.show()



