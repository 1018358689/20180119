#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml.html import etree
import random
import re
import datetime
import time
from colorama import init, Fore

random.seed(datetime.datetime.now())
init(autoreset=False)


def down_url(url):  #请求下载链接
    hds = [
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
    ]
    return requests.get(url=url, headers=random.choice(hds))


def image_title(url):  #获取图片名称
    response = down_url(url)
    dom_tree = etree.HTML(response.content) #构造dom_tree
    title = dom_tree.xpath('//div[@class="article"]/h2[1]/text()')[0] #xpath返回列表 需要交[0]
    return title


def parse_image_url(url): #获取所有图片url组成列表
    image_url_list = []
    img_id = int(re.compile('\d+').findall(url)[0])
    response = down_url(url)
    dom_tree = etree.HTML(response.content)
    info_time = dom_tree.xpath('//div[@class="info"]/i[1]/text()')[0]
    year = int(re.compile('(?<=发表于: )(\d{4})(?=年)').findall(info_time)[0])  # 发表年份 用于构架img_url
    page_num = int(dom_tree.xpath('//*[@id="page"]/a[last()-1]/text()')[0])  # 总页数
    for i in range(page_num):
        image_url = 'http://img.mmjpg.com/{}/{}/{}.jpg'.format(year, img_id, i + 1)
        image_url_list.append(image_url)
    return image_url_list


def new_headers(refer_url): #新建一个headers  仿下载图片被重定向
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'img.mmjpg.com',
        'Referer': refer_url,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
    return headers


def down_img(url_list, title, headers): #传入图片的url列表，下载所有图片
    for i in range(len(url_list)):
        file_name = '{}_{}'.format(title, i + 1) #构建图片文件名字
        with open('C:\\PIC\\{}.jpg'.format(file_name), 'wb') as fimg:
            fimg.write(requests.get(url_list[i], headers=headers).content)
            # time.sleep(random.uniform(0,2))  #启动下载间隔时间


# def change_color(a_string):
#     return(Fore.LIGHTRED_EX + a_string + Fore.RESET)

def main():
    # tip_1 = change_color('"PIC"')
    # tip_2 = change_color('（用空格隔开）')
    # some_id = input('请先在C盘新建一个{}的文件夹\n接下来再输入mmjpg的一个或多个id{}：'.format(tip_1, tip_2)).split(' ')
    some_id = input(Fore.LIGHTBLUE_EX + '请先在C盘新建一个叫"PIC"的文件夹\n接下来再输入mmjpg的一个或多个id（用空格隔开）：' + Fore.RESET).split(' ')
    # time.sleep(50)
    try:
        for input_id in some_id:
            # input_id = 1212
            mmjpg_url = 'http://www.mmjpg.com/mm/{}'.format(input_id)
            headers = new_headers(mmjpg_url)
            title = image_title(mmjpg_url)
            image_url_list = parse_image_url(mmjpg_url)
            down_img(image_url_list, title, headers)
            print('\n\n----id为"{}"下载完毕，正在下载下一套ing----\n\n'.format(input_id))
        print(Fore.RED + '----已经下载全部下载完毕----' + Fore.RESET)
    except:
        print(Fore.RED + '----1.请确定你输入多个ID是用空格隔开的---------' + Fore.RESET)
        print(Fore.LIGHTRED_EX + '----2.请确定你输入的是否为有效的mmjpg里的ID----' + Fore.RESET)


if __name__ == '__main__':
    main()
