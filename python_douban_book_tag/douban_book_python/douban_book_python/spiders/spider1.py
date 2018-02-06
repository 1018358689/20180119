#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import scrapy.spider
import random
import time
import datetime
from urllib.request import urlretrieve
from douban_book_python.items import DoubanBookPythonItem

random.seed(datetime.datetime.now())

l = 0

class DoubanBookPythonSpider(scrapy.spider.CrawlSpider):
    name = 'douban_book_python'

    hds = [
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
    ]

    def start_requests(self):
        #start_url = 'https://book.douban.com/tag/python'
        start_url = 'https://accounts.douban.com/login'
        yield scrapy.Request(url=start_url, meta={'cookiejar':1} ,headers=random.choice(self.hds), callback=self.log_in)

    def log_in(self, response):
        captcha = response.xpath('//img[@id="captcha_image"]/@src').extract()
        print(captcha)
        if len(captcha)>0:
            print('有验证码')
            urlretrieve(captcha[0], 'captcha.jpg')
            captcha_value = input('查看验证码图片并输入：')
            formdata = {
                'source': 'None',
                'redir': 'https://book.douban.com/tag/python',
                'form_email': '##@qq.com',
                'form_password': '##',
                'captcha-solution': captcha_value,
                'remember': 'on'
            }
        else:
            print('无验证码')
            formdata ={
                'source': 'None',
                'redir': 'https://book.douban.com/tag/python',
                'form_email': '##@qq.com',
                'form_password': '##',
                'remember': 'on'
            }
        time.sleep(random.uniform(0, 2))
        print('----正在登录----')
        yield scrapy.FormRequest.from_response(response, meta={'cookiejar':response.meta['cookiejar']}, headers=random.choice(self.hds), formdata=formdata, callback=self.parse_url)


    def parse_url(self, response):
        # item = DoubanBookPythonItem()
        global l
        sel = response.xpath('//div[@class="info"]')
        for i in sel:
            l += 1
            # //*[@id="subject_list"]/ul/li[1]/div[2]/h2/a
            book_url = i.xpath('./h2/a/@href').extract()[0]
            yield scrapy.Request(url=book_url, meta={'item_book_num': l}, headers=random.choice(self.hds),
                                 callback=self.parse)
        next_url_form = response.xpath('//*[@id="subject_list"]/div[2]/span[4]/a/@href').extract()
        if next_url_form:
            next_url = 'https://book.douban.com' + next_url_form[0]
            time.sleep(random.uniform(0, 2))
            yield scrapy.Request(url=next_url, headers=random.choice(self.hds), callback=self.parse_url)

    def parse(self, response):
        item = DoubanBookPythonItem()
        item['book_num'] = [response.meta['item_book_num']]

        item['book_title'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()
        item['book_author'] = response.xpath('//*[@id="info"]/a[1]/text()').extract()
        try:
            str(item['book_author'][0])
            # //*[@id="info"]/span[1]/a
        except:
            item['book_author'] = response.xpath('//*[@id="info"]/span[1]/a/text()').extract()

        item['book_rating_peo'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a[@class="rating_people"]/span/text()').extract()
        item['book_rating_num'] = response.xpath('//*[@id="interest_sectl"]/div/div[@class="rating_self clearfix"]/strong/text()').extract()

        time.sleep(random.uniform(0, 2))
        # item['book_from'] = response.xpath('//div[@id="info"]').re(r'(?<=出版社:</span>).*?(?=<br/>)')
        # item['book_time'] = response.xpath('//div[@id="info"]').re(r'(?<=出版年:</span>").*?(?=")')
        # item['book_much'] = response.xpath('//div[@id="info"]').re('(?<=定价:</span>\").*?(?=\")')
        yield item
