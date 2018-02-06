# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
import scrapy.exceptions
import random
from urllib.request import urlretrieve


# class Mmjpg1Pipeline(ImagesPipeline):
#
#
#     def get_media_requests(self, item, info):
#         for image_url in item['mmjpg_url']:
#             yield scrapy.Request(image_url)
#
#     def item_completed(self, results, item, info):
#         image_path = [x['path'] for ok,x in results if ok]
#         print(image_path)
#         if not image_path:
#             raise scrapy.exceptions.DropItem('该链接不包含图片')
#         item['mmjpg_path'] = [image_path]

class Mmjpg1Pipeline(object):
    def process_item(self, item, spider):
        return item
