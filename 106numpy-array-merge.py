# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-6-np-concat/
import numpy as np

# A = np.array([1, 1, 1])[:, np.newaxis] # np.newaxis加了一個維度, 這條是列
# B = np.array([2, 2, 2])[:, np.newaxis] # np.newaxis加了一個維度, 這條是列
# # A = A[np.newaxis, :].shape # np.newaxis加了一個維度, 這條是行
# # A = A[:, np.newaxis] # np.newaxis加了一個維度, 這條是列
# C = np.vstack((A, B)) # vertical stack, 上下合併
# D = np.hstack((A, B)) # horizontal stack, 左右合併
# print(D)
# print(A.shape, D.shape)
# print(np.hstack((A, A, B))) # 三個矩陣合併

A = np.array([1, 1, 1])[:, np.newaxis] # np.newaxis加了一個維度, 這條是列
B = np.array([2, 2, 2])[:, np.newaxis] # np.newaxis加了一個維度, 這條是列
C = np.concatenate((A, B, B, A), axis=0) # concatenate可定義行或列合併, axis=0縱向合併
D = np.concatenate((A, B, B, A), axis=1) # concatenate可定義行或列合併, axis=1橫向合併
print(C)
print(D)