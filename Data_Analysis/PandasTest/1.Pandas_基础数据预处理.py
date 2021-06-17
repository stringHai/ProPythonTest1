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
# 现实所有列
pd.set_option('display.max_columns',None)
# 显示所有行
pd.set_option('display.max_rows',None)
# 每个列宽是20
pd.set_option('max_colwidth',20)


data = pd.read_csv("movie_data.csv",
        usecols=['average','genre','language','release_date','country','title','votes'])

# 对获取的数据表的字段进行重新排列，而不是按数据源的字段顺序显示。
# data = data[['title','country','average','genre','language','release_date','votes']]

# print(data)
# print("===========================================================")



# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* 查重，根据title去重 *************
# print(data.duplicated('title'))
clean_data = data.drop_duplicates('title')
# print(clean_data)
# print(len(clean_data),"----",len(data))
# print("============================================================")



# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* 缺失值：NaN，评分/人数——》用平均值填充，文本数据——》NaN *************
# clean_data = pd.isna(clean_data)
# # print(na_data)
clean_data['average'] = round(clean_data['average'].fillna(value = clean_data['average'].mean()),3)
# print(clean_data['average'] )
# print(clean_data['average'].mean())




# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* 分列 *************
clean_data['release_date']= clean_data['release_date'].str.split('(',expand = True)[0]
# print(clean_data)
# print(clean_data.head(3))




# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* 每年电影产量——聚合每一年的电影名称 *************
clean_data['release_date'] = pd.to_datetime(clean_data['release_date'])
# print(clean_data['release_date'].head(5))
# clean_data = clean_data.set_index(clean_data['release_date'])
# print(clean_data.head(5))
# print("===================================================")
# print(clean_data['release_date'].resample('Y').count())
# print(clean_data.max())







# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* 电影类型聚合统计——聚合电影类型 *************
# print(clean_data['genre'])
# 删除前面和后面的[ ] 号
clean_data['genre'] = clean_data['genre'].str.strip('[')
clean_data['genre'] = clean_data['genre'].str.strip(']')

# 用字符串的空值去填充NaN的数据
clean_data['genre'] = clean_data['genre'].fillna(value='')
# print(clean_data['genre'])
# exit()
genre_list = []
for i in clean_data['genre']:
        i = i.split(', ')
        # 这里注意一下，这步操作会引发一个float的报错，
        # 原因是for循环出来的i有空值，这个空值是float类型，
        # 因此，没有办法通过处理文本的方法split来操作，
        # 所以，要在前面先把genre的值处理一下，把NaN先变成文本类型的空值‘ ’
        # 也就是这行代码：clean_data['genre'] = clean_data['genre'].fillna(value='')
        for j in i:
                # print(j)
                genre_list.append(j)
# print(genre_list)
# 然后用set方法把for循环取出来的电影标签进行去重，并且把genre_list的数据结构换成list的数据结构形式
genre_list = list(set(genre_list))
# 移除genre_list里面的空值
genre_list.remove('')
# 移除list里面的空格元素

# print(genre_list)

movie_genre_count =  pd.DataFrame(np.zeros([len(genre_list),1]),
                index=genre_list,columns=['电影标签统计值'])

# print(movie_genre_count)

for i in clean_data['genre']:
        # print(i)
        for label in genre_list:
                if str(i).__contains__(label): # 如果 i 的集合 包含了j，那么就
                        # 找到label这个标签在movie_genre_count这个表里面的行号
                        movie_genre_count.loc[label,'电影标签统计值'] += 1
# print(movie_genre_count)
# exit()






# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* 各个评分下的电影数量——聚合每个评分下的电影名称 *************
# 1、获取当前数据区间：最大值和最小值，并且对区间进行间隔分配
# 2、获取各个评分类别的数据
# 3、对每个评分区间进行统计

# 数据整体情况
# print(clean_data)
# print(clean_data['average'].describe())
clean_data['average'] = clean_data['average'].__round__(1)

x = 2.2
average_list = []
while x < 9.7:
        x += 0.1
        x = x.__round__(1)
        average_list.append(x)
# print(average_list)

movie_average_tj = pd.DataFrame(np.zeros([len(average_list),1]),
                                index=average_list, columns=['各评分段电影统计'])
# print(movie_average_tj)

for i in average_list:
        for j in clean_data['average']:
                # print("记录点1================")
                if i==j :
                        movie_average_tj.loc[j,'各评分段电影统计'] += 1
# print(movie_average_tj)








# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* 排序和筛选 *************
# print(clean_data)

# 对列标签进行排序，单列/多列，正序/逆序
# print(clean_data.sort_values('title', ascending= True))
# print(clean_data.sort_values(['average','votes'], ascending= True))

# 筛选：行（索引、值、行数）、列、行列
# 筛选行
# print(clean_data.iloc[0:100])
# 筛选列
# print(clean_data.loc[clean_data['average']== 4.0])
# 行列一起筛选
# print(clean_data['average','votes'])
# print(clean_data.loc[clean_data['average']==4.0 , ['average','votes']])









# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* 各国每年的电影产量 *************
# print(clean_data)
# 对数据的字段顺序进行重新排列

# clean_data = clean_data[['title','country','average','genre','language','release_date','votes']
# ]
# # print(clean_data)
# # 删除country字段里包含的NaN元素
# clean_data['country'] = clean_data['country'].fillna(value='')
# # 删除country每个元素中前面和后面的空格部分，不然会影响数据的唯一性
# clean_data['country'] = clean_data['country'].str.strip(' ')
# country_list = []
# for c in clean_data['country']:
#         c = c.split(' / ')
#         # 这里注意一下，如果不进行clean_data['genre'] = clean_data['genre'].fillna(value=' ')
#         # 这步操作会引发一个float的报错，因为split没办法对NaN进行操作
#         # 原因是for循环出来的i有空值，这个空值是float类型，
#         # 因此，没有办法通过处理文本的方法split来操作，
#         # 所以，要在前面先把genre的值处理一下，把NaN先变成文本类型的空值‘ ’
#         # 也就是这行代码：clean_data['genre'] = clean_data['genre'].fillna(value=' ')
#         for l in c:
#                 # print(l)
#                 country_list.append(l)
# # print(country_list)
# # 对for循环取出来的国家标签去重，使用set去重，并且把country_list数据结构 转换成list列表的形式
# country_list = list(set(country_list))
# # 删除country_list中的空值
# country_list.remove('')
# # 到这里就已经获得了国家的列表
# print(country_list)
# # 刷选之后发现有一些是有重复的，比如：“美国/澳大利亚”在统计的时候就会和“美国”“澳大利亚”重复计算，所以要删除
# country_list.remove('美国/澳大利亚')
# country_list.remove('美国/加拿大/印度尼西亚')
# country_list.remove('捷克斯洛伐克/捷克')
# country_list.remove('捷克/捷克斯洛伐克')
#
# # 这里把这几个标签删除是因为其实都是中国，所以只需要统计“中国”这个标签即可。
# country_list.remove('中国香港')
# country_list.remove('中国台湾')
# country_list.remove('中国澳门')
# country_list.remove('中国大陆')
# print(country_list)

# 筛选看看数据是否正确,因为country字段里的元素中，一个元素可能存在多个国家数据，
# 因此不能用==来筛选，只能用contains，即包含某个数据来筛选，
# 这里先试着筛选了一个国家的电影，下面通过for来筛选全部国家的电影。
# print(clean_data[clean_data['country'].str.contains('中国')])

# 这里筛选全部国家的电影，使用for
# 获取到所有国家的列表之后，就要总的数据clean_data中把包含不同的国家的电影提取出来，
# 然后再进行统计，这里用for循环+contains匹配来操作
# 因为这里有两个维度，所有第一部分可以先统计年份的聚合，然后再根据国家进行聚合

# 首先把年份变成时间格式
clean_data['release_date'] = pd.to_datetime(clean_data['release_date'])
# 然后把年份这个字段变成clean_data的索引
# clean_data = clean_data.set_index(clean_data['release_date'])

# # 然后先根据国家、时间进行电影数量聚合
# for label in country_list:
#         temp = clean_data[clean_data['country'].str.contains(label)]
#         # 这里注意一下，这个temp就是筛选的每个国家的电影列表，而这个列表的长度就是这个国家电影的数量
#         print(type(temp))
#         print("国家："+label )
#         print('[ '+label+" ]的电影频数是 : ", len(temp))
#         # 这里就是根据年份这个索引来统计电影数量
#         country_year_tj = temp['release_date'].resample('Y').count()
#         print(country_year_tj)
#         # print(temp[['country','title']])
#         print("==============================================")








# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* 电影语言的频次 *************

# print(clean_data)
# 删除language字段中的空值
clean_data['language'] = clean_data['language'].fillna(value='')
# 删除language字段中每个元素包含的空格
clean_data['language'] = clean_data['language'].str.strip(' ')
language_list = []
for l in clean_data['language']:
        l = l.split(' / ')
        print(l)
        for label in l:
                language_list.append(label)
# print(language_list)
print(len(language_list))
print("==============================================================")
language_list = list(set(language_list))
print("去重后一共有的语言数：",len(language_list))
print(language_list)


# 构建一个统计列表
movie_language_count =  pd.DataFrame(np.zeros([len(language_list),1]),
                index=language_list,columns=['电影语言统计值'])
# 有了电影语言的列表之后，就开始循环列表里的语言，
# 然后拿出来和总表 clean_data['language'] 进行模糊匹配，然后计算频次
for i in clean_data['language']:
        for label in language_list:
                if str(i).__contains__(label):
                        movie_language_count.loc[label,'电影语言统计值'] += 1
print(movie_language_count)

# 聚合







# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* 各国个评分下的电影数量 *************








# *****************************************************************
# *****************************************************************
# *****************************************************************
# ************* TOP电影排行榜 *************
























