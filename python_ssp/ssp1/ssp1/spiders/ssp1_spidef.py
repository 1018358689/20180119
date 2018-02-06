#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
from ssp1.items import Ssp1Item
import scrapy.spider
import json


class Ssp1Spider(scrapy.spider.CrawlSpider):
    name = 'ssp1'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }

    def start_requests(self):
        start_url = 'https://sspai.com/api/v1/articles?offset=0&limit=10&type=recommend_to_home&sort=recommend_to_home_at&include_total=false'
        yield scrapy.Request(url=start_url, headers=self.headers, callback=self.parse_start_url)

    def parse_start_url(self, response):
        #item = Ssp1Item()
        json_dates = json.loads(response.body, encoding='utf-8')['list']
        for date in json_dates:
            # item['ssp_title'] = date['title']
            # item['ssp_author'] = date['author']['nickname']
            # item['ssp_summary'] = date['summary']
            id = date['id']
            next_url = 'https://sspai.com/post/%d' % id
            request = scrapy.Request(url=next_url, headers=self.headers, callback=self.parse)
            # request.meta['item'] = item
            yield request

    def parse(self, response):
        # item = response.meta['item']
        item =Ssp1Item()
        sel = response.xpath('//article')
        item['ssp_title'] = sel.xpath('./h1/text()').extract()
        # // *[ @ id = "app"] / div / div[1] / div / div[2] / div / article / div[1] / div[1] / h4
        item['ssp_author'] = sel.xpath('./div[1]/div[1]/h4/a/text()').extract()
        #//*[@id="app"]/div/div[1]/div/div[2]/div/article/div[1]/div[2]/span/sup
        item['ssp_like'] = sel.xpath('./div[1]/div[2]/span/sup/text()').extract()

        yield item
