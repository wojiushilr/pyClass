#from scipy.optimize import fsolve
'''
# 定义了第一条拟合直线
def line1(x):
	a1 = svr_lin1.coef_[0][0]
	b1 = svr_lin1.intercept_[0]
	return a1*x + b1

# 定义了第二条拟合直线
def line2(x):
	a2 = svr_lin2.coef_[0][0]
	b2 = svr_lin2.intercept_[0]
	return a2*x + b2

# 定义了找到两条直线的交点的 x 坐标的函数
def findIntersection(fun1,fun2,x0):
	return fsolve(lambda x : fun1(x) - fun2(x),x0)


result = findIntersection(line1,line2,0.0)
print "[x,y] = [ %d , %d ]" % (result,line1(result))

# x = [0,10,20, ..., 300]
x = np.linspace(0,300,31)
plt.plot(x,line1(x),x,line2(x),result,line1(result),'ro')

# axis 函数规定了 x 轴和 y 轴的取值范围
plt.axis((0,400,15,25))
plt.plot(dist,temp_min,'bo')
'''