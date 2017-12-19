# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import datetime
#matplotlib inline
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

# 取出我们要分析的温度和日期数据
y1 = df_milano['temp']
x1 = df_milano['day']
#print(x1)
#把日期数据转换成 datetime 的格式
day_milano = [parser.parse(x) for x in x1]
print(day_milano)
# 调用 subplot 函数
fig, ax = plt.subplots()
plt.xticks(rotation=70)
hours = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hours)
ax.plot(day_milano ,y1, 'r',linewidth=4)
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.legend(["milano"])
# 读取温度和日期数据
y1 = df_ravenna['temp']
x1 = df_ravenna['day']
y2 = df_faenza['temp']
x2 = df_faenza['day']
y3 = df_cesena['temp']
x3 = df_cesena['day']
y4 = df_milano['temp']
x4 = df_milano['day']
y5 = df_asti['temp']
x5 = df_asti['day']
y6 = df_torino['temp']
x6 = df_torino['day']

# 把日期从 string 类型转化为标准的 datetime 类型
day_ravenna = [parser.parse(x) for x in x1]
day_faenza = [parser.parse(x) for x in x2]
day_cesena = [parser.parse(x) for x in x3]
dat_milano = [parser.parse(x) for x in x4]
day_asti = [parser.parse(x) for x in x5]
day_torino = [parser.parse(x) for x in x6]

# 调用 subplots() 函数，重新定义 fig, ax 变量
fig, ax = plt.subplots(1,1)
plt.xticks(rotation=70)

hours = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hours)

#这里需要画出三根线，所以需要三组参数， 'g'代表'green'
ax.plot(day_ravenna,y1,'r',day_faenza,y2,'#00FF00',day_cesena,y3,'#8B0000',linewidth=2)
ax.plot(dat_milano,y4,'#F08080',day_asti,y5,'#4B0082',day_torino,y6,'y',linewidth=2)
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.legend(["ravenna","faenza","cesena","milano","asti","torino"])
#plt.savefig('power.png', dpi=75)
plt.show()