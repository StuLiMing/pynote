import numpy as np,numpy.linalg as ng
import matplotlib.pyplot as plt
N=4;v=1.0;d=200.0;time=400.0;divs=201
xy=np.array([[-d,d],[d,d],[d,-d],[-d,-d]])
print(xy)
T=np.linspace(0,time,divs)
dt=T[1]-T[0]
xyn=np.empty((4,2))
Txy=xy
for n in range(1,len(T)):
    for i in [0,1,2,3]:
        j=(i+1)%4
        dxy=xy[j]-xy[i]
        dd=dxy/ng.norm(dxy)
        xyn[i]=xy[i]+v*dt*dd
    Txy=np.c_[Txy,xyn]
    xy=xyn.copy()

print(Txy)
for i in range(N):
    plt.plot(Txy[i,::2],Txy[i,1::2])
plt.show()