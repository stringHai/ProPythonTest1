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

movie_url = "https://movie.douban.com/subject/1292052/"
headers = {'user-agent': 'my-app/0.0.1'}

resbons = requests.get(url= movie_url, headers= headers).text
soup = BeautifulSoup(resbons, 'html.parser')

def get_list(soup_list):
    list = []
    for elm in soup_list:
        list.append(elm.text)
    return list

movie_info = {}
movie_info["movie_title"] = soup.find(property="v:itemreviewed").text
movie_info["movie_director"] = soup.find(rel="v:directedBy").text
movie_info["movie_writer"] = soup.findAll(class_="attrs")[1].text
movie_info["movie_actor"] = get_list(soup.findAll(rel="v:starring"))
movie_info["movie_genre"] = get_list(soup.findAll(property="v:genre"))
movie_info["movie_country"] = soup.find(text="制片国家/地区:").next_element
movie_info["movie_langage"] = soup.find(text="语言:").next_element
movie_info["movie_time"] = soup.find(property="v:initialReleaseDate").text
movie_info["movie_runtime"] = soup.find(property="v:runtime").text
movie_info["movie_rate_average"] = soup.find(property="v:average").text
movie_info["movie_rate_people_num"] = soup.find(property="v:votes").text

print(movie_info)
for key in movie_info:
    print(key,":",movie_info.get(key))

