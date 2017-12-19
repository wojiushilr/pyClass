'''import the libs'''
import matplotlib.pyplot as plt

def logistic_growth(k=100,r=1.0,n0=1.0,t=20):
    nt=n0
    datax=[]
    datay=[]

    datax.append(0)
    datay.append(nt)

    for i in range(t):
        nt=nt+r*nt*(1.0-nt/k)
        datax.append(i+1)
        datay.append(nt)

    return (datax,datay)

dataX,dataY=logistic_growth(r=0.8)
plt.plot(dataX,dataY)

dataX,dataY=logistic_growth(r=1.9)
plt.plot(dataX,dataY)

dataX,dataY=logistic_growth(r=2.7)
plt.plot(dataX,dataY)

plt.xlabel("Time")
plt.ylabel("Population size")
plt.legend(["r=0.8","r=1.9","r=2.7"])
plt.show()