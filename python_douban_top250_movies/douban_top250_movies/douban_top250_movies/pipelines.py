# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import csv
import json


class DoubanTop250MoviesPipeline(object):
    def open_spider(self, spider):
        self.file = codecs.open('douban_top250_movies.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = ''
        # item2 = {}
        # for i in range(len(item['movie_name'])):
        #     item2['movie_name'] = str(item['movie_name'][i])
        #     item2['movie_desc'] = str(item['movie_desc'][i])
        #     item2['movie_url'] = str(item['movie_url'][i])
        #     line += json.dumps(item2, ensure_ascii=False) + '\n'
        for i in range(len(item['movie_name'])):
            m_name = {'movie_name': str(item['movie_name'][i])}
            m_desc = {'movie_desc': str(item['movie_desc'][i])}
            m_url = {'movie_url': str(item['movie_url'][i])}
            line += json.dumps(m_name, ensure_ascii=False)
            line += json.dumps(m_desc, ensure_ascii=False)
            line += json.dumps(m_url, ensure_ascii=False)
            line += '\n'

        self.file.write(line)

    def close_spider(self, spider):
        self.file.close()

class DoubanTop250MoviesPipeline2(object):
    def __init__(self):
        self.file = codecs.open('items.csv', 'wb', encoding='utf_8_sig')
    def process_item(self, item, spider):
        csv_file = csv.writer(self.file)
        for i in range(len(item['movie_name'])):
            m_name = str(item['movie_name'][i])
            m_desc = str(item['movie_desc'][i])
            m_url = str(item['movie_url'][i])
            csv_file.writerow([m_name, m_desc, m_url])