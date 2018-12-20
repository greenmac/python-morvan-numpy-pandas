# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-2-np-array/
import numpy as np

# a = np.array([[2, 23, 4], [2, 32 ,4]])
# a = np.zeros((3, 4))
# a = np.ones((3, 4), dtype=np.int16)
# a = np.empty((3, 4))
# a = np.arange(10, 20, 2)
# a = np.arange(12).reshape((3, 4))
# a = np.linspace(1, 10, 5) # 生成線段
a = np.linspace(1, 10, 6).reshape((2, 3)) # 生成線段

print (a)