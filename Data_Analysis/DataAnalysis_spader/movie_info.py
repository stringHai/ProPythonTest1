# ！
# encoding: utf-8
'''
@author: String
@softwore: pycharm
@file: 
@desc:
'''

import requests
from bs4 import BeautifulSoup


'''获取网页信息并且存入到一个BeautifulSoup对象中'''
movie_url = "https://movie.douban.com/subject/1292064/"
headers = {'user-agent': 'my-app/0.0.1'}
'''获取网页信息并解析'''
resbons = requests.get(url = movie_url, headers = headers).text
# print(resbons)
'''得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出，其中'html.parser'代表HTML文件的解析器除了html的解析器还有其他的解析器'''
soup = BeautifulSoup(resbons,'html.parser')
# print(soup)
 


'''定义一个for循环的方法，因为要经常调研for循环，所以直接写一个方法来调用就行了'''
def get_list(soup_list):
    list = []
    for ele in soup_list:
        list.append(ele.text)
    return list



'''定义一个字典存放一个电影的所有信息'''
movie_info = { }

'''获取电影名称,并存入movie_info字典'''
movie_info['movie_title'] = soup.find(property="v:itemreviewed").text
# print(movie_title)
'''获取导演'''
movie_info['movie_director'] = soup.find(rel="v:directedBy").text
# print(movie_director)
'''获取编剧'''
# 注意这里因为网页信息中的id标签class 和Python的关键词类标签class冲突了，所以在class后面加一个“_”来告诉程序这个是电影信息里的id标签
movie_info['movie_writer'] = soup.findAll(class_ ="attrs")[1].string
# print(movie_writer)
'''获取主演'''
# 这里把for循环的事情定义了一个方法get_list，然后直接调用方法，把参数传进去就可以实现for循环的功能
movie_info['movie_actor'] = get_list(soup.find_all(rel="v:starring"))
# print(movie_actor)
'''获取类型'''
movie_info['movie_genre'] = get_list(soup.findAll(property="v:genre"))
# print(movie_genre)
'''获取国家'''
movie_info['movie_country'] = soup.find(text="制片国家/地区:").next_element
# print(soup.find(text="制片国家/地区:").next_element)
'''获取语言'''
movie_info['movie_langage'] = soup.find(text="语言:").next_element
# print(movie_langage)
'''获取上映日期'''
movie_info['movie_ReleaseDate'] = soup.find(property="v:initialReleaseDate").text
# print(movie_time)
'''获取片长'''
movie_info['movie_runtime'] = soup.find(property="v:runtime").text
# print(movie_runtime)
'''获取豆瓣评分'''
movie_info['movie_average'] = soup.find(property="v:average").text
# print(movie_average)
'''获取评分人数'''
movie_info['movie_RatingPeople'] = soup.find(property="v:votes").text
# print(movie_RatingPeople)

for key in movie_info:
    print(key,":",movie_info.get(key))



