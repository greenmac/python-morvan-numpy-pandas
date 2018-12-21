# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-5-pd-to/
# https://github.com/MorvanZhou/tutorials/tree/master/numpy%26pandas/15_read_to
import pandas as pd

data = pd.read_csv('student.csv')
print(data)

data.to_pickle('student.pickle') # 保存檔案, pickle是python內建的儲存格式之一, 這邊當範例用而已