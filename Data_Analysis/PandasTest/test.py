# ！
# encoding: utf-8
'''
@author: String
@softwore: pycharm
@file: 
@desc:
'''

import pandas as pd
import numpy as np

# 显示格式设置：设置显示所有列
pd.set_option('display.max_columns', None)

# 显示格式设置，设置显示所有行
pd.set_option("display.max_rows", None)

# 显示格式设置，设置数据显示长度
pd.set_option('max_colwidth', 10)

data = pd.read_csv("movie_data.csv", usecols=['average','genre','language','release_date','title','votes'])

print(data)




# 查重、去重：通过title来确定
df_duplicated = data.duplicated('title')
print(df_duplicated)


# 缺失值NaN：如果是定类数据——》保留NaN，如果是数值型数据——》替换成平均值


# 分列