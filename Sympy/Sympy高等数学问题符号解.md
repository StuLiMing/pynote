# Sympy高等数学问题符号解

[TOC]

## 极限

```python
from sympy import *
x=symbols('x')
print(limit(sin(x)/x,x,0))
print(limit(pow(1+1/x,x),x,oo))
```

```python
out:
    1
	E
```



## 求导

```python
from sympy import *
x,y=symbols('x y')
z=sin(x)+x**2*exp(y)
print("关于x的二阶导数为: ",diff(z,x,2))
print("关于y的一阶导数为: ",diff(z,y))
```

```python
out:
    关于x的二阶导数为:  2*exp(y) - sin(x)
	关于y的一阶导数为:  x**2*exp(y)
```



## 级数求和

```python
from sympy import *
k,n=symbols('k n')
print(factor(summation(k**2,(k,1,n))))
print(summation(1/k**2,(k,1,oo)))
```

```python
out:
    n*(n + 1)*(2*n + 1)/6
    pi**2/6
```



## 泰勒展开

```python
from sympy import *
x,y=symbols('x y')
y=sin(x)
z=series(y,x,0,7)
print(z)
z=z.removeO()
print(z)
```

```python
out:
    x - x**3/6 + x**5/120 + O(x**7)
	x**5/120 - x**3/6 + x
```



## 定积分与不定积分

```python
from sympy import *
x=symbols('x ')
print(integrate(sin(2*x)))
print(integrate(sin(x)/x,(x,0,oo)))
```

```python
out:
    -cos(2*x)/2
	pi/2
```



## 代数方程（组）

```python
from sympy import *
x=symbols('x ')
print(solve(x**3-1,x))
print(solve((x-2)**2*(x-1)**3,x))
print(roots((x-2)**2*(x-1)**3,x))   #roots可以得到根的重数信息
```

```python
out:
    [1, -1/2 - sqrt(3)*I/2, -1/2 + sqrt(3)*I/2]
    [1, 2]
    {2: 2, 1: 3}
```

```python
from sympy import *
x,y=symbols('x y')
s=solve([x**2+y**2-1,x-y],[x,y])
print(s)
```


```python
out:
    [(-sqrt(2)/2, -sqrt(2)/2), (sqrt(2)/2, sqrt(2)/2)]
```



## 微分方程

```python
from sympy import *
x=symbols('x ')
y=symbols('y',cls=Function)   #声明y为函数类型
eq1=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)
eq2=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)-x*exp(2*x)
print(dsolve(eq1,y(x)))
print(dsolve(eq2,y(x)))
print(dsolve(eq1,y(x),ics={y(0):1,diff(y(x),x).subs(x,0):0}))      #给出定解条件
```

y=symbols('y',cls=Function)  也可以写成 y=Function('y')

```python
out:
    Eq(y(x), (C1 + C2*exp(x))*exp(2*x))
	Eq(y(x), (C1 + C2*exp(x) - x**2/2 - x)*exp(2*x))
    Eq(y(x), (3 - 2*exp(x))*exp(2*x))
```

注:返回的值是一个对象，可以用.rhs与.lhs分别提取表达式的坐左边和右边
