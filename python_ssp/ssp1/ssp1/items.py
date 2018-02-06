# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Ssp1Item(scrapy.Item):
    ssp_title = scrapy.Field()
    ssp_author = scrapy.Field()
    ssp_like = scrapy.Field()
    # ssp_link = scrapy.Field()
    # ssp_summary = scrapy.Field()
    # ssp_h2 = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
