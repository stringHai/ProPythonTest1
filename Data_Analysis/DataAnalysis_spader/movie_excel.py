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
import pandas as pd
import time

uer = []
# 定义全局变量url、headers、movie_links、movie_names = []
url = "https://movie.douban.com/top250"
headers = {'user-agent': 'my-app/0.0.1'}
movie_links = []
movie_names = []
all_movie = []



# 在获取每个电影信息的时候，查提取每个电影的连接的方法
def get_list(soup_list):
    list = []
    for ele in soup_list:
        list.append(ele.text)
    return list

# 访问主页面，并且完成页面跳转
def get_page(page_url):
    page = 0
    max_page = 225
    while page <= max_page:
        time.sleep(5)
        url = page_url+"?start="+page.__str__()+"&filter="
        response = requests.get(url=url, headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        get_link(soup)
        page += 25

# 获取每页的所有电影链接
def get_link(soup):
    for ele in soup.findAll(class_="hd"):
        movie_links.append(ele.find('a', href=True).attrs['href'])
        movie_names.append(ele.find(class_="title").text)
        print(movie_links)
        # exit()


# 根据电影链接，获取个电影的信息
def get_movieinfo(movie_link):
    time.sleep(5)
    resbons = requests.get(url=movie_link, headers=headers).text
    soup = BeautifulSoup(resbons, 'html.parser')
    movie_info = {}
    movie_info['movie_title'] = soup.find(property="v:itemreviewed").string
    movie_info['movie_director'] = soup.find(rel="v:directedBy").text
    movie_info['movie_writer'] = soup.find_all(class_="attrs")[1].text if len(soup.find_all(class_="attrs"))>1 else ""
    # print(movie_info['movie_writer'])
    # exit()
    movie_info['movie_actor'] = get_list(soup.find_all(rel="v:starring"))
    movie_info['movie_genre'] = get_list(soup.findAll(property="v:genre"))
    movie_info['movie_country'] = soup.find(text="制片国家/地区:").next_element
    movie_info['movie_langage'] = soup.find(text="语言:").next_element
    movie_info['movie_ReleaseDate'] = soup.find(property="v:initialReleaseDate").text
    movie_info['movie_runtime'] = soup.find(property="v:runtime").text
    movie_info['movie_average'] = soup.find(property="v:average").text
    movie_info['movie_RatingPeople'] = soup.find(property="v:votes").text
    movie_info['movie_linke'] = movie_link
    for key in movie_info:
        print(key, ":", movie_info.get(key))

    # 把一个电影的所有信息装入一个容器里
    all_movie.append(movie_info)


# for循环找出每一条连接，并根据连接获取每个电影的详细信息
def get_onelink(movie_links):
    for n,l in zip(movie_names,movie_links):
        print( n+"："+l )
        get_movieinfo(l)
        print("-------------------------------------------------------")


# 运行作为一个入口文件
if __name__ =='__main__':
    # 测试代码
    # get_movieinfo('https://movie.douban.com/subject/26430107/')
    # exit()

    # 调用获取页面连接方法
    get_page(url)
    # 调用获取页面信息方法
    get_onelink(movie_links)

    # 将所有电影数据存入表格中
    data = pd.DataFrame(all_movie)
    data.to_excel("Top250豆瓣高分电影.xlsx")