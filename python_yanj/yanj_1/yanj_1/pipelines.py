# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import codecs


class Yanj1Pipeline(object):

    def __init__(self):
        self.file = codecs.open('item2.csv', 'wb', encoding='utf_8_sig')

    def process_item(self, item, spider):
        csv_file = csv.writer(self.file)
        y_num = str(item['yanj_num'][0])
        y_title = str(item['yanj_title'][0]).strip()
        y_author = str(item['yanj_author'][0]).strip()
        y_price = str(item['yanj_price'][0])
        y_read = str(item['yanj_read'][0]).strip(' 浏览')
        y_down = str(item['yanj_down'][0]).strip(' 下载')
        csv_file.writerow([y_num, y_title, y_author, y_price, y_read, y_down])
