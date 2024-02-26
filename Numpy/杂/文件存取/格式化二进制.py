from json import load
import numpy as np
a=np.arange(6).reshape(2,3)
np.save("C:\\数模\\py\\NumPy\\文件存取\\exap_1.npy",a)
#.npy的二进制文件为numpy专用，保留了格式
b=np.load("C:\\数模\\py\\NumPy\\文件存取\\exap_1.npy")
print(b)
c=np.arange(6,12).reshape(2,3)
d=np.sin(c)

#szvez将npy打包成npz
np.savez("C:\\数模\\py\\NumPy\\文件存取\\exap_1.npz",c,d)

e=np.load("C:\\数模\\py\\NumPy\\文件存取\\exap_1.npz")
f1=e["arr_0"]     #读取第一个数组的数据
f2=e["arr_1"]     #读取第二个数组的数据
print(f2)
