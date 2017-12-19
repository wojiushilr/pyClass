import matplotlib
#for Canopy users
import matplotlib.animation as animation
#for EPD users
#matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
TH=np.linspace(0,1,num=11)
temp =[]
for i in range(len(TH)):
    #TH=TH[i]
    print(TH[i])
    temp.append(TH[i])

print("temp",temp)