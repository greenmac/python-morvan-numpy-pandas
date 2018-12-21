# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-3-pd-assign/
import pandas as pd
import numpy as np

dates = pd.date_range('20181221', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6 ,4)), index=dates, columns=['A', 'B', 'C', 'D']) # 未定義index會自動生成

print(df)
print('------------------------------')

df.iloc[2, 2] = 1111
df.loc['2018-12-21', 'B'] = 2222
# df[df.A > 4] = 0 # 改變A列>4裡所有的值
# df.A[df.A > 4] = 0 # 改變A列>4那列的值而已
df.B[df.A > 4] = 0 # 改變B列>4那列的值而已
df['F'] = np.nan
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20181221', periods=6))
print(df)