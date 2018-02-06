#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import scrapy
from scrapy.selector import Selector

from mmjpg_scrapy.items import MmjpgScrapyItem

class MmjpgScrapySpider(scrapy.Spider):
    name = 'text_2'

    def start_requests(self):
        item = MmjpgScrapyItem()
        url = 'http://www.mmjpg.com/mm/1198'
        id_num = int(re.compile('\d+').findall(url)[0])
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'img.mmjpg.com',
            'Referer': url,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }
        item['url_headers'] = headers
        yield scrapy.Request(url=url, meta={'item':item,'id_num':id_num})

    def parse(self, response):
        item = response.meta['item']
        selector = Selector(response)
        year_num = int(selector.xpath('//div[@class="info"]/i[contains(text(),"发表于")]/text()')[0].re('\d{4}')[0])
        sum_num = int(selector.xpath('//*[@id="page"]/a[last()-1]/text()')[0].extract())
        item['img_name'] = selector.xpath('//div[@class="article"]/h2[1]/text()')[0].extract()
        for i in range(sum_num):
            # http://img.mmjpg.com/2016/767/2.jpg
            item['img_url'] = 'http://img.mmjpg.com/%d/%d/%d.jpg' % (year_num, response.meta['id_num'], i+1)
            yield item
