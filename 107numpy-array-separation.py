# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-7-np-split/
import numpy as np

A = np.arange(12).reshape((3, 4))
print(A)
# print(np.split(A, 2, axis=1)) # 對縱向分割
# print(np.split(A, 3, axis=0)) # 對橫向分割
# print(np.array_split(A, 3, axis=1)) # 對縱向不對等分割
print(np.vsplit(A, 3)) # 橫向分割
print(np.hsplit(A, 2)) # 縱向向分割