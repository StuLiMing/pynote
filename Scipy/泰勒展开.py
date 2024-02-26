import numpy as np
import matplotlib.pyplot as plt

#阶乘函数
def fac(n):
    return (1 if n<1 else n*fac(n-1))   

#展开后的项
def item(n,x):
    return (-1)**n*x**(2*n+1)/fac(2*n+1)

#展开式
def mysin(n,x):
    return (0 if n<0 else mysin(n-1,x)+item(n,x))

#把[-2pi,2pi]分成100份
x=np.linspace(-2*np.pi,2*np.pi,101)
#画sin(x)
plt.plot(x,np.sin(x),'*-')
#画泰勒展开
str=['v-','H-','-.']
for n in [1,2,3]:
    plt.plot(x,mysin(2*n-1,x),str[n-1])
plt.legend(['sin','n=1','n=3','n=5'])
plt.savefig('figure3_16.png',dpi=500)
plt.show()