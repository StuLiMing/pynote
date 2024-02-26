# Sympy符号函数作图

[TOC]

## 二维曲线画图

![这是一张图片](C:\Users\lm\AppData\Roaming\Typora\typora-user-images\image-20220707203517901.png)

```python
from sympy import *
x=symbols('x')
plot((2*sin(x),(x,-6,6)),(cos(x+pi/4),(x,-5,5)))
```

## 三维曲线画图

```python
from sympy import *
x,y=symbols('x y')
plotting.plot3d(sin(sqrt(x**2+y**2)),(x,-10,10),(y,-10,10))
```

## 隐函数画图

```python
from sympy import *
x,y=symbols('x y')
plot_implicit(Eq((x-1)**2+(y-2)**3,4),(x,-6,6),(y,-2,4))
```

使用匿名函数的写法（没看懂）

```python
from sympy import *
x,y=symbols('x y')
ezplot=lambda expr:plot_implicit(expr)
ezplot((x-1)**2+(y-2)**3-4)
```

