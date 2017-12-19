import matplotlib.pyplot as plt

#for Canopy users
import matplotlib.animation as animation

#for EPD users
#matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
import random as rnd


# “TypeError: 'float' object cannot be interpreted as an integer” '/ 'change to '//'  use the '// 'floor division operator:
def gtypeToPtype(gtype):
   return (np.sum([gtype[i]*(2**i) for i in range(L)])//float(2**L-1))

def fitnessFunction(p):
   return(p**2)

def fitnessFunction2(p):
   return(np.sin(17.0*p)*np.cos(35.0*p)+1.5)

## define classes
class Agent(object):

    def __init__(self, gtype):
        self.genotype= gtype[:]
        self.phenotype= None
        self.fitness= 0.0

    def getOffspring(self):
        o= Agent(self.genotype)

        for i in range(L):
            if (rnd.random()<MUT):
                o.genotype[i]= 1-o.genotype[i]

        return(o)

    def develop(self, dfunc):
        self.phenotype= dfunc(self.genotype)

    def evaluate(self, efunc):
        self.fitness= efunc(self.phenotype)

def selectAnAgentByRoulette(pop):
    total= sum([i.fitness for i in pop])
    val= rnd.random()*total
    for i in pop:
        val-= i.fitness
        if (val<0):
            return(i)
'''
def selectAnAgentByTournament(pop):
    a1= pop[rnd.randint(0, len(pop)-1)]
    #a1= rnd.choice(pop)
    a2= rnd.choice(pop)
    if(a1.fitness>a2.fitness):
        return(a1)
    else:
        return(a2)'''

'''
def selectAnAgentByRank(pop):
    pop.sort(lambda x, y: int(x.fitness-y.fitness))
    rank= range(N, 0, -1)

    total= sum(rank)
    val= rnd.random()*total
    for i in range(N):
        val-= rank[i]
        if (val<0):
            return(pop[i])'''

def crossover(a1, a2):
    point= rnd.randint(1, L-2)
    for i in range(point, L):
        a1.genotype[i], a2.genotype[i]= a2.genotype[i], a1.genotype[i]

def update(t):
    fig.clear()
    ax1= fig.add_subplot(2, 1, 1)
    ax1.plot(averageFitness)
    ax1.set_title('g = ' + str(t))
    ax1.plot(bestFitness)
    ax1.set_xlabel("generaiton")
    ax1.set_ylabel("average / best fitness")
    ax2= fig.add_subplot(2, 1, 2)
    ax2.plot(sx, sy)
    ax2.plot(pp, pf, ".")
    ax2.set_xlabel("x")
    ax2.set_ylabel("fitness")
    fig.tight_layout()
'''
# setup for visualization
fig = plt.figure()


def update(time):
    fig.clear()

    ax1= fig.add_subplot(2, 1, 1)
    ax1.plot(averageFitness)
    ax1.set_title('g = ' + str(time))
    ax1.plot(bestFitness)

    ax2= fig.add_subplot(2, 1, 2)
    x= [a.phenotype[0] for a in population]
    y= [a.phenotype[1] for a in population]
    ax2.plot(x, y, "o")
    ax2.imshow(SZ, origin='lower', extent=[-500, 500, -500, 500])
'''
#initialization
SEED=101
N= 100
G= 100
L= 20
MUT= 0.001
T=100
CROSS= 0.2
rnd.seed(SEED)
population= [Agent([rnd.randint(0, 1) for j in range(L)]) for i in range(N)]

fig= plt.figure()
#some variables for graphs
averageFitness= []
bestFitness= []
best= population[0]
sx= np.arange(0, 1.01, 0.01)
sy= [fitnessFunction(i) for i in sx]
pp= []
pf= []



# main loop (call back function for animation)
def main_loop(t):
    step()
    update(t)

# events in a step
def step():
    global population, pp, pf
    #fitness evaluation
    best= population[0]

    for a in population:
        a.develop(gtypeToPtype)
        a.evaluate(fitnessFunction)

        if(a.fitness>best.fitness):
            best= a
    averageFitness.append(np.average([a.fitness for a in population]))
    bestFitness.append(best.fitness)

    pp= [a.phenotype for a in population]
    pf= [a.fitness for a in population]

    print (str(best.genotype)+":"+str(best.fitness))
    #evolution
    newpop= []
    for i in range(N//2):
        n1= selectAnAgentByRoulette(population).getOffspring()
        n2= selectAnAgentByRoulette(population).getOffspring()

        if rnd.random()<CROSS:
            crossover(n1, n2)
        newpop.append(n1)
        newpop.append(n2)
    population= newpop



#for Canopy users
ani = animation.FuncAnimation(fig, main_loop, np.arange(0, T), interval=25, repeat=False)
plt.show()


#for EPD users
#for i in range(T):
#    main_loop(i)
#    fig.canvas.manager.window.update()
#    fig.show()
#fig.canvas.manager.window.wait_window()