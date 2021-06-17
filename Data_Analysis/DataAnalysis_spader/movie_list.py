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


# 访问top250电影页面
url = "https://movie.douban.com/top250"
headers = {'user-agent': 'my-app/0.0.1'}

# 跳转页面: ?start=25&filter=
page = 0
max_page = 225
movie_link = []
movie_name = []

while page <= max_page:
    # 跳转到下一页
    # 注意：这里使用了__str__把page转换成字符串,效果和 str(page) 一样
    url = "https://movie.douban.com/top250?start="+page.__str__()+"&filter="
    response = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    for ele in soup.findAll(class_="hd"):
        # print(ele)
        movie_link.append(ele.find('a',href = True).attrs['href'])
        movie_name.append(ele.find(class_="title").text)
    # 增加page的值
    page += 25
    # 验证数据正确性
    # print(link)
    # 跳出：进入第一页之后就跳出，不然会抓取10页信息，没必要
    # exit()

# 浏览链接
for name,link in zip(movie_name,movie_link):
    print(name)
    print(link)


# 获取实现每个页面信息的抓取

