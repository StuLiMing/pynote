import numpy as np
from scipy.optimize import fsolve

#二分法
def binara_search(f,a,b,r):
    c=(a+b)/2
    while np.abs((f(c)))>r:
        if f(a)*f(c)<0:b=c
        else:a=c
        c=(a+b)/2
    return c

#牛顿法
def newton_iter(f,r,x0,dx=1e-8):
    def diff(f,dx=dx):
        return lambda x:(f(x+dx)-f(x-dx))/(2*dx)
    df=diff(f,dx)
    x1=x0-f(x0)/df(x0)
    while np.abs(x1-x0)>r:
        x0=x1
        x1=x1-f(x1)/df(x1)    
    return x1

y=lambda x:x**3+1.1*x**2+0.9*x-1.4
a=0;b=1;r=10e-6
print(binara_search(y,a,b,r))
print(newton_iter(y,r,0))
print(fsolve(y,0))
