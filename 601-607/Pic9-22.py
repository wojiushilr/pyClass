import numpy as np
import pandas as pd
import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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


size = w
colors =z

plt.scatter(x,y,s=size,c=colors,alpha=50, marker=(9, 3, 30))
plt.xlabel("WindSpeed")
plt.ylabel("Temperature")
plt.title("Humidity")
plt.colorbar()
plt.show()
#风速和温度越高，湿度越低