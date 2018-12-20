# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-3-np-math1/
import numpy as np

# a = np.array([10, 20, 30, 40, 90])
# b = np.arange(4)
# print (a, b)
# c = a*b
# c = b**2
# c = 10*np.sin(a)
# print (c)
# print (b)
# print (b < 3)
# print (b == 3)

# a = np.array([[1, 1], [0, 1]])
# b = np.arange(4).reshape((2 ,2))
# # print (a)
# # print (b)
# c = a*b
# c_dot = np.dot(a, b) # 矩陣運算
# c_dot_2 = a.dot(b)
# print (c)
# print (c_dot)
# print (c_dot_2)

a = np.random.random((2, 4))
print(a)
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.sum(a, axis=1)) # axis維度, axis=1每一行求值
print(np.min(a, axis=1)) # axis維度, axis=1每一行求值
print(np.max(a, axis=1)) # axis維度, axis=1每一行求值
print(np.sum(a, axis=0)) # axis維度, axis=0每一列求值
print(np.min(a, axis=0)) # axis維度, axis=0每一列求值
print(np.max(a, axis=0)) # axis維度, axis=0每一列求值