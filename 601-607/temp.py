
#normal distribution center at x=0 and y=5
import numpy as np
import pandas as pd
import datetime
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
from dateutil import parser

df_ferrara = pd.read_csv('ferrara_270615.csv')
df_milano = pd.read_csv('milano_270615.csv')
df_mantova = pd.read_csv('mantova_270615.csv')
df_ravenna = pd.read_csv('ravenna_270615.csv')
df_torino = pd.read_csv('torino_270615.csv')
df_asti = pd.read_csv('asti_270615.csv')
df_bologna = pd.read_csv('bologna_270615.csv')
df_piacenza = pd.read_csv('piacenza_270615.csv')
df_cesena = pd.read_csv('cesena_270615.csv')
df_faenza = pd.read_csv('faenza_270615.csv')

wind = df_ravenna['wind_speed']
temp = df_ravenna['temp']
hum = df_ravenna['humidity']
windd=df_ravenna['wind_deg']
#print(wind)
w=np.array(wind)
t=np.array(temp)



print(w)
#风速和温度越高，湿度越低

hist2d(w ,t, bins=20, norm=LogNorm())

colorbar()

show()
'''


import numpy as np
import pandas as pd
import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
from dateutil import parser

df_ferrara = pd.read_csv('ferrara_270615.csv')
df_milano = pd.read_csv('milano_270615.csv')
df_mantova = pd.read_csv('mantova_270615.csv')
df_ravenna = pd.read_csv('ravenna_270615.csv')
df_torino = pd.read_csv('torino_270615.csv')
df_asti = pd.read_csv('asti_270615.csv')
df_bologna = pd.read_csv('bologna_270615.csv')
df_piacenza = pd.read_csv('piacenza_270615.csv')
df_cesena = pd.read_csv('cesena_270615.csv')
df_faenza = pd.read_csv('faenza_270615.csv')

wind = df_ravenna['wind_speed']
temp = df_ravenna['temp']
hum = df_ravenna['humidity']
windd=df_ravenna['wind_deg']
#print(wind)

x=[]
y=[]
z=[]
w=[]
x.append(wind)
y.append(temp)
z.append(hum)
w.append(windd)
x=np.array(x)
y=np.array(y)
z=np.array(z)
N = int(len(z)**.5)
z = z.reshape(N, -1)
plt.imshow(z+10, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)),
        cmap=cm.hot, norm=LogNorm())
plt.colorbar()
plt.xlabel("Wind_speed")
plt.ylabel("Temperature")

plt.show()
#风速和温度越高，湿度越低
'''