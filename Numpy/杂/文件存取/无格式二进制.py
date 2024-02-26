import numpy as np
a=np.arange(6).reshape(2,3)
a.tofile('C:\\数模\\py\\NumPy\\文件存取\\exap_1.bin')
#需自己指定数据类型和数组形状
b=np.fromfile('C:\\数模\\py\\NumPy\\文件存取\\exap_1.bin',dtype=int).reshape(2,3)
print(b)
