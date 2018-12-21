# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-4-pd-nan/
import pandas as pd
import numpy as np

dates = pd.date_range('20181221', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
# print(df.dropna(axis=0, how='any')) # how={'any', 'all'}, any=出現一個nan就丟掉這個行, how=出現全部nan才丟掉這個行
# print(df.dropna(axis=1, how='any')) # how={'any', 'all'}, any=出現一個nan就丟掉這個列, how=出現全部nan才丟掉這個列
# print(df.dropna(axis=0, how='all')) # how={'any', 'all'}, any=出現一個nan就丟掉這個行, how=出現全部nan才丟掉這個行
# print(df.dropna(axis=1, how='all')) # how={'any', 'all'}, any=出現一個nan就丟掉這個列, how=出現全部nan才丟掉這個列
# print(df.fillna(value=0)) # 出現nan, 就用0填充(value值定義)
# print(df.isnull()) # 判斷是否有缺失數據, True為缺失這個值
print(np.any(df.isnull()) == True) # 檢查缺失的, 至少有一個True返回True