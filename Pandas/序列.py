import pandas as pd
import numpy as np
s1=pd.Series(np.array([10.5,20.5,30.5]))
s2=pd.Series({"北京":10.5,"上海":20.5,"广东":30.5})
s3=pd.Series([10.5,20.5,30.5],index=['b','c','d'])
print(s1)
print("----------------")
print(s2)
print("----------------")
print(s3)
print("----------------")
print(s2["北京"])

#平均数
print(s2.mean()) 
#std标准差，cov协方差矩阵，var方差，describe一堆基本情况
