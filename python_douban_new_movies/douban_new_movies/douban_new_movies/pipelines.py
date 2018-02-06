# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class DoubanNewMoviesPipeline(object):

    # def __init__(self):
    #     self.file = codecs.open('douban_new_movies.json', 'wb', encoding='utf-8')

    def open_spider(self, spider):
        self.file = codecs.open('douban_new_movies.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = 'THE NEW MOVIES LIST : \n'
        for i in range(len(item['movie_star'])):
            name = {'movie_name': str(item['movie_name'][i]).replace(' ', '').replace('\n','').replace('/','')}
            star = {'movie_star': str(item['movie_star'][i]).replace(' ', '')}
            url = {'movie_url': str(item['movie_url'][i]).replace(' ', '')}
            line += json.dumps(name, ensure_ascii=False)
            line += json.dumps(star, ensure_ascii=False)
            line += json.dumps(url, ensure_ascii=False)
            line += '\n'
        self.file.write(line)

    def close_spider(self, spider):
        self.file.close()