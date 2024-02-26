# Sympy基础知识

sympy库用来作符号计算

[TOC]

## 一些”常数“

E=2.71828...

pi=3.14159...

oo : 正无穷

O:无穷小量

I:虚数单位

## 定义变量

定义变量用symbols()，定义多个变量可以用空格隔开或者用形同m0:4的形式（m1,m2,m3,m4）

```python
from sympy import *
x,y,z=symbols('x y z')
m0,m1,m2,m3=symbols('m0:4')
```

## 创建符号表达式

```python
expr=y**2+sin(y)*cos(y)+sin(z)
print(expr)
```

```python
out:
    y**2 + sin(y)*cos(y) + sin(z)
```

## 带入符号变量的值

```python
print(expr.subs({y:2,z:3}))
```

```python
out:
    sin(2)*cos(2) + sin(3) + 4
```

## 以浮点数显示计算结果

显示对象的浮点数值有n()与evalf()两个方法，默认15位，可以在括号内写个参数指定小数位数

```python
print(expr2.subs({y:2,z:3}).n())
```

```python
out:
    3.76271876040590
```

```python
print("{} = {}".format(pi,pi.evalf(3)))
```

```python
out:
    pi = 3.14
```

## 式子的变形

```python
from sympy import *
x,y=symbols('x y')
expr=(x**2+x)/(2*x)
expr2=apart(expr)         #把分式拆开
expr3=together(expr2)     #通分
print(expr)
print(expr2)
print(expr3)
```

```python
out:
    (x**2 + x)/(2*x)
    x/2 + 1/2
    (x + 1)/2
```

```python
expr4=x**2+2*x+1
print(factor(expr4))     #因式分解
```

```python
out:
    (x + 1)**2
```



## 未分类

1.若y是t的一个sympy的函数式子，可以通过lambdify转化为一个python的函数

f=lambdify(t,y,'numpy')
