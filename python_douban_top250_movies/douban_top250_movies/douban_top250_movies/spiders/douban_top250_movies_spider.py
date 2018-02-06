#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import scrapy.spider
from douban_top250_movies.items import DoubanTop250MoviesItem

class DoubanTop250MoviesSpider(scrapy.spider.CrawlSpider):
    name = 'douban_top250_movies'

    headers_content = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }

    def start_requests(self):
        start_url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url=start_url, callback=self.parse, headers=self.headers_content)

    def parse(self, response):
        item = DoubanTop250MoviesItem()
        info = response.xpath('//div[@class="info"]')
        for sel in info:
            item['movie_name'] = sel.xpath('./div[@class="hd"]/a/span[1]/text()').extract()
            item['movie_desc'] = sel.xpath('./div[@class="bd"]//span[@class="inq"]/text()').extract()
            item['movie_url'] = sel.xpath('./div[@class="hd"]/a/@href').extract()
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url
            yield scrapy.Request(url=next_url, callback=self.parse, headers=self.headers_content)