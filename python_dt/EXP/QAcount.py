#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml.html import etree
import re

def Q_A_count(Question, Answer):
    count = []
    # print('QA搜索结果计数：')
    for word in Answer:
        # wd = '{} +{}'.format(Question, word)
        wd = Question + word
        res = requests.get(url='http://www.baidu.com/s', params={'wd': wd}).text
        # res = requests.get(url='http://www.sogou.com/sogou', params={'query': wd}).text
        # result = int(re.findall('(?<=百度为您找到相关结果约).*(?=个)', content)[0].replace(',', ''))
        dom_tree = etree.HTML(res)
        # result = dom_tree.xpath('//div[@class="nums"]/text()')[0]
        result = dom_tree.xpath('//p[@class="num-tips"]/text()')[0]
        result = int(re.findall('[\d,]+', result)[0].replace(',', ''))
        count.append(result)
    # p_it(Answer, count)
    return count, 'Q_A'

def Question_count(Question):
    # print('Q搜索结果计数：')
    wd = Question
    # res = requests.get(url='http://www.baidu.com/s', params={'wd': wd}).text
    res = requests.get(url='http://www.sogou.com/sogou', params={'query': wd}).text
    # result = int(re.findall('(?<=百度为您找到相关结果约).*(?=个)', content)[0].replace(',', ''))
    dom_tree = etree.HTML(res)
    # result = dom_tree.xpath('//div[@class="nums"]/text()')[0]
    result = dom_tree.xpath('//p[@class="num-tips"]/text()')[0]
    result = int(re.findall('[\d,]+', result)[0].replace(',', ''))
    # print('{0:{2}<9}{1}'.format(Question, result, chr(12288)))
    return result

Que = '新装修的房子通常哪种化学物质含量会比较高?'
Ans = ['甲醛', '苯', '甲醇']
a, b =Q_A_count(Que, Ans)
print(a)