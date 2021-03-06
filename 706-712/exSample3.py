#参数调整的temp
import matplotlib
#for Canopy users
import matplotlib.animation as animation
#for EPD users
#matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
import random as rnd

# set parameters
N= 500
T= 10
W= 30
SEED=101
agents= []

#TH=0.3
colorlist=['red', 'blue']


## define functions
def clip(x):
  if x<0:
    return(x+W)
  elif x>=W:
    return(x-W)
  else:
    return(x)

## define classes
class Agent(object):
  def __init__(self, sp):
   self.x= rnd.randint(0, W-1)
   self.y= rnd.randint(0, W-1)
   self.p= sp
   self.s= 0

  def randomwalk(self):
   self.x+= rnd.randint(-100, 100)
   self.y+= rnd.randint(-100, 100)
   self.x= clip(self.x)
   self.y= clip(self.y)

  def isOverlapped(self):
   for a in agents:
     if((a.x==self.x and a.y==self.y) and (a!=self)):
        return(True)
   return(False)

  def findNewSpace(self):
   self.randomwalk()
   if(self.isOverlapped()==True):
      self.findNewSpace()

  def updateSatisfaction(self):
    neighbors= [a for a in agents \
        if (abs(a.x-self.x)<=1 and \
            abs(a.y-self.y)<=1) and a!=self]
    neighborsCount= len(neighbors)

    sameCount= len([a for a in neighbors \
                    if (a.p==self.p)])
    self.s= (float(sameCount)/float(neighborsCount) \
                    if neighborsCount!=0 else 0.0)

  def seek(self):
   self.updateSatisfaction()
   if(self.s<TH):
      self.findNewSpace()

# initialize variables
rnd.seed(SEED)
agents=[Agent(i%2) for i in range(N)]
for a in agents:
   a.findNewSpace()


# main loop (call back function for animation)
def main_loop(t):
   step()
   #update(t)

# events in a step
def step():
   rnd.shuffle(agents)
   for a in agents:
      a.seek()
   averageSatisfaction.append(np.average([a.s for a in agents]))

# update function for graph
def update(t):
    fig.clear()
    ax1= fig.add_subplot(2, 2, 1)
    x= [a.x for a in agents]
    y= [a.y for a in agents]
    c=[colorlist[a.p] for a in agents]
    ax1.scatter(x, y, color=c)
    ax1.axis([-1, W, -1, W])
    ax1.set_title('t = ' + str(t))
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax2= fig.add_subplot(2, 2, 3)
    s= [a.s for a in agents]
    ax2.hist(s, 10)
    ax2.set_xlabel('satisfaction')
    ax2.set_ylabel('frequency')
    ax3= fig.add_subplot(2, 2, 4)
    ax3.plot(averageSatisfaction)
    ax3.set_xlabel('t')
    ax3.set_ylabel('averageSatisfaction')
    plt.tight_layout()
#for Canopy users
#ani = animation.FuncAnimation(fig, main_loop, np.arange(0, T), interval=25, repeat=False)
lastaverageSatisfaction=[]
Th = np.linspace(0.1,1,num=10)
for i in range(len(Th)):
 TH= Th[i]
 averageSatisfaction=[]
 for j in range(T):
   main_loop(j)
   #print(len(averageSatisfaction))
 #print(averageSatisfaction)
 lastaverageSatisfaction.append(averageSatisfaction[9])

#print(Th)
#print(lastaverageSatisfaction)

fig = plt.figure()
plt.plot(Th,lastaverageSatisfaction)
plt.xlabel("th")
plt.ylabel("lastAverageSatisfaction")
plt.show()
