import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 定义微分方程组
def model(w, t, a, b, c,d):
    x, y = w
    dxdt = -a * x + b * x * y
    dydt = c * y - d * x * y
    return [dxdt, dydt]

# 定义参数
a = 1  
b = 1  
c = 1  
d =1 

# 定义初始条件
y0 = [1, 1]  # 初始值，x(0) = 1, y(0) = 1
t = np.linspace(0, 20, 1000)  # 时间范围，从0到10，分成1000个点

# 使用odeint函数求解微分方程组
ret = odeint(model, y0, t, args=(a, b, c,d))

# 提取解
x, y = ret[0:1799:, 0], ret[:, 1]

# 绘制结果
plt.figure(figsize=(8, 6))
plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)')
plt.xlabel('时间')
plt.ylabel('解')
plt.title('微分方程组的数值解')
plt.legend()
plt.grid(True)
plt.show()
