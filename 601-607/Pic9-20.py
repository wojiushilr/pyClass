hist, bin = np.histogram(df_ferrara['wind_deg'],8,[0,360])
showRoseWind(hist,'Ferrara', max(hist))