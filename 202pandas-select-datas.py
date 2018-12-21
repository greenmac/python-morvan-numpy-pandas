# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-2-pd-indexing/
import pandas as pd
import numpy as np

dates = pd.date_range('20181221', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6 ,4)), index=dates, columns=['A', 'B', 'C', 'D']) # 未定義index會自動生成

print(df)
print('------------------------------')
# print(df['A'], df.A)
# print(df[0:3], df['2018-12-22':'2018-12-24'])

# select by label:loc
# print(df.loc['2018-12-22']) # 橫向標籤選擇
# print(df.loc[:, ['A', 'B']]) # 橫向全部, 縱向A B兩列
# print(df.loc['2018-12-22', ['A', 'B']]) # 橫向選擇某個, 縱向A B兩列

# select by position:iloc
# print(df.iloc[3]) # 橫向選擇第幾個
# print(df.iloc[3, 1]) # 橫向選擇第幾個第幾位
# print(df.iloc[3:5, 1:3])
# print(df.iloc[[1,3,5], 1:3]) # 不連續篩選

# mixed selection:ix
# print(df.ix[:3, ['A', 'C']]) # 選擇行列或標籤

# Boolean indexing
print(df[df.A > 8])
