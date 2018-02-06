#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy import cmdline

name = 'douban_new_movies'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())