'''import the libs'''

import matplotlib.pyplot as plt

def logistic_growth(ra,rb,pt0,na0,nb0,t,da,db):
    na=na0
    nb=nb0
    pt=pt0
    a=0.2
    s=0.1
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
        ntta=na
        nttb=nb
        x=ntta+nttb
        q=da*ntta+db*nttb
        na=na+a*na*(ra-x-da*pt)
        nb=nb+a*nb*(rb-x-db*pt)
        pt=pt+a*pt*(q-s)
        '''..............................................'''
        datax.append(i+1)
        datay1.append(na)
        datay2.append(nb)
        datay3.append(x)
        datay4.append(pt)
    return (datax,datay1,datay2,datay3,datay4)
'''ra,rb,pt0,na0,nb0,t,da,db'''
data1X,data1Y1,data1Y2,data1Y3,data1Y4=logistic_growth(0.9,0.8,0.1,0.1,0.1,10000,0.9,0.1)
data2X,data2Y1,data2Y2,data2Y3,data2Y4=logistic_growth(0.9,0.8,0.1,0.1,0.1,10000,0.8,0.1)
data3X,data3Y1,data3Y2,data3Y3,data3Y4=logistic_growth(0.9,0.8,0.1,0.1,0.1,10000,0.7,0.1)
data4X,data4Y1,data4Y2,data4Y3,data4Y4=logistic_growth(0.9,0.8,0.1,0.1,0.1,10000,0.6,0.1)
plt.figure(1)
ax1=plt.subplot(211)#在图表1中创建子图1
ax2=plt.subplot(212)#在图表1中创建子图2
plt.figure(2)
ax3=plt.subplot(211)#在图表2中创建子图1
ax4=plt.subplot(212)#在图表2中创建子图2
#ax3=plt.subplot(223)#在图表2中创建子图1
#ax4=plt.subplot(224)#在图表2中创建子图2

plt.sca(ax1)
plt.plot(data1X,data1Y1)
plt.plot(data1X,data1Y2)
plt.plot(data1X,data1Y3)
plt.plot(data1X,data1Y4)
plt.xlabel("pt")
plt.ylabel("Population size")
plt.legend(["NA","NB","NA+NB","P"])

plt.sca(ax2)
plt.plot(data2X,data2Y1)
plt.plot(data2X,data2Y2)
plt.plot(data2X,data2Y3)
plt.plot(data2X,data2Y4)
plt.xlabel("pt")
plt.ylabel("Population size")
plt.legend(["NA","NB","NA+NB","P"])

plt.sca(ax3)
plt.plot(data3X,data3Y1)
plt.plot(data3X,data3Y2)
plt.plot(data3X,data3Y3)
plt.plot(data3X,data3Y4)
plt.xlabel("pt")
plt.ylabel("Population size")
plt.legend(["NA","NB","NA+NB","P"])

plt.sca(ax4)
plt.plot(data4X,data4Y1)
plt.plot(data4X,data4Y2)
plt.plot(data4X,data4Y3)
plt.plot(data4X,data4Y4)
plt.xlabel("pt")
plt.ylabel("Population size")
plt.legend(["NA","NB","NA+NB","P"])

plt.show()