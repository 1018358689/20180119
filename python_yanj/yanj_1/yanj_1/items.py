# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Yanj1Item(scrapy.Item):
    yanj_num = scrapy.Field()
    yanj_title = scrapy.Field()
    yanj_author = scrapy.Field()
    yanj_link = scrapy.Field()
    yanj_price = scrapy.Field()
    yanj_read = scrapy.Field()
    yanj_down = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
