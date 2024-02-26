import numpy as np
from scipy.integrate import dblquad
f=lambda y,x:np.exp(-x**2/2)*np.sin(x**2+y)   #积分次序和变量次序要一致
bd=lambda x:np.sqrt(1-x**2)
print("I1=",dblquad(f,-1,1,lambda x: -bd(x),bd))

#三次积分类似