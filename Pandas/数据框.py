import pandas as pd
import numpy as np
a=np.arange(1,7).reshape(3,2)
df1=pd.DataFrame(a)
print(df1)
print("------------------")
df2=pd.DataFrame(a,index=['a','b','c'],columns=['x1','x2'])
print(df2)
print("------------------")
df3=pd.DataFrame({'x1':a[:,0],'x2':a[:,1]})
print(df3)
print("------------------")
