# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs


class Ssp1Pipeline(object):
    def open_spider(self, spider):
        self.file = codecs.open('item2.csv', 'wb', encoding='utf_8_sig')

    def process_item(self, item, spider):
        # line = ''
        csv_file = csv.writer(self.file)
        for i in range(len(item['ssp_title'])):
            s_title = str(item['ssp_title'][i])
            s_author = str(item['ssp_author'][i])
            s_like = str(item['ssp_like'][i])
            csv_file.writerow([s_title, s_author, s_like])

    def close_spider(self, spider):
        self.file.close()
