# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

# class WyfPicPipeline(object):
#     def process_item(self, item, spider):
#         return item

class WyfPicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['wyf_img_url']:
            yield scrapy.Request(image_url)
    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('图片未下载好 %s' % image_path)