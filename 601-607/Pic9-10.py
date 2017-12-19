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

#把日期数据转换成 datetime 的格式
day_milano = [parser.parse(x) for x in x1]

# 调用 subplot 函数
fig, ax = plt.subplots()
plt.xticks(rotation=70)
hours = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hours)
ax.plot(day_milano ,y1, 'r')
# dist 是一个装城市距离海边距离的列表
dist = [df_ravenna['dist'][0],
	df_cesena['dist'][0],
	df_faenza['dist'][0],
	df_ferrara['dist'][0],
	df_bologna['dist'][0],
	df_mantova['dist'][0],
	df_piacenza['dist'][0],
	df_milano['dist'][0],
	df_asti['dist'][0],
	df_torino['dist'][0]
]

# temp_max 是一个存放每个城市最高温度的列表
temp_max = [df_ravenna['temp'].max(),
	df_cesena['temp'].max(),
	df_faenza['temp'].max(),
	df_ferrara['temp'].max(),
	df_bologna['temp'].max(),
	df_mantova['temp'].max(),
	df_piacenza['temp'].max(),
	df_milano['temp'].max(),
	df_asti['temp'].max(),
	df_torino['temp'].max()
]

# temp_min 是一个存放每个城市最低温度的列表
temp_min = [df_ravenna['temp'].min(),
	df_cesena['temp'].min(),
	df_faenza['temp'].min(),
	df_ferrara['temp'].min(),
	df_bologna['temp'].min(),
	df_mantova['temp'].min(),
	df_piacenza['temp'].min(),
	df_milano['temp'].min(),
	df_asti['temp'].min(),
	df_torino['temp'].min()
]

fig, ax = plt.subplots()
ax.plot(dist,temp_max,'ro')
plt.xlabel("Distence")
plt.ylabel("Temperature")
plt.title("Interaction between distence and temperature")
plt.show()