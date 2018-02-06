#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
from urllib.request import urlretrieve


class DoubanMnSpider(scrapy.Spider):
    name = 'douban_mn'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }

    def start_requests(self):
        start_url = 'https://accounts.douban.com/login'
        yield scrapy.Request(url=start_url, meta={'cookiejar': 1}, headers=self.headers, callback=self.parse)

    def parse(self, response):
        img_info = response.xpath('//img[@id="captcha_image"]/@src').extract()
        print(img_info)
        if len(img_info) > 0:
            urlretrieve(img_info[0], 'captcha.jpg')
            captcha_value = input('查看验证码图片并输入：')
            form_data = {
                'source': 'None',
                'redir': 'https://book.douban.com/tag/python',
                'form_email': '##@qq.com',
                'form_password': '##',
                'captcha-solution': captcha_value,
                'remember': 'on'
            }
        else:
            print('无验证码')
            form_data = {
                'source': 'None',
                'redir': 'https://book.douban.com/tag/python',
                'form_email': '##@qq.com',
                'form_password': '##',
                'remember': 'on'
            }
        print('-----------------\n正在登录\n-----------------')
        yield scrapy.FormRequest.from_response(
            response,
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.headers,
            formdata=form_data,
            callback=self.parse_connect
        )

    def parse_connect(self, response):
        title = response.xpath('//title/text()').extract()[0]
        if '登陆豆瓣' in title:
            print('登录失败')
        else:
            print('--登录成功--' + title)
