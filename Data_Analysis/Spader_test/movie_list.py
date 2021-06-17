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
import time

url = "https://movie.douban.com/top250"
headers = {'user-agent': 'my-app/0.0.1'}

page = 0
max_page =225
movie_name = []
movie_link = []
while page < max_page:
    time.sleep(5)
    url ="https://movie.douban.com/top250?start="+ page.__str__() +"&filter="
    response = requests.get(url= url, headers = headers).text
    soup = BeautifulSoup(response, 'html.parser')
    # 逐步缩小范围的过程
    for ele in soup.find_all(class_="hd"):
        movie_name.append(ele.find(class_="title").text)
        movie_link.append(ele.find('a',href= True).attrs['href'])
        print(movie_name)
        # print(movie_link)
    exit()
    # page += 25

# for name,link in zip(movie_name,movie_link):
#     print(name+ ":" +link)


