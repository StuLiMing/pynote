from scipy.optimize import linprog
c=[-1,4]
A=[[-3,1],[1,2]]
b=[6,4]
bounds=((None,None),(-3,None))
res=linprog(c,A,b,None,None,bounds)
print(res.fun)
print(res.x)
