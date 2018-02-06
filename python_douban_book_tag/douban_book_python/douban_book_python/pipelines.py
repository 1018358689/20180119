# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import codecs


class DoubanBookPythonPipeline(object):

    def __init__(self):
        self.file = codecs.open('items4.csv', 'wb', encoding='utf_8_sig')

    def process_item(self, item, spider):
        csv_file = csv.writer(self.file)
        # csv_file.writerow(['num','title','author','rating_num','rating_peo'])
        # for i in range(len(item['book_title'])):
        #     l_num = str(item['book_num'][i])
        #     l_title = str(item['book_title'][i]).replace(' ', '')
        #     l_author = str(item['book_author'][i]).replace(' ', '').replace('\n', '')
        #     l_rating_num = str(item['book_rating_num'][i]).replace(' ', '')
        #     l_rating_peo = str(item['book_rating_peo'][i]).replace(' ', '')
        #     csv_file.writerow([l_num, l_title, l_author, l_rating_num, l_rating_peo])
        l_num = str(item['book_num'][0])
        l_title = str(item['book_title'][0]).replace(' ', '')
        l_author = str(item['book_author'][0]).replace(' ', '').replace('\n', '')
        try:
            #l_author = str(item['book_author'][0]).replace(' ', '').replace('\n', '')
            l_rating_num = str(item['book_rating_num'][0]).replace(' ','')
            l_rating_peo = str(item['book_rating_peo'][0]).replace(' ','')
        except:
            l_rating_num = '-1'
            l_rating_peo = '-1'
        csv_file.writerow([l_num,l_title,l_author,l_rating_num,l_rating_peo])
