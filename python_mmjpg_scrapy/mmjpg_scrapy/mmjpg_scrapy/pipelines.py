# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import re

class Text1Pipeline(object):
    def process_item(self, item, spider):
        print('----###PIPELINES###----')
        print(item['img_url'])
        print(item['img_name'])
        #return item

class MmjpgScrapyPipeline(object):

    def process_item(self, item, spider):
        file_name = 'C:\\PIC\\{}'.format(re.findall('(?<=\/)\d+\.jpg', item['img_url'])[0])
        self.file = open(file_name, 'wb')
        request = requests.get(url=item['img_url'], headers=item['url_headers']).content
        self.file.write(request)

    def close_spider(self):
        self.file.close()