from doctest import Example
import pandas as pd
data=pd.read_excel("Pandas\example.xlsx",usecols=['Name','Scores'])
#会自动给每一行加个索引（从0开始）
print(data)

#保存
data.to_pickle("Pandas\Saved.pickle")