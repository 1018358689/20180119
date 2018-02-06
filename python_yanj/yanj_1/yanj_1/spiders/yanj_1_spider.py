#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import scrapy.spider
import datetime
import random
import time
from yanj_1.items import Yanj1Item

random.seed(datetime.datetime.now())
num_info = 0
page_info = 0

class Yanj1Spider(scrapy.spider.CrawlSpider):
    name = 'yanj_1'
    hds = [
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
    ]
    def start_requests(self):
        start_url = 'http://www.yanj.cn/product_list-1-0-0-0-3-1-0-0-0-4-1.html'
        yield scrapy.Request(url=start_url, headers=random.choice(self.hds), callback=self.parse)

    def parse(self, response):
        global num_info
        global page_info

        time.sleep(random.uniform(0, 1))

        print('-------------------------开始-------------------------')
        item = Yanj1Item()
        data = response.xpath('//div[@class="onecp"]')
        if len(data.extract())>0:
            for sel in data:
                num_info += 1
                #print('-------------------------个数[%d]-------------------------' % num_info)
                item['yanj_num'] = [num_info]
                item['yanj_title'] = sel.xpath('./div[@class="cpmess"]/h3/a/text()').extract()
                item['yanj_link'] = sel.xpath('./div[@class="cpmess"]/h3/a/@href').extract()
                item['yanj_read'] = sel.xpath('./div[@class="cpmess"]/div[@class="cpinfo"]/div[@class="fr"]/span[1]/text()').extract()
                item['yanj_down'] = sel.xpath('./div[@class="cpmess"]/div[@class="cpinfo"]/div[@class="fr"]/span[2]/text()').extract()
                item['yanj_author'] =sel.xpath('./div[@class="cpmess"]/div[@class="cpmessleft"]/a/text()').extract()
                item['yanj_price'] = sel.xpath('./div[@class="cpmess"]/div[@class="cpmessright"]/span/text()').extract()
                yield item
            time.sleep(random.uniform(0,1))
            page_info += 1
            print('-------------------------页码[%d]-------------------------' % page_info)
            next_page = response.xpath('//div[@class="pagination"]/ul/li[last()]/a/@href').extract()[0]
            yield scrapy.Request(url=next_page, headers=random.choice(self.hds), callback=self.parse)
