# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-4-np-math2/
import numpy as np

# A = np.arange(2, 14).reshape((3, 4))
# print(A)
# print(np.argmin(A)) # 最小值索引
# print(np.argmax(A)) # 最大值索引
# print(np.mean(A)) # 平均值
# print(np.average(A)) # 平均值
# print(np.median(A)) # 中位數
# print(np.cumsum(A)) # 逐漸累加的值
# print(np.diff(A)) # 逐漸累減的值
# print(np.nonzero(A)) # 非0的數

B = np.arange(14, 2, -1).reshape((3, 4))
print(B)
# print(np.sort(B)) # 排序
# print(np.transpose(B)) # 行列互換
# print(B.T) # 行列互換
# print((B.T).dot(B)) # 矩陣乘法
# print(np.clip(B, 5, 9)) # clip, 範例=>小於5的數等於5, 大於9的數等於9
print(np.mean(B, axis=0)) # 可對於列的指定計算
print(np.mean(B, axis=1)) # 可對於行的指定計算