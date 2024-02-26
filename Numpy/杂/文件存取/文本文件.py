
import numpy as np
a=np.arange(0,3,0.5).reshape(2,3)

#存
np.savetxt("C:\\数模\\py\\NumPy\\文件存取\\exap_1.txt",a)
#读
b=np.loadtxt("C:\\数模\\py\\NumPy\\文件存取\\exap_1.txt")
print("b=",b)

#fmt指定格式，delimiter指定分隔符
np.savetxt("C:\\数模\\py\\NumPy\\文件存取\\exap_2.txt",a,fmt="%d",delimiter=",")
c=np.loadtxt("C:\\数模\\py\\NumPy\\文件存取\\exap_2.txt",delimiter=",")

print("c=",c)

#genfromtxt见p50