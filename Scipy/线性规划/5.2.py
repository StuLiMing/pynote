from scipy.optimize import linprog
c=[-1,2,3]
A=[[-2,1,1],[3,-1,-2]]
b=[9,-4]
Aeq=[[4,-2,-1]]
beq=[-6]
LB=[-10,0,None]
UB=[None]*len(c)
bounds=tuple(zip(LB,UB))
res=linprog(c,A,b,Aeq,beq,bounds)
for i in range(len(res.x)):
    res.x[i]=round(res.x[i],1)
print("最优解:",res.x)
print("最优值: %.4f"%res.fun)
