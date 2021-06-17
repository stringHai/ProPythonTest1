# ！
# encoding: utf-8
'''
@author: String
@softwore: pycharm
@file: 
@desc:
'''


import numpy as np
import pandas as pd

d = {
    'one': pd.Series([1,2,3],index=['a','b','c']),
    'two': pd.Series([1,2,3,4],index=['a','b','c','d'])
}

# 构建DataFrame对象
df = pd.DataFrame(d)
print(df)
print("====================")
# 按行号查询一条数据
print(df.iloc[1])
print("====================")
# 按索引index查询一行记录
print(df.loc['c'])
print("====================")
# 查询一个字段的所有内容
print(df['two'])
print("====================")
# 查询多个字段数据
print(df[['two','one']])
print("====================")
# 查找单单元格数据
print(df['one'].loc['d'])
print("====================")
print(df[['two','one']].loc['d'])
print("====================")
# 模糊查询
print(df[df['two']>2])
# 精准查询

