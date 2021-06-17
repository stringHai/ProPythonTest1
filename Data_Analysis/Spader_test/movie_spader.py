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
import pandas as pd

page_url = "https://movie.douban.com/top250"
headers = {'user-agent': 'my-app/0.0.1'}
movie_name = []
movie_link = []
all_movie_info = []


# 在获取网页详细信息中使用的获取编剧和演员的方法
def get_list(soup_list):
    list = []
    for elm in soup_list:
            list.append(elm.text)
    return list




# 1、获取网页信息
def get_page(page_url):
    page = 0
    max_page = 225
    while page <= max_page:
        time.sleep(3)
        url = page_url+"?start=" + page.__str__() + "&filter="
        response = requests.get(url=url, headers=headers).text
        get_link(response)
        page += 25




# 2、获取页面链接
def get_link(response):
    soup = BeautifulSoup(response, 'html.parser')
        # 逐步缩小范围的过程
    for ele in soup.findAll(class_="hd"):
        movie_name.append(ele.find(class_="title").string)
        # print(movie_name)
        # exit()
        movie_link.append(ele.find('a', href=True).attrs['href'])



# 3、获取网页详细的电影信息
def get_info(movie_link):
    time.sleep(3)
    resbons = requests.get(url= movie_link, headers= headers).text
    soup = BeautifulSoup(resbons, 'html.parser')

    movie_info = {}
    movie_info["movie_title"] = soup.find(property="v:itemreviewed").text
    movie_info["movie_director"] = soup.find(rel="v:directedBy").text
    # 这行代码重点看，是当一个信息缺失之后的处理方案
    writer = soup.findAll(class_="attrs")
    movie_info["movie_writer"] = soup.findAll(class_="attrs")[1].text if len(writer) > 1 else ""
    movie_info["movie_actor"] = get_list(soup.findAll(rel="v:starring"))
    movie_info["movie_genre"] = get_list(soup.findAll(property="v:genre"))
    movie_info["movie_country"] = soup.find(text="制片国家/地区:").next_element
    movie_info["movie_langage"] = soup.find(text="语言:").next_element
    movie_info["movie_time"] = soup.find(property="v:initialReleaseDate").text
    movie_info["movie_runtime"] = soup.find(property="v:runtime").text
    movie_info["movie_rate_average"] = soup.find(property="v:average").text
    movie_info["movie_rate_people_num"] = soup.find(property="v:votes").text
    movie_info["movie_link"] = movie_link
    for key in movie_info:
        print(key,":",movie_info.get(key))

    all_movie_info.append(movie_info)
    # print(all_movie_info)
    # exit()


if __name__ == '__main__':
    # get_info("https://movie.douban.com/subject/26430107/")
    # exit()
    get_page(page_url)

    for name, link in zip(movie_name, movie_link):
        print(name + ":" + link)
        get_info(link)
        print("===================================================================")

    data = pd.DataFrame(all_movie_info)
    data.to_excel("豆瓣250部高分电影.xlsx")