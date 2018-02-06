#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import scrapy.spider
import datetime
import time
import random
import re
from mmjpg_1.items import Mmjpg1Item
import requests
random.seed(datetime.datetime.now())

class Mmjpg1Spider(scrapy.spider.Spider):
    name = 'mmjpg_1'

    hds = [
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
    ]

    # meta = {
    #     'dont_redirect': True,  # 禁止网页重定向
    #     'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    # }

    def start_requests(self):
        start_url = 'http://www.mmjpg.com/hot/'
        yield scrapy.Request(url=start_url, headers=random.choice(self.hds), callback=self.parse_url)

    def parse_url(self, response):
        all_pic = response.xpath('//div[@class="pic"]/ul')
        for part_pic in all_pic:
            pic_li = part_pic.xpath('./li')
            for pic_a in pic_li:
                pic_href = pic_a.xpath('./a/@href').extract()[0]
                yield scrapy.Request(
                    url=pic_href,
                    headers=random.choice(self.hds),
                    callback=self.parse
                )

    def parse(self, response):

        print('----------------------------------已进入图集----------------------------------')
        #time.sleep(random.uniform(1.1,2))

        pic_id = str(re.compile('\d+').findall(response.url)[0])

        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Host':'img.mmjpg.com',
            'Referer':'http://www.mmjpg.com/mm/%s' % pic_id,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }

        item = Mmjpg1Item()
        img_title = str(response.xpath('//div[@class="article"]/h2[1]/text()').extract()[0])
        img_num = int(response.xpath('//div[@class="page"]/a[last()-1]/text()').extract()[0])
        for i in range(img_num):
            item['mmjpg_title'] = ['%s-%d' % (img_title, i+1)]
            item['mmjpg_url'] = ['http://img.mmjpg.com/2017/%s/%d.jpg' % (pic_id, i+1)]

            down_url = item['mmjpg_url'][0]
            file_name = '../../PIC/1/%s.jpg' % item['mmjpg_title'][0]
            with open(file_name,'wb')as f_jpg:
                f_jpg.write(requests.get(down_url, headers=headers).content)











            #print('----------------------------------已获取图片----------------------------------')
            #time.sleep(random.uniform(1.1, 2))
            #urlretrieve(item['mmjpg_url'][0], '../../PIC/%s.jpg' % item['mmjpg_title'][0])
            yield item
