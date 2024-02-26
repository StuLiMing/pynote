from scipy.optimize import linprog
c=[110,120,130,110,115,-150]
A=[[1,1,0,0,0,0],[0,0,1,1,1,0],[8.8,6.1,2.0,4.2,5.0,-6],[-8.8,-6.1,-2.0,-4.2,-5.0,3]]
b=[200,250,0,0]
Aeq=[[1,1,1,1,1,-1]]
beq=[0]
res=linprog(c,A,b,None,None)
for i in range(len(res.x)):
    res.x[i]=round(res.x[i],4)
print("最优值: %.4f" %-res.fun)
print("最优解: ",res.x)