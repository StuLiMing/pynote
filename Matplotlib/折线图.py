from matplotlib.image import pil_to_array
import matplotlib.pyplot as plt
from numpy import square
squares = [1,4,9,16,25]
input_value=[1,2,3,4,5]
plt.plot(input_value,squares,linewidth=4)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()