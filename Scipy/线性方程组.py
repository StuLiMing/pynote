import numpy as np
from scipy.linalg import solve
a=np.array([[3,1,-2],[1,-1,4],[2,0,3]])
b=np.array([5,-2,2.5])
x=solve(a,b)
print(x)