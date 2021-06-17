# ！
# encoding: utf-8
'''
@author: String
@softwore: pycharm
@file: 
@desc:
'''

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('max_colwidth',20)

# 获取数据，这里去除了索引列,index_col=0
data = pd.read_csv('ad_performance.csv', index_col=0)
print(data.head(10))
# 这里的describe是打印整体基本数据情况， T 方法是行列转置
print(data.describe().round(2).T)
# 这里因为round（2），所以导致平均注册率和订单转化率很多等于零，
# 原因是转化率小，取两位小数就变成零，所有要round（4）多显示几位小数
# 注意这里打印*号的代码
print("{:*^60}".format('数据样本：统计描述'))
print(data.describe().round(4).T)


# 对数据进行审查：是否有缺失值
print("{:*^60}".format('显示：NaN值'))
print(data[data.isna().values])
# 这里使用了values==True，values是提取所有的单元格内容，
# 而values==True作用是指提取True的单元格
# print(data[data.isna().values == True])


# 对缺失值进行填充
print("{:*^60}".format('缺失值：填充'))
# print(data.fillna(data.mean))
# 注意：这里如果直接用mean的方法来填充均值，在计算相关性的时候，
# 平均停留时间在打印的不存在，所以，在此之前需要先用常数的方式把均值填充到数据表中，
# 而不是data.mean放入到 fiilna 中
# data = data.fillna(data.mean)
m = data['平均停留时间'].mean
# print(m)
# 发现平均停留时间打印出来是：419.77
data = data.fillna(419.77)



# 计算、筛选：相关性
# Kmeans聚类分析：
# 使用Kmeans聚类分析的注意点：在使用聚类算法的时候，需要用相关性分析分析一下，
# 各个聚类因子的相关性是否高，如果相关性高，需要对高相关的因子进行合并，
# 这样才不会造成聚类的时候重复计算高相关的因子，从而夸大某些特征
# 为什么使用计算相关性：因为当相关性高的变量存在的情况下，
# 聚合算法Kmeans就会重复计算这些相关性高的变量特征，从而夸大这些变量的特征影响
# 这个时候就需要合并相关性高的变量，保留一个变量即可
# print("{:*^60}".format('相关性'))
# print(data.corr().round(4))
# pd.DataFrame(data.corr().round(4)).to_excel('各因素相关性corr.xlsx')
# 这里要把高相关性的两个因素进行合并，合并的方式就是删除一个因素
# 这里的axis是控制drop的是行数据还是列数据，如果是axis=0那么，drop的是字段下面的行数据
# 但是如果是axis=1，删除的就是这个字段的所有数据
data = data.drop(['平均停留时间'], axis=1)
print(data.columns)



# 对数据标准化：标准化是常用的数据预处理操作，处理不同规模和量纲的数据，缩放到相同的数据范围
# 以此减少规模、特征。分布差异，方便比较
# 标准化方法有两种【主流】的方法：zscore_scaler、minmax_scaler
# zscore_scaler：x’=(x-mean)/std，是一种实现中心化、正态分布的标准化模型，标准化之后是以0为均值，方差为1的正态分布，会一定程度的改变数据形态。
# minmax_scaler：x'=(x-min)/(max-min)，是一种线性变换，能比较好的保持原有结构，并且能使数据完全落入0~1的区间内。
# 其他标准化方法：min-max标准化（也叫离差标准化）、z-score法（零-均值规范化）、log函数转换、atan函数转换
# 这里我们使用归一化min-max，0-1区间的minmax_scaler标准化模型
print("{:*^60}".format('对数据进行标准化'))
# print(data)

# 截取需要进行归一化的字段和对应的数据
print(data.iloc[:,0:7])
# 这个代码的意思是指，从第 1 行到最后一行，从第 1 列到第 7 列的数据，其中一个是渠道标识
# matrix = data.iloc[:,0:7] 如果使用0:7相当于取值了渠道序号，后面进行标准化的时候会报错
# 这里应该把渠道号去除，也就是1:7
matrix = data.iloc[:,1:7]
min_max_model = MinMaxScaler()
data_rescaled = min_max_model.fit_transform(matrix)
print("{:*^60}".format('使用MinMax标准化模型'))
print(data_rescaled.round(3))



# 字符串分类
# 特征数字化，把字符串的定类数据进行特征数字化，让不可以计算的字段也变成用数值进行处理
print("{:*^60}".format('特征数字化'))

