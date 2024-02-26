from cProfile import label
from shutil import which
import matplotlib.pyplot as plt

x=list(range(1,1001))
y=[a**2 for a in x]
plt.scatter(x,y,s=10,edgecolors='none',c=y,cmap=plt.cm.Blues)

plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which="both",labelsize=14)
plt.axis([0,1100,0,1100000])

plt.savefig('C:\\数模\\py\\Matplotlib\\fig2.png',bbox_inches='tight')
plt.show()