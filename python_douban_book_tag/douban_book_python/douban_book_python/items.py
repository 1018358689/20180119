# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookPythonItem(scrapy.Item):
    book_num =scrapy.Field()
    book_title = scrapy.Field()
    book_rating_num = scrapy.Field()
    book_rating_peo = scrapy.Field()
    book_author = scrapy.Field()
    book_from = scrapy.Field()
    book_time = scrapy.Field()
    book_much = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
