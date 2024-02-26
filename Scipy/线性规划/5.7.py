from scipy.optimize import linprog
c=[-72,-64]
A=[[3,0],[12,8]]
b=[100,480]
Aeq=[[1,1]]
beq=[50]
res=linprog(c,A,b,Aeq,beq)
for i in range(len(res.x)):
    res.x[i]=round(res.x[i],1)
print("最优解:",res.x)
print("最优值: %.4f"%-res.fun)
