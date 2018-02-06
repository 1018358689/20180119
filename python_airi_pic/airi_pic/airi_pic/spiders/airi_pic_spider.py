#!/usr/bin/env python
# -*- coding:utf-8 -*-

from airi_pic.items import AiriPicItem
import scrapy.spider
import scrapy

class AiriPicSpider(scrapy.spider.CrawlSpider):
    name = 'airi_pic'

    def start_requests(self):
        start_url = 'http://tieba.baidu.com/p/4023230951'
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        item = AiriPicItem()
        sel = response.xpath('//div[@id="post_content_75283192143"]/img')
        for i in sel:
            item['img_urls'] = i.xpath('./@src').extract()
            yield item