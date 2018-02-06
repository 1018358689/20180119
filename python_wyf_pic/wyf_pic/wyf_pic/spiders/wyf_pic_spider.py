#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import scrapy.spider
from wyf_pic.items import WyfPicItem

class WyfPicSpider(scrapy.spider.CrawlSpider):
    name = 'wyf_pic'


    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }

    def start_requests(self):
        start_url = 'https://movie.douban.com/celebrity/1337000/photos/?type=C&start=0&sortby=like&size=a&subtype=a'
        yield scrapy.Request(url=start_url, headers=self.headers, callback=self.parse)

    # // *[ @ id = "content"] / div / div[1] / ul / li[2] / div[1] / a / img
    def parse(self, response):
        item = WyfPicItem()
        sel = response.xpath('//ul[@class="poster-col3 clearfix"]/li')
        for i in sel:
            item['wyf_img_url'] = i.xpath('./div[@class="cover"]/a/img/@src').extract()
            yield item
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        if next_url:
            yield scrapy.Request(url=next_url, headers=self.headers, callback=self.parse)