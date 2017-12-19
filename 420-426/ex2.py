'''import the libs'''
'''此练习的要求时在瞬间t=251-300的期间内r的变化和nt之间的关系图'''
'''r为某一值时，y轴代表的时t从251到300期间nt的变化范围'''
import matplotlib.pyplot as plt

def logistic_growth(k,r,n0,t):
    nt=n0
    datax=[]
    datay=[]

    datax.append(r)
    datay.append(nt)

    for i in range(t):
        nt=nt+r*nt*(1.0-nt/k)
        datax.append(i+1)
        datay.append(nt)

    return (datay)

bifX=[]
bifY=[]
'''因为r最大为3，所以i的范围是1到201'''
'''[i/100.0+1.0]是list中的一个元素'''
for i in range(201):
    dataY=logistic_growth(100.0,i/100+1.0,0.01,300)
    bifX=bifX+([i/100.0+1.0]*50)
    bifY=bifY+dataY[251:301]

plt.plot(bifX,bifY,'.')

plt.xlabel("r")
plt.ylabel("Population size")

plt.show()