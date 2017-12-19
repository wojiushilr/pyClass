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

hist, bins = np.histogram(df_ravenna['wind_deg'],8,[0,360])

def showRoseWind(values,city_name,max_value):
	N = 8
	
	# theta = [pi*1/4, pi*2/4, pi*3/4, ..., pi*2]
	theta = np.arange(0.,2 * np.pi, 2 * np.pi / N)
	radii = np.array(values)
	# 绘制极区图的坐标系
	plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
	
	# 列表中包含的是每一个扇区的 rgb 值，x越大，对应的color越接近蓝色
	colors = [(1-x/max_value, 1-x/max_value, 0.75) for x in radii]
	
	# 画出每个扇区
	plt.bar(theta, radii, width=(2*np.pi/N), bottom=0.0, color=colors)
	
	# 设置极区图的标题
	plt.title(city_name, x=0.2, fontsize=20)
	plt.show()
def RoseWind_Speed(df_city):
    # degs = [45, 90, ..., 360]
	degs = np.arange(45,361,45)
	tmp = []
	for deg in degs:
	    # 获取 wind_deg 在指定范围的风速平均值数据
		tmp.append(df_city[(df_city['wind_deg']>(deg-46)) & (df_city['wind_deg']<deg)]
		['wind_speed'].mean())
	return np.array(tmp)

showRoseWind(RoseWind_Speed(df_ravenna),'Ravenna',max(hist))
