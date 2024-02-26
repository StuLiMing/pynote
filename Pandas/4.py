from http.client import ImproperConnectionState
import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(24).reshape(6,4))
df.iloc[0,0]=np.nan
#axis=0，按行，axis=1,按列
#how={"any","all"}
#any:有就丢（默认）；all：全是才丢
#这里不改变原DataFrame
print(df.dropna(axis=0,how="any"))
print(df)

#fillna()填值
print(df.fillna(value=114514))

#检查是否缺失数据
print(df.isna())
print(df.isnull())

#检查是否至少缺失了一个数据
# np.any是对df.isnull()输出的整个表格作或运算
print(np.any(df.isnull()))
