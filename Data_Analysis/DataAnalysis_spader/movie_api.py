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
url = "https://movie.douban.com/j/new_search_subjects/"
tags= "电影"
genres = "动作"
countries= "欧美"
year_range="2020,2020"
headers = {'user-agent': 'my-app/0.0.1'}


movie_links = []
movie_names = []
movie_lists = []




# 在获取每个电影信息的时候，查提取每个电影的连接的方法
def get_list(soup_list):
    list = []
    for ele in soup_list:
        list.append(ele.text)
    return list

# 根据电影【链接列表】，获取个电影的信息
def get_movieinfo(movie_link):
    time.sleep(3)
    try:
        resbons = requests.get(url=movie_link, headers=headers).text
        soup = BeautifulSoup(resbons, 'html.parser')
        movie_info = {}
        movie_info['movie_title'] = soup.find(property="v:itemreviewed").string
        movie_info['movie_director'] = soup.find(rel="v:directedBy").text
        movie_info['movie_writer'] = soup.find_all(class_="attrs")[1].text if len(soup.find_all(class_="attrs"))>1 else ""
        movie_info['movie_actor'] = get_list(soup.find_all(rel="v:starring"))
        movie_info['movie_genre'] = get_list(soup.findAll(property="v:genre"))
        movie_info['movie_country'] = soup.find(text="制片国家/地区:").next_element
        movie_info['movie_langage'] = soup.find(text="语言:").next_element
        movie_info['movie_ReleaseDate'] = soup.find(property="v:initialReleaseDate").text
        movie_info['movie_runtime'] = soup.find(property="v:runtime").text
        # https://movie.douban.com/subject/34801538/ 电影列表中runtime异常的电影
        movie_info['movie_average'] = soup.find(property="v:average").text
        movie_info['movie_RatingPeople'] = soup.find(property="v:votes").text
        movie_info['movie_linke'] = movie_link
        for key in movie_info:
            print(key, ":", movie_info.get(key))
    except AttributeError:
        print("缺失部分电影信息")
    # 把一个电影的所有信息装入一个容器里
    movie_lists.append(movie_info)

# 获取每个页面的【链接列表】
def get_page(page_url,tags,genres,countries,year_range):
    page = 0
    max_page = 100
    while page <= max_page:
        time.sleep(3)
        url = page_url+"?sort=U&range=0,10&tags="+tags+"&start="+page.__str__()+"&genres="+genres+"&countries="+countries+ "&year_range="+year_range
        response = requests.get(url=url, headers=headers).text
        # 将获取到的response转换成字典类型，不然后面用字典的get方法时会报错，因为网络传输的类型是字符串，不管是不是长的样子想字典
        response = eval(response)
        print(url)
        for m in response['data']:
            url_str = m.get('url').replace('\/','/')
            movie_links.append(url_str)
        # exit()
        page += 20


if __name__ == "__main__":
    # get_movieinfo("https://movie.douban.com/subject/34801538/")
    # exit()
    get_page(url,tags,genres,countries,year_range)
    for l in movie_links:
        print(l)
        get_movieinfo(l)

    data = pd.DataFrame(movie_lists)
    data.to_excel("2020年欧美动作电影列表.xlsx")

