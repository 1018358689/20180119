#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml.html import etree
import re
import webbrowser

def open_web(Question):
    webbrowser.open('https://www.baidu.com/s?wd=%s' % Question)

def word_count(Question, Answer):
    content = requests.get(url='http://www.baidu.com/s', params={'wd': Question}).text
    count = []
    if '不是' in Question:
        print('**请注意此题为否定题,选计数最少的**')
    print('词频计数：')
    for word in Answer:
        count.append(content.count(word))
    p_it(Answer, count)


def result_count(Question, Answer):
    count = []
    if '不是' in Question:
        print('**请注意此题为否定题,选计数最少的**')
    print('结果计数：')
    for word in Answer:
        wd = '{}+{}'.format(Question, word)
        content = requests.get(url='http://www.baidu.com/s', params={'wd': wd}).content
        dom_tree = etree.HTML(content)
        result = dom_tree.xpath('//div[@class="nums"]/text()')[0]
        result = int(re.findall('[\d,]+', result)[0].replace(',', ''))
        count.append(result)
    p_it(Answer, count)


def p_it(Answer, count):
    for i in range(len(Answer)):
        print('{0}.{1:{3}<9}:{2}'.format(i + 1, Answer[i], count[i], chr(12288)))
    print('')
