# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-5-np-indexing/
import numpy as np

# A = np.arange(3, 15)
A = np.arange(3, 15).reshape((3, 4))

print(A)
# print(A[2])
# print(A[1][1]) # 第一行第一列
# print(A[2][1]) # 第二行第一列
# print(A[2, 1]) # 第二行第一列
# print(A[2, :]) # 第二行所有的數
# print(A[:, 1]) # 第一列所有的數
# print(A[1, 1:3]) # 第一行, 第1~第3的值

# for row in A:
#     print(row) # 疊代所有的數

# for column in A.T: # 行列互換
#     print(column) # 可以計算原本所有的列

# print(A.flatten()) # 返回所有值成一行
for item in A.flat: # 所有的值可疊代
    print(item)