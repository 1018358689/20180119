# -*- coding: utf-8 -*-
import scrapy
import re
# from mmjpg_disi.items import MmjpgDisiItem
import requests
import os

class MmjpgDisiSpiderSpider(scrapy.Spider):
    name = 'mmjpg_disi_spider'

    def start_requests(self):
        start_url = 'http://www.mmjpg.com/tag/disi'
        yield scrapy.Request(url=start_url,callback=self.parse_img_url)

    def parse_img_url(self, response):
        all_href = response.xpath('//div[@class="pic"]/ul/li/a/@href').extract()
        all_title = response.xpath('//div[@class="pic"]/ul/li/a/img/@alt').extract()
        for href, title in zip(all_href,all_title):
            print('------进入【%s】------' % title)
            yield scrapy.Request(url=href, meta={'title':title}, callback=self.parse)
        next_page = response.xpath('//div[@class="page"]/a[text()="下一页"]/@href').extract()[0]
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse_img_url)


    def parse(self, response):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'img.mmjpg.com',
            'Referer': response.url,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }
        # item = MmjpgDisiItem()
        img_id = int(re.findall('\d+', response.url)[0])
        img_num = int(response.xpath('//*[@id="page"]/a[last()-1]/text()').extract()[0])
        img_year = int(response.xpath('//div[@class="info"]/i[1]').re('\d{4}')[0])
        os.mkdir('C:\\PIC\\%s' % response.meta['title'])
        for i in range(img_num):
            # http://img.mmjpg.com/2016/540/1.jpg
            img_url = 'http://img.mmjpg.com/%d/%d/%d.jpg' % (img_year, img_id, i+1)
            # item['image_urls'] = img_url
            file_name = 'C:\\PIC\\%s\\%d.jpg' % (response.meta['title'], i+1)
            with open(file_name, 'wb') as img_file:
                img_file.write(requests.get(url=img_url, headers=headers).content)