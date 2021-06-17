# ！
# encoding: utf-8
'''
@author: String
@softwore: pycharm
@file: 清理数据：重复值、缺失值、分列
@desc:
'''
import pandas as pd
import numpy as np

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',30)


# 读取数据
data = pd.read_csv("movie_data.csv",
                   usecols=['average','genre','language','release_date','title','votes'])
# print(data)

# 查重、去重、按title来评判
dup = data.duplicated('title')
print(len(dup))
# print(dup)

data_dd= data.drop_duplicates('title')
print(len(dup),":", len(data_dd))


# 缺失值：
# 如果是数值型数据，用平均值去填充NaN，这样可以把缺失值对统计结果的影响降到比较小的范围。
# 如果是文本数据，则不用处理
# data_dd['average'] = round(data_dd['average'].fillna(value= data_dd['average'].mean()),3)
data_dd['average'] = round(data_dd['average'].fillna(value= 7.186),2)
# 【这里出现一个问题】：就是fillna的取小数位数的2时，打印结果只有1位小数，而调整到3时，又显示了3位小数？？？？？？
print(data_dd['average'])
print(round(1.22334,2))

#
# # 分列
# print(data_dd['release_date'])
# # data_dd['release_date'] = data_dd['release_date'].str.split('(',expand=False)
# data_dd['release_date'] = data_dd['release_date'].str.split('(',expand=True)
# print(data_dd['release_date'])
# print(data_dd)
