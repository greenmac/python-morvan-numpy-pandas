# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-8-np-copy/
import numpy as np

# a = np.arange(4)
# b = a
# c = a
# d = b
# a[0] = 11
# print(a)
# print(b)
# print(c)
# print(d)
# print(b is a)
# print(d is a)

# a = np.arange(4)
# b = a
# c = a
# d = b
# a[0] = 11
# d[1:3] = [22, 33]
# print(a)
# print(b)
# print(c)
# print(d)

a = np.arange(4)
b = a
c = a
d = b
a[0] = 11
d[1:3] = [22, 33]
b = a.copy() # deep copy, 深度copy, 這樣就不會被關聯
a[3] = 44
print(a)
print(b) # b因為deep copy的關係, 所以b[3]不會被改變, 這樣就不會被關聯
print(c)
print(d)