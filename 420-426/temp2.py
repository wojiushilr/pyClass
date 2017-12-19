'''import the libs'''

import matplotlib.pyplot as plt

def logistic_growth(r,n0,p0,t):
    nt=n0
    pt=p0
    a=0.2
    s=0.1
    da=0.2
    q=da*nt
    datax=[]
    datay1=[]
    datay2=[]
    datax.append(0)
    datay1.append(nt)
    datay2.append(pt)

    for i in range(t):
        ntt=nt
        nt=ntt+a*ntt*(r-nt-da*pt)
        pt=pt+a*pt*(q-s)
        datax.append(i+1)
        datay1.append(nt)
        datay2.append(pt)
    return (datax,datay1,datay2)

dataX,dataY1,dataY2=logistic_growth(0.1,0.11,0.1,5000)
plt.plot(dataX,dataY1)
plt.plot(dataX,dataY2)

plt.xlabel("t")
plt.ylabel("Population size")

plt.show()