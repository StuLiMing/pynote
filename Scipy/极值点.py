from numpy import *
from scipy.optimize import fminbound,fmin,minimize

f= lambda x: exp(x)*cos(2*x)
x1=fminbound(f,0,3)   #f在[0,3]的极小值点
print("极小值点为:{},极小值为:{}".format(x1,f(x1)))

x2=fmin(f,1)          #f在1附近的极小值点
print("极小值点为:{},极小值为:{}".format(x2,f(x2)))

f=lambda x:100*(x[1]-x[0]**2)**2+(1-x[0])**2
x0=minimize(f,[2.0,2.0])   #多元函数f在[2,2]附近的极值点
print("极小值点为:{},极小值为:{}".format(x0.x,x0.fun))
