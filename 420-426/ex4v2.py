'''import the libs'''
import matplotlib.pyplot as plt
'''function setting'''
def logistic_growth(ra,rb,pt0,na0,nb0,t,da,db,s):
    na=na0
    nb=nb0
    pt=pt0
    a=0.2
    datax=[]
    datay1=[]
    datay2=[]
    datay3=[]
    datay4=[]
    datax.append(0)
    datay1.append(na0)
    datay2.append(nb0)
    datay3.append(na0+nb0)
    datay4.append(pt0)
    for i in range(t-1):
        ntta = na
        nttb = nb
        x = ntta + nttb
        q = da * ntta + db * nttb
        na = ntta + a * ntta * (ra - x - da * pt)
        nb = nttb + a * nttb * (rb - x - db * pt)
        pt = pt + a * pt * (q - s)

        datax.append(i + 1)
        datay1.append(na)
        datay2.append(nb)
        datay3.append(x)
        datay4.append(pt)
    return (datax,datay1,datay2,datay3,datay4)
'''ra,rb,pt0,na0,nb0,t,da,db,s'''
dataX,dataY1,dataY2,dataY3,dataY4=logistic_growth(0.8,0.5,0.1,0.1,0.1,3000,0.8,0.1,0.1)

'''plot graph'''

#plt.plot(dataY1,dataY2)
plt.figure(1)
plt.plot(dataX,dataY1)
plt.plot(dataX,dataY2)
plt.plot(dataX,dataY3)
plt.plot(dataX,dataY4)
plt.title("ra=0.8,rb=0.5,pt0=0.1,na0=0.1,nb0=0.1,t=3000,da=0.8,db=0.1,s=0.1")
plt.xlabel("t")
plt.ylabel("Population size")
plt.legend(["NA","NB","NA+NB","P"])

plt.figure(2)
plt.plot(dataY1,dataY2)
plt.title("ra=0.8,rb=0.5,pt0=0.1,na0=0.1,nb0=0.1,t=3000,da=0.8,db=0.1,s=0.1")
plt.xlabel("NA")
plt.ylabel("NB")

plt.figure(3)
plt.plot(dataY4,dataY1)
plt.title("ra=0.8,rb=0.5,pt0=0.1,na0=0.1,nb0=0.1,t=3000,da=0.8,db=0.1,s=0.1")
plt.xlabel("P")
plt.ylabel("NA")


plt.show()