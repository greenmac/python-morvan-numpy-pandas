# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-8-pd-plot/
# https://github.com/MorvanZhou/tutorials/blob/master/numpy%26pandas/18_plot.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot data

# Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum() # cumsum() 累加函数

# DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list('ABCD'))
data = data.cumsum() # cumsum() 累加函数
# print(data.head()) # 默認顯示前五個的數據

## plot methods:
## 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'
# data.plot()
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1') # scatter分散數據點的圖
data.plot.scatter(x='A', y='C', color='LightGreen', label='Class 2', ax=ax) # scatter分散數據點的圖
plt.show()