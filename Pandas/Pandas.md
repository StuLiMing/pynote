# Pandas

[TOC]



## 概述

+ 大多数方法都不改变原始的输入数据，而是复制数据，生成新的对象
+ 某种意义上，他的行为像是“字典”

### 处理数据的一般步骤

1. 数据整理与清洗
2. 数据分析与建模
3. 数据可视化与制表

### 数据结构

| 维数 | 名称                | 描述                               |
| ---- | ------------------- | ---------------------------------- |
| 1    | Series（序列）      | 带标签的一维同构数组               |
| 2    | DataFrame（数据框） | 带标签的，大小可变的，二维异构表格 |

## 创建

### 创建一个Series

```python
s=pd.Series([1,3,np.nan,44],index=['a','b','c','d'])
```

```python
out:
    a     1.0
    b     3.0
    c     NaN
    d    44.0
    dtype: float64
```



### 创建一个DataFrame

1.指定元素（可以用numpy的ndarray)、行名字，列名字,index指行，columns指列

  ```python
  df=pd.DataFrame(np.random.randn(6,4),index=['a','b','c','d','e','f'],columns=['A','B','C','D'])
  ```

```python
out:
          A         B         C         D
    a  0.655586  0.646335  0.822507  0.323696
    b -0.151768  0.575952 -0.343239 -0.055880
    c -1.206932 -0.557051 -0.216566 -0.184250
    d -1.264155 -0.233418  0.364680 -0.672801
    e -1.010761 -0.457117 -0.454199  0.927331
    f  0.747188 -0.058683 -1.314254  0.107907
```



2.用一个字典创建，字典的键就是每一列的名字（有自动补全机制）

```python
df2 = pd.DataFrame({'A': 1.,
                       'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                       'D': np.array([3] * 4, dtype='int32'),
                       'E': pd.Categorical(["test", "train", "test", "train"]),
                       'F': 'foo'})
```

```python
out:
         A          B    C  D      E    F
    0  1.0 2013-01-02  1.0  3   test  foo
    1  1.0 2013-01-02  1.0  3  train  foo
    2  1.0 2013-01-02  1.0  3   test  foo
    3  1.0 2013-01-02  1.0  3  train  foo
```

## 属性

+ 行名

  ```python
  index=df.index
  ```

+ 列名

  ```python
  colums=df.colums
  ```

+ 数据内容

  ```python
  values=df.values
  ```

+ 每一列数据类型

  ```python
  dtypes=df.dtypes
  ```

+ 形状（行列数）

  ```python
  df.shape
  ```

==注：以上几个都是属性，不要()==

+ 查看统计信息

  ```python
  df.describe()
  ```

## 操作

### 取转置

```python
new_df=df.T
```

### 排序

1. 按照行或列的名字排序

   ```python
   df2.sort_index(axis=1,asceding=False)  #列排序，降序
   df2.sort_index(axis=0,asceding=False)  #行排序，降序
   
   out:
            F      E  D    C          B    A
       0  foo   test  3  1.0 2013-01-02  1.0
       1  foo  train  3  1.0 2013-01-02  1.0
       2  foo   test  3  1.0 2013-01-02  1.0
       3  foo  train  3  1.0 2013-01-02  1.0
       
            A          B    C  D      E    F
       3  1.0 2013-01-02  1.0  3  train  foo
       2  1.0 2013-01-02  1.0  3   test  foo
       1  1.0 2013-01-02  1.0  3  train  foo
       0  1.0 2013-01-02  1.0  3   test  foo
   ```

2. 按照值排序

   ```python
   df2.sort_values(axis=0,by='E')   #行排序，按照每一行的"E"
   
   out:
            A          B    C  D      E    F
       0  1.0 2013-01-02  1.0  3   test  foo
       2  1.0 2013-01-02  1.0  3   test  foo
       1  1.0 2013-01-02  1.0  3  train  foo
       3  1.0 2013-01-02  1.0  3  train  foo
   ```

3. 多列联合排序

   ```python
   df2.sorted(axis=0,by=['A','E'],ascending=[True,False],inplace=True)
   //先按照A排（升序），相同的A再按照E排（降序）。inplace=True指直接改变原df不返回新df。
   ```

   

## 索引

像numpy一样，修改索引到的元素就是修改原Dataframe或Series的元素

```python
dates=pd.date_range('20220523',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)
```

```python
out:
                 A   B   C   D
    2022-05-23   0   1   2   3
    2022-05-24   4   5   6   7
    2022-05-25   8   9  10  11
    2022-05-26  12  13  14  15
    2022-05-27  16  17  18  19
    2022-05-28  20  21  22  23
```

1. 用中括号，这可以直接索引到某一列作为Series输出，但是对行只能切片得到一个子的DataFrame

```python
print(df['A'])
```

```python
out:
    2022-05-23     0
    2022-05-24     4
    2022-05-25     8
    2022-05-26    12
    2022-05-27    16
    2022-05-28    20
    Freq: D, Name: A, dtype: int32
```

```python
print(df['2022-05-24':"2022-05-24"])
```

```python
out:
                A  B  C  D
    2022-05-24  4  5  6  7
```

2. loc方法是按名字切片，切两维得到子DataFrame,切一维得到Series（只能是索引到某一行）

```python
print(df.loc[["2022-05-24","2022-05-27"],['D','A']])
```

```python
out:
                 D   A
    2022-05-24   7   4
    2022-05-27  19  16
```


3. iloc方法是按索引切片

```python
print(df.iloc[:,[1,3]])
```

```python
out:
                 B   D
    2022-05-23   1   3
    2022-05-24   5   7
    2022-05-25   9  11
    2022-05-26  13  15
    2022-05-27  17  19
    2022-05-28  21  23
```

```python
print(df.iloc[1])
```

```python
out:
    A    4
    B    5
    C    6
    D    7
```

4. 按布尔值切片

```python
print(df[df['A']>8])
```

```python
out:
                 A   B   C   D
    2022-05-26  12  13  14  15
    2022-05-27  16  17  18  19
    2022-05-28  20  21  22  23
```

## 增

如果是索引到不存在的行或列，则可以添加这一行或者这一列

  ```python
dates=pd.date_range('20220523',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)
  ```

```python
out:
                 A   B   C   D
    2022-05-23   0   1   2   3
    2022-05-24   4   5   6   7
    2022-05-25   8   9  10  11
    2022-05-26  12  13  14  15
    2022-05-27  16  17  18  19
    2022-05-28  20  21  22  23
```

```python
df.loc["add"]=np.nan
df['E']=np.nan
```

```python
out:
                            A     B     C     D   E
    2022-05-23 00:00:00   0.0   1.0   2.0   3.0 NaN
    2022-05-24 00:00:00   4.0   5.0   6.0   7.0 NaN
    2022-05-25 00:00:00   8.0   9.0  10.0  11.0 NaN
    2022-05-26 00:00:00  12.0  13.0  14.0  15.0 NaN
    2022-05-27 00:00:00  16.0  17.0  18.0  19.0 NaN
    2022-05-28 00:00:00  20.0  21.0  22.0  23.0 NaN
    add                   NaN   NaN   NaN   NaN NaN
```

插入一列

```python
import pandas as pd
 
#create DataFrame
df = pd.DataFrame({'points': [25, 12, 15, 14, 19],
                   'assists': [5, 7, 7, 9, 12],
                   'rebounds': [11, 8, 10, 6, 6]})
 
#view DataFrame
df
        points	assists	rebounds
0	25	5	11
1	12	7	8
2	15	7	10
3	14	9	6
4	19	12	6
 
#insert new column 'player' as first column
player_vals = ['A', 'B', 'C', 'D', 'E']
df.insert(loc=0, column='player', value=player_vals)
df
 
        player	points	assists	rebounds
0	A	25	5	11
1	B	12	7	8
2	C	15	7	10
3	D	14	9	6
4	E	19	12	6
```



## 其他

+ 缺失值处理

  ```python
  data.fillna(0) 					#用0填上缺失值NAN             
  ```

  





