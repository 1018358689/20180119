#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import scrapy.spider
from scrapy.selector import Selector

from mmjpg_scrapy.items import MmjpgScrapyItem


class Text1Spider(scrapy.spider.Spider):
    name = 'text_1'

    def start_requests(self):
        start_url = ['http://www.mmjpg.com/mm/767',]
        for url in start_url:
            print(url)
            print('----s request----')
            yield scrapy.Request(url=url)

    def parse(self, response):
        print('----parse----')
        item = MmjpgScrapyItem()
        selector = Selector(response)
        year_num = selector.xpath('//div[@class="info"]/i[contains(text(),"发表于")]/text()')[0].re('\d{4}')
        sum_num = int(selector.xpath('//*[@id="page"]/a[last()-1]/text()')[0].extract())
        print(year_num,sum_num)
        x = ['#1','#2','#3']
        for i in range(3):
            item['img_url'] = i
            item['img_name'] = x[i]
            print('----for----')
            print(item['img_url'], item['img_name'])
            yield item
