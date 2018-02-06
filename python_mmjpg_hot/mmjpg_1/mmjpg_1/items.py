# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Mmjpg1Item(scrapy.Item):
    mmjpg_url = scrapy.Field()
    mmjpg_title = scrapy.Field()
    mmjpg_path = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
