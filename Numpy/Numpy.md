# Numpy学习笔记

[TOC]

## 创建

### 用reshape()改变数组形状

注意size一定要正确

```python
range=range.reshape((3,4)) #将range改成一个3行4列的数组
```



## 变形

变形有reshape()和resize()两个方法，前者返回改变后的数组但不改变原数组，后者改变原数组无返回值。

```python
a=np.arange(4).reshape(2,2)
b=a
print(a.reshape(4,),'\n',a)
print(b.resize(4,),'\n',b)
```

```python
out:
    [0 1 2 3] 
     [[0 1]
     [2 3]]
    None
     [0 1 2 3]
```

reshape(-1)可以把数组变为一维数组，也可以用flatten()

#### 升维（添加一个新轴）

```python
a=np.arange(24).reshape(4,6)

a=a[...,np.newaxis]

print(a.shape)
```

```
out:
	(4, 6, 1)
```



## 基础运算

### 元素的运算

以下的运算全部是对数组的每个元素运算

四则运算：

```python
a1=np.array([[1,2,3],[4,5,6]])
a2=np.ones((2,3))
ans=a1+a2                          # -  *  /  相同
```

给一个数组加减一个常数就是给每个元素加减这个常数

乘方运算：

```python
ans=a1**3
```

数乘运算：

```python
ans=a1*4
```

三角函数运算或其他数学运算：

需要调用numpy中的对应函数

```python
ans=np.sin(a1)
```

取小数部分或整数部分

```python
a=np.arange(10,15)
b=np.arange(5,10)
print("a/b的整数部分是\n",np.modf(a/b)[1])
print("a/b的小数部分是\n",np.modf(a/b)[0])
```

对数组进行判断：

最后会返回一个由True和False组成的数组

```python
print(a1==1)

out:
    [[ True False False]
    [False False False]]
```


### 对整个数组运算

对数组的运算一般都有两种写法:

1. np.function(array)
2. array.function()

可以用axis=0或axis=1指定对列或行运算。不写默认对整个数组运算

常用运算如下：

| 方法   | 作用     | 方法  | 作用         |
| ------ | -------- | ----- | ------------ |
| sum    | 求和     | var   | 求方差       |
| mean   | 求平均   | diff  | 相邻数字求差 |
| max    | 最大值   | ceil  | 向上取整     |
| min    | 最小值   | floor | 向下取整     |
| cumsum | 累计求和 | rint  | 四舍五入     |



```python
array=np.array([[1,2,3],[4,5,6]])
print(array.cumsum())

out:
    [ 1  3  6 10 15 21]
```

```python
array=np.array([[1,2,3],[4,5,6]])
print(np.diff(array))

out:
    [[1 1] 
    [1 1]]
```

**注：diff只有np.diff的形式**

求非0元素索引：nonzero (行索引和列索引是两个分开的数组)

8. 排序：sort

9. 剪切：clip

np.clip(array,min,max):

array中所有小于min的数都使之等于min，所有大于max的数都使之等于max，其他不变

```python
array=np.array([[1,2,3],[4,5,6]])
print(np.clip(array,2,5))

out:
    [[2 2 3]
    [4 5 5]]
```



## 矩阵运算

### np.dot()

np.dot()有三种用法

1. 矩阵乘法

```python
a=np.array([[1,2],[3,4]])
print(np.dot(a,a.T))
```

```python
out:
    [[ 5 11] 
     [11 25]]
```

2. 向量内积

```python
print(np.dot([1,2],[3,4]))
```

```python
out:
    11
```

3. 矩阵与向量的乘法

   可以理解为X每一行看作一个向量分别与y做内积，然后输出一个行向量

```python
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y=[1,2]
print(np.dot(X, y))
```

```python
out:
	[3 5 6 8]   
```

**注：一种等价的写法是a.dot(b)**

### 矩阵求转置

使用.T可以取一个矩阵的转置

```python
a3=a2.T
```

### 矩阵的求逆

可逆矩阵求逆，用np.linalg.inv(a)

求伪逆，用np.linalg.pinv(a)


## 索引

1.直接通过二维的坐标来索引二维数组的某个元素

```python
ar=np.arange(3,15).reshape((3,4))
print(ar)
print(ar[1][3])

out:
    [[ 3  4  5  6]
    [ 7  8  9 10]
    [11 12 13 14]]
    10
```

2.可将行索引和列索引放在一个中括号

```python
print(ar[1,3])

out:
    10
```

3.只写一个索引会得到对应的一整行

```python
print(ar[1])

out:
    [ 7  8  9 10]
```

4.可以用  :  来切片

```python
print(ar[1,1:3])

out:
    [8 9]
```

```python
print(ar[:,2])

out:
	[ 5  9 13]
```

5.可以将多个索引打包到一个[]内，这样一来n维数值索引就是一个中括号内套n个中括号。

```python
print(ar[[0,1,2],[0,1,2]])

out:
    [ 3  8 13]
```

6.布尔索引

```python
print(ar[ar%2==0])
out:
    [ 4  6  8 10 12 14]
```

**注：修改索引到的元素就是修改原来的数组中的元素**



## 增删改

1.删除一行或者一列（不改变原数组，返回删除后的新数组）

```python
ar=np.arange(3,15).reshape((3,4))
print(ar)

out:
    [[ 3  4  5  6]
    [ 7  8  9 10]
    [11 12 13 14]]
```

```python
ar=np.delete(ar,2,axis=0)
print(ar)
ar=np.delete(ar,0,axis=1)
print(ar)

out:
    [[ 3  4  5  6]
	 [ 7  8  9 10]]
    
    [[ 4  5  6]
	 [ 8  9 10]]
```

2.增加行或列（不改变原数组，返回增加后的新数组）

```pyy
ar=np.append(ar,[[1,1,1],[2,3,3]],axis=0)
print(ar)
ar=np.append(ar,[[1,2],[3,4],[5,6],[7,8]],axis=1)

out:
	[[ 4  5  6]
     [ 8  9 10]
     [ 1  1  1]
     [ 2  3  3]]
     
     [[ 4  5  6  1  2]
     [ 8  9 10  3  4]
     [ 1  1  1  5  6]
     [ 2  3  3  7  8]]
```

3.用where修改元素（不改变原数组，返回修改后的新数组）

```python
ar=np.where(ar>3,0,ar)     #将ar中大于3的元素修改为0，其他元素仍然为ar
print(ar)  

out:
    [[0 0 0 1 2]
     [0 0 0 3 0]
     [1 1 1 0 0]
     [2 3 3 0 0]]
```



## 常用迭代方法

1.for循环会迭代行

```python
ar=np.arange(3,15).reshape((3,4))
for row in ar:
	print(row)
    
out:
    [3 4 5 6]
    [ 7  8  9 10]
    [11 12 13 14]
```

2.可以取转置来迭代列

```python
for column in ar.T:
    print(colum)
    
out:
    [ 3  7 11]
    [ 4  8 12]
    [ 5  9 13]
    [ 6 10 14]
```

3.迭代每一个元素,可以先将二维数组转变为一维数组

```python
for item in ar.flatten():
    print(item)
    
out:
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
```



## 数组的合并（可以用np.append()替代，没啥用）

### np.vstack()和np.hstack()

np.vstack()是垂直合并，np.hstack()是水平合并，二者可以合并多个数组,注意参数是一个元组

```python
a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.hstack((a1,a2,a2,a1)))

out:
    [1 2 3 4 5 6 4 5 6 1 2 3]
```

### np.concatenate()

np.concatenate()通过指定axis的值来确定是水平合并还是垂直合并

```python
print(np.concatenate((a1,a2),axis=0))

out:
    [1 2 3 4 5 6]
```

### np.c_()

```python
print(np.c_[np.array([1,2,3]),np.array([4,5,6])])

out:
    [[1 4]
     [2 5]
     [3 6]]
```





## 数组的分割

### np.vsplit()和np.hsplit()

这两个方法与合并的vstack和hstack类似

```python
ar=np.arange(12).reshape((3,4))
print(np.vsplit(ar,2))

out:
    [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
```

### np.split()

这个方法与合并的concatenate类似

```python
print(np.split(ar,2,axis=1))

out:
    [array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
```

### np.array_split()

split,vsplit,hsplit只能将数组分成相等大小的子数组（否则会报错），而array_split可以进行不等的分割

```python
print(np.array_split(ar,3,axis=1))

out:
    [array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2],
       [ 6],
       [10]]), array([[ 3],
       [ 7],
       [11]])]
```



## 拷贝

### 浅拷贝

数组的直接赋值时浅拷贝，拷贝的时对象的指针

```python
a=np.array([1,2,3])
b=a
c=a
d=c
```

这里的a,b,c,d指向的是同一块内存，可以理解为是同一个东西的不同名字。改变任何一个，其他的同步改变

### 深拷贝

对一个数组进行深拷贝需要用到这个数组的copy方法。

```python
e=a.copy()
e[1]=0

out:
    [1 0 3]
```

这里e和a就没有关联了，改变e不会改变a

也可以写成e=np.copy(a)

## random模块

### exponential

指数分布,参数sacle的值是1/lambda

```python
d=np.random.exponential(scale="10",size=(3,4))
```

### nomal

正态分布，参数loc是均值，参数scale是标准差

```python
d=np.random.normal(loc=10,scale=2,size=(3,4))
```

### randn

标准正态分布，具体见如下例子

```python
a=np.random.randn(2)
b=np.random.randn(2,3)
c=np.random.randn(2,3,4)
print("a:",a)
print("b:",b)
print("c:",c)
```

```python
out:
    a: [ 1.50527515 -0.60379306]
    
    b: [[-1.07720039 -1.51389476  1.02505915]
     [-0.09201379  0.41854434 -0.32141671]]
    
    c: [[[ 0.25549075  0.43310217  0.57788455 -0.31156577]
      [ 0.77659345  0.00843061  1.33288197 -0.40092301]
      [-0.2124421  -0.57728996  1.00016399 -0.61871522]]

     [[ 1.81882988 -0.31106235 -0.42865033  0.2189887 ]
      [-0.380735   -0.86369707 -1.42328479 -1.44414051]
      [-1.24517567  0.0863569   1.61479671 -1.45128044]]]
```




## 其他

### 升维

```python
a=np.array([1,2,3])
print(a)

out:
    [1 2 3]
```

```python
a=a[np.newaxis,:]      #给a增加一个行的维度
print(a)

out:
    [[1 2 3]]
```

```python
a=a[:,np.newaxis]      #给a增加一个列的维度
print(a)

out:
    [[1]
     [2]
     [3]]
```







