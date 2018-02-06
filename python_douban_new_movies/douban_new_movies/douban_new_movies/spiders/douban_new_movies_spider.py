#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
from douban_new_movies.items import DoubanNewMoviesItem


class DoubanNewMoviesSpider(scrapy.Spider):
    name = 'douban_new_movies'
    headers_content = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://movie.douban.com/chart/'
        yield scrapy.Request(url=url, headers=self.headers_content, callback=self.parse)

    def parse(self, response):

        # response.headers = {
        #     "Accept": "*/*",
        #     "Accept-Encoding": "gzip,deflate",
        #     "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        #     "Connection": "keep-alive",
        #     "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        #     "Referer": "http://www.zhihu.com/"
        # }

        # item = DoubanNewMoviesItem()
        # // *[ @ id = "content"] / div / div[1] / div / div / table[1] / tbody / tr / td[2] / div / a
        # // *[ @ id = "content"] / div / div[1] / div / div / table[2] / tbody / tr / td[2] / div / a
        # // *[ @ id = "content"] / div / div[1] / div / div / table[3] / tbody / tr / td[2] / div / a
        # // *[ @ id = "content"] / div / div[1] / div / div / table[1] / tbody / tr / td[2] / div / div / span[2]
        # // *[ @ id = "content"] / div / div[1] / div / div / table[2] / tbody / tr / td[2] / div / div / span[2]
        # // *[ @ id = "content"] / div / div[1] / div / div / table[3] / tbody / tr / td[2] / div / div / span[2]

        # for sel in response.xpath('// *[ @ id = "content"] / div / div[1] / div / div / table'):
        #     item['movie_name'] = sel.xpath('./ tbody / tr / td[2] / div / a / text()').extract()
        #     item['movie_star'] = sel.xpath('./ tbody / tr / td[2] / div / div / span[2] / text()').extract()
        #     item['movie_url'] = sel.xpath('./ tbody / tr / td[2] / div / a / @href').extract()
        #     yield item
        item = DoubanNewMoviesItem()
        for sel in response.xpath('//div[@class="pl2"]'):
            item['movie_name'] = sel.xpath('./a/text()').extract()
            item['movie_star'] = sel.xpath('./div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()
            item['movie_url'] = sel.xpath('./a /@href').extract()
            yield item

        # item['movie_name'] = [n.encode('utf-8') for n in m_name]
        # item['movie_star'] = [n for n in m_star]
        # item['movie_url'] = [n for n in m_url]
        # yield item