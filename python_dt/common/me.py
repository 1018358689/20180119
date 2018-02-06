#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml.html import etree
import re
import webbrowser


def open_web(Question):
    # webbrowser.open('https://www.baidu.com/s?wd=%s' % Question)
    webbrowser.open('http://www.sogou.com/sogou?query=%s' % Question)


def result_count(Question, Answer):
    count = []
    print('结果计数：')
    for word in Answer:
        wd = '{} +{}'.format(Question, word)
        res = requests.get(url='http://www.baidu.com/s', params={'wd': Question + word}).text
        # res = requests.get(url='http://www.sogou.com/sogou', params={'query': wd}).text
        # result = int(re.findall('(?<=百度为您找到相关结果约).*(?=个)', content)[0].replace(',', ''))
        dom_tree = etree.HTML(res)
        result = dom_tree.xpath('//div[@class="nums"]/text()')[0]
        # result = dom_tree.xpath('//p[@class="num-tips"]/text()')[0]
        result = int(re.findall('[\d,]+', result)[0].replace(',', ''))
        count.append(result)
    p_it(Answer, count)
    return count


def word_count(Question, Answer):
    res = requests.get(url='http://www.baidu.com/s', params={'wd': Question}).text
    # res = requests.get(url='http://www.sogou.com/sogou', params={'query': Question}).text
    dom_tree = etree.HTML(res)
    content = dom_tree.xpath('//div[@id="content_left"]//text()')
    content = ''.join(content).replace('\t','').replace(' ','').replace('\n','')
    # content = dom_tree.xpath('string(.)')
    # print(content)
    count = []
    print('词频计数：')
    for word in Answer:
        count.append(content.count(word))
    p_it(Answer, count)
    return count


def repeat_w_count(w_count, count): #监测重复项
    if w_count.count(w_count[count]) > 1:
        return True
    else:
        return False


def solve2methods(Answer, r_count, w_count, temp):
    result_count_max = r_count.index(max(r_count))
    result_count_min = r_count.index(min(r_count))
    word_count_max = w_count.index(max(w_count))
    word_count_min = w_count.index(min(w_count))
    if temp == 'NO':
        result_count_idx = result_count_min
        word_count_idx = word_count_min
    else:
        result_count_idx = result_count_max
        word_count_idx = word_count_max

    if repeat_w_count(w_count, word_count_idx):
        print('推荐答案为: {}.{}'.format(result_count_idx + 1, Answer[result_count_idx]))
    else:
        if result_count_idx == word_count_idx:
            print('推荐答案为: {}.{}'.format(result_count_idx + 1, Answer[result_count_idx]))
        else:
            print('推荐答案为: {}.{}\n参考答案为: {}.{}\n自己斟酌吧.'.format(word_count_idx + 1, Answer[word_count_idx],
                                                              result_count_idx + 1, Answer[result_count_idx]))


def p_it(Answer, count):
    for i in range(len(Answer)):
        print('{0}.{1:{3}<9}{2}'.format(i + 1, Answer[i], count[i], chr(12288)))
    print('')
