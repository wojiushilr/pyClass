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