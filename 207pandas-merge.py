# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-7-pd-merge/
# https://github.com/MorvanZhou/tutorials/blob/master/numpy%26pandas/17_merge.py
import pandas as pd

# merging two df by key/keys. (may be used in database)
# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                                   'A': ['A0', 'A1', 'A2', 'A3'],
#                                   'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                                     'C': ['C0', 'C1', 'C2', 'C3'],
#                                     'D': ['D0', 'D1', 'D2', 'D3']})
# print(left)
# print(right)
# res = pd.merge(left, right, on='key')
# print(res)

# consider two keys
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                              'key2': ['K0', 'K1', 'K0', 'K1'],
#                              'A': ['A0', 'A1', 'A2', 'A3'],
#                              'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                               'key2': ['K0', 'K0', 'K0', 'K0'],
#                               'C': ['C0', 'C1', 'C2', 'C3'],
#                               'D': ['D0', 'D1', 'D2', 'D3']})
# print(left)
# print(right)
# ## how = ['left', 'right', 'outer', 'inner']
# # res = pd.merge(left, right, on=['key1', 'key2'], how='inner')  # default for how='inner'
# # res = pd.merge(left, right, on=['key1', 'key2'], how='outer') # default for how='outer'
# # res = pd.merge(left, right, on=['key1', 'key2'], how='left') # default for how='left'
# res = pd.merge(left, right, on=['key1', 'key2'], how='right') # default for how='right'
# print(res)

# indicator
# df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
# df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
# print(df1)
# print(df2)
# # res = pd.merge(df1, df2, on='col1', how='outer', indicator=True) # indicator顯示merge的樣子
# # give the indicator a custom name
# res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column') # indicator顯示merge的樣子, 這個範例是改顯示名稱indicator_column
# print(res)

# merged by index
# left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
#                                   'B': ['B0', 'B1', 'B2']},
#                                   index=['K0', 'K1', 'K2'])
# right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
#                                      'D': ['D0', 'D2', 'D3']},
#                                       index=['K0', 'K2', 'K3'])
# print(left)
# print(right)
# # left_index and right_index
# # res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
# res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
# print(res)

# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
# res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner') # suffixes, 變數後加別名
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='outer') # suffixes, 變數後加別名
print(res)

# join function in pandas is similar with merge. If know merge, you will understand join